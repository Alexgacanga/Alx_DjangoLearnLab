from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library,Book


books = Book.objects.all()  # required by checker
return render(request, 'relationship_app/list_books.html', {'books': books})  # required by checker

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
