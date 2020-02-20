from django.urls import path
from journal.views import JournalEntryListView

urlpatterns = [
    path('journal/', JournalEntryListView.as_view(), name='journalentry-list')
]
