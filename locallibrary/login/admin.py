from django.contrib import admin

# Register your models here.
from . models import Genero, Libro, Autor

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Genero)