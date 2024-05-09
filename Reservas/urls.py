from django.contrib import admin
from django.urls import path
from webapp.views import index, reservar, reservas, login, exportar_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('reservar/', reservar, name='reservar'),
    path('reservas/',reservas, name='reservas'),
    path('login/', login, name='login'),   # Renombrar la vista de inicio de sesión
    path('exportar_excel/', exportar_excel, name='exportar_excel'),              
]
