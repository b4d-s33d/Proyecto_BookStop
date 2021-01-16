from django.shortcuts import render
from .models import Libro, Autor, Genero


#Para creación de forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

# Create your views here.
def index(request):
    num_books = Libro.objects.all().count()
    num_authors = Autor.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_authors':num_authors,}
    )

def ranking(request):  
    books = Libro.objects.all()
    return render(request, 'ranking.html', context={'books':books,})  
    

def login(request):  
    return render(request, 'login.html')  

def register(request):  
    return render(request, 'register.html')  
 



class CrearLibro(CreateView):
    model = Libro
    fields = '__all__'
    
class ActualizarLibro(UpdateView):
    model = Libro
    fields = '__all__'

class EliminarLibro(DeleteView):
    model = Libro
    success_url = reverse_lazy('ranking')            

class BookDetailView(generic.DetailView):
    model = Libro
  


class CrearAutor(CreateView):
    model = Autor
    fields = '__all__'
    
class ActualizarAutor(UpdateView):
    model = Autor
    fields = '__all__'

class EliminarAutor(DeleteView):
    model = Autor
    success_url = reverse_lazy('ranking')            

class AuthorDetailView(generic.DetailView):
    model = Autor



