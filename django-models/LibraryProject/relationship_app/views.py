from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library,Book
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View

books = Book.objects.all()  
return render(request, 'relationship_app/list_books.html', {'books': books})  

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # Auto login after registration
            return redirect('list_books')  # Redirect anywhere you prefer
        return render(request, 'relationship_app/register.html', {'form': form})
