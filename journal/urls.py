from django.urls import path
from journal.views import JournalEntryListView, JournalEntryCreate, JournalEntryDelete

urlpatterns = [
    path('journal/', JournalEntryListView.as_view(), name='journalentry-list'),
    path('journal/create', JournalEntryCreate.as_view(), name='journalentry-list-create'),
    path('journal/delete/<int:pk>', JournalEntryDelete.as_view(), name='journalentry-list-delete'),
]
