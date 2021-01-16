from django.test import TestCase
from login.models import Libro, Autor

class LibroModelTest(TestCase):

    @classmethod

    #setUpTestData()
    def setUpTestData(cls):
        Libro.objects.create(titulo='El principito', resumen='Resumen del libro', isbn='9784483555128') 

    def test_titulo_label(self):
        libro=Libro.objects.get(id=1)
        field_label = libro._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label,'titulo')
        
    def test_resumen_label(self):
        libro=Libro.objects.get(id=1)
        field_label = libro._meta.get_field('resumen').verbose_name
        self.assertEquals(field_label,'resumen')

    def test_isbn_label(self):
        libro=Libro.objects.get(id=1)
        field_label = libro._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label,'ISBN')        
    
    def test_titulo_max_length(self):
        libro=Libro.objects.get(id=1)
        max_length = libro._meta.get_field('titulo').max_length
        self.assertEquals(max_length,200)

    def test_resumen_max_length(self):
        libro=Libro.objects.get(id=1)
        max_length = libro._meta.get_field('resumen').max_length
        self.assertEquals(max_length,1000)

    def test_isbn_max_length(self):
        libro=Libro.objects.get(id=1)
        max_length = libro._meta.get_field('isbn').max_length
        self.assertEquals(max_length,13)    
    
    #setUp()
    def setUp(self):
        a1=Autor.objects.create(nombre="Albert Camus")
        a2=Autor.objects.create(nombre="Simone de Beauvoir")
        Libro.objects.create(titulo="El extranjero", autor=a1, resumen="Resumen del libro")
        Libro.objects.create(titulo="El segundo sexo", autor=a2, resumen="Resumen del libro")
    
    def test_libro_autor(self):
        book1 = Libro.objects.get(titulo="El segundo sexo")
        self.assertEqual(book1.autor.nombre, "Simone de Beauvoir")
        book2 = Libro.objects.get(titulo="El extranjero")
        self.assertEqual(book2.autor.nombre, "Albert Camus")


class AutorModelTest(TestCase):

    @classmethod
    
    #setUpTestData()
    def setUpTestData(cls):
        Autor.objects.create(nombre='Milan', apellido='Kundera') 

    def test_nombre_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_fecha_fall_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('fecha_fall').verbose_name
        self.assertEquals(field_label,'Fecha fall')    