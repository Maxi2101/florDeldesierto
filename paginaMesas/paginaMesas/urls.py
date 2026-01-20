from django.contrib import admin
from django.urls import path
from contactos import views as vista 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vista.index,name='index'),
]
