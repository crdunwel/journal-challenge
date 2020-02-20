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
        return JournalEntry.objects.filter(user=self.request.user).order_by('-pub_date')


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
