from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

"""
Generic Views for Book API
--------------------------

The following views provide CRUD operations using Django REST Framework’s
powerful generic class-based views. These views reduce boilerplate code
by handling common patterns such as retrieving objects, validating input,
saving data, and rendering responses.

Views Included:
    - BookListView: Lists all books (GET)
    - BookDetailView: Retrieve a single book by ID (GET)
    - BookCreateView: Create a new book (POST)
    - BookUpdateView: Update an existing book (PUT/PATCH)
    - BookDeleteView: Delete a book (DELETE)

Permissions:
    - Read-only: Unauthenticated users may access list & detail views.
    - Write operations: Require authenticated users.

Customization:
    - BookCreateView and BookUpdateView override `perform_create` and
      `perform_update` to allow custom logic during save operations.
"""


class BookListView(generics.ListAPIView):
    """
    ListView: Returns a list of all books.

    Permissions:
        - Accessible by anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView: Retrieves a single book by primary key (ID).

    Permissions:
        - Accessible by anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView: Allows authenticated users to create a new book.

    Custom Behavior:
        - perform_create(): hook to add custom logic before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom save behavior.
        You can insert logging, analytics, or other side effects here.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Retrieve the book instance using ?pk=<id>
        """
        pk = self.request.query_params.get("pk")
        return generics.get_object_or_404(Book, pk=pk)

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Retrieve the book instance using ?pk=<id>
        """
        pk = self.request.query_params.get("pk")
        return generics.get_object_or_404(Book, pk=pk)
