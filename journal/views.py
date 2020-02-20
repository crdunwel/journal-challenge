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


class JournalEntryCreate(CreateView):
    success_url = '/journal/'
    model = JournalEntry
    fields = ['title', 'body']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class JournalEntryDelete(DeleteView):
    success_url = '/journal/'
    model = JournalEntry



# class JournalEntryUpdate(UpdateView):
#     success_url = '/journal/'
#     model = JournalEntry
#     fields = ['title', 'body']
#
