from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

"""
URL Routing for Book API
------------------------

Each path maps to one of the generic views.
These endpoints provide full CRUD functionality.

Patterns:
    /books/                     -> List all books
    /books/<int:pk>/            -> Retrieve single book
    /books/create/              -> Create book
    /books/<int:pk>/update/     -> Update book
    /books/<int:pk>/delete/     -> Delete book
"""

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
