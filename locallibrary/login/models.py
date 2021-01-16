from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.
class Genero(models.Model):
    #Model representing a book genre."""
	nombre = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre

class Libro(models.Model):
    
	titulo = models.CharField(max_length=200)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)   
	resumen = models.TextField(max_length=1000, help_text='Ingrese una breve descripción del libro')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="isbn-international.org/content/what-isbn">ISBN number</a>')
	genero = models.ManyToManyField(Genero)
	caratula = models.ImageField(upload_to='libros', default='undefined.png')
    
	def __str__(self):
		return self.titulo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('book-detail', args=[str(self.id)])


class Autor(models.Model):
	"""Model representing an author."""
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	fecha_nac = models.DateField('Fecha Nacimiento', null=True, blank=True)
	fecha_fall = models.DateField('Fecha fall', null=True, blank=True)

	class Meta:
		ordering = ['apellido', 'nombre']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.nombre}'	        
