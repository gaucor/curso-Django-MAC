from django.contrib import admin
from .models import Libro, Autor, Editorial
# Register your models here.
class Libroadmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "editorial", "sinopsis", "isbn")
    list_filter =  ("autor", "editorial")
    ordering = ("titulo", "autor", "editorial", "sinopsis", "isbn")
    search_fields = ("titulo", "sinopsis", "isbn")

admin.site.register(Libro, Libroadmin)

class AutorAdmin (admin.ModelAdmin):
    list_display = ("nombre", "apellidos", "pseudonimo", "nacionalidad", "fechaNacimiento", "fechaFallecimiento", "foto")
    search_fields = ("nombre", "apellidos", "pseudonimo", "nacionalidad")

admin.site.register(Autor, AutorAdmin)

class EditorialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono")

admin.site.register(Editorial, EditorialAdmin)

