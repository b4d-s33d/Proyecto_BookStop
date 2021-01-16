from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ranking', views.ranking, name='ranking'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/create', views.CrearLibro.as_view(), name='crear_libro'),
    path('book/<int:pk>/update', views.ActualizarLibro.as_view(), name='actualizar_libro'),
    path('book/<int:pk>/delete', views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create', views.CrearAutor.as_view(), name='crear_autor'),
    path('author/<int:pk>/update', views.ActualizarAutor.as_view(), name='actualizar_autor'),
    path('author/<int:pk>/delete', views.EliminarAutor.as_view(), name='eliminar_autor'),
]

