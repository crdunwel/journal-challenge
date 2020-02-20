from django.views.generic.list import ListView
from journal.models import JournalEntry
from django.contrib.auth.mixins import LoginRequiredMixin


class JournalEntryListView(LoginRequiredMixin, ListView):

    model = JournalEntry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
