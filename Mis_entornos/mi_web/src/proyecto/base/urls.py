from django.urls import path
from .views import ListaPendientes,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea,PaginaRegistro, Logueo
from django.contrib.auth.views import LogoutView
urlpatterns = [path('',ListaPendientes.as_view(),name='tareas'),
            path('login/',Logueo.as_view(),name='login'),
            path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
            path('registro/',PaginaRegistro.as_view(),name='registro'),
            path('tarea/<int:pk>',DetalleTarea.as_view(),name='tarea'),
            path('crear_tarea',CrearTarea.as_view(),name='crear-tarea'),
            path('editar_tarea/<int:pk>',EditarTarea.as_view(),name='editar-tarea'),
            path('eliminar_tarea/<int:pk>',EliminarTarea.as_view(),name='eliminar-tarea')] 