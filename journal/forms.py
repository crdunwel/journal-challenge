from django.forms import ModelForm
from journal.models import JournalEntry


class JournalEntryForm(ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'body']
