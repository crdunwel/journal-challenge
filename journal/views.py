from django.views.generic import CreateView
from django.views.generic.list import ListView

from journal.forms import JournalEntryForm
from journal.models import JournalEntry
from django.contrib.auth.mixins import LoginRequiredMixin


class JournalEntryListView(LoginRequiredMixin, ListView):

    model = JournalEntry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)


class JournalEntryCreate(CreateView):
    success_url = '/journal/'
    model = JournalEntry
    fields = ['title', 'body']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


# class JournalEntryUpdate(UpdateView):
#     success_url = '/journal/'
#     model = JournalEntry
#     fields = ['title', 'body']
#
