from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
<!-- Book: 1984 by George Orwell (1949) -->


retrieved = Book.objects.get(id=book.id)
retrieved.title, retrieved.author, retrieved.publication_year
<!-- ('1984', 'George Orwell', 1949) -->


book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
book.title
<!-- 'Nineteen Eighty-Four' -->



book.delete()
Book.objects.all()
<!-- <QuerySet []>    -->