# Book API — Generic Views (Django REST Framework)

This module demonstrates the use of Django REST Framework’s generic views
and permission classes to build clean, reusable CRUD endpoints for the
Book model.

## Views Implemented

### 1. BookListView (GET)
- Returns all books
- Public access

### 2. BookDetailView (GET)
- Returns a single book by ID
- Public access

### 3. BookCreateView (POST)
- Creates a new book
- Requires authentication
- Uses `perform_create()` for custom logic

### 4. BookUpdateView (PUT/PATCH)
- Updates an existing book
- Requires authentication
- Uses `perform_update()` for custom behavior

### 5. BookDeleteView (DELETE)
- Deletes a book
- Requires authentication

## Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/api/books/` | GET | List all books |
| `/api/books/<pk>/` | GET | Get book by ID |
| `/api/books/create/` | POST | Create new book |
| `/api/books/<pk>/update/` | PUT/PATCH | Update book |
| `/api/books/<pk>/delete/` | DELETE | Delete book |

## Permissions

- Unauthenticated users: **Read-only**
- Authenticated users: **Full CRUD**

## Testing
Use curl or Postman to test creation, updates, and deletions.
