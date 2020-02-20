from datetime import datetime

from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, DeleteView
from django.views.generic.list import ListView

from journal.models import JournalEntry
from django.contrib.auth.mixins import LoginRequiredMixin


class JournalEntryListView(LoginRequiredMixin, ListView):

    model = JournalEntry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        journal_entries = JournalEntry.objects.filter(user=self.request.user).order_by('-pub_date')

        start_date, end_date = self._get_start_end_date()

        if start_date and not end_date:
            return journal_entries.filter(pub_date__date__gte=start_date)
        elif end_date and not start_date:
            return journal_entries.filter(pub_date__date__lte=end_date)
        elif start_date and end_date:
            return journal_entries.filter(pub_date__date__range=(start_date, end_date))
        else:
            return journal_entries

    def _get_start_end_date(self):
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)

        def get_datetime(date_str):
            if date_str is not None:
                try:
                    return datetime.strptime(date_str, '%m/%d/%Y')
                except ValueError:
                    return None

        return get_datetime(start_date), get_datetime(end_date)


class JournalEntryCreate(LoginRequiredMixin, CreateView):
    success_url = '/journal/'
    model = JournalEntry
    fields = ['title', 'body']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class JournalEntryDelete(LoginRequiredMixin, DeleteView):
    success_url = '/journal/'
    model = JournalEntry

    def get_object(self, queryset=None):
        journal_entry = super().get_object(queryset)
        if journal_entry.user != self.request.user:
            raise PermissionDenied
        return journal_entry


from django.contrib.auth import logout

# TODO
# class JournalEntryUpdate(UpdateView):
#     success_url = '/journal/'
#     model = JournalEntry
#     fields = ['title', 'body']
#
