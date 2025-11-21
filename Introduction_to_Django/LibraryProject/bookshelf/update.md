book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
book.title


<!-- 'Nineteen Eighty-Four' -->