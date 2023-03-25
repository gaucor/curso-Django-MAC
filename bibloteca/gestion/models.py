from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(verbose_name="título del libro", max_length=255)
    sinopsis = models.TextField(verbose_name="sinopsis", max_length=500)
    portada = models.ImageField(verbose_name="Portada del Libro", upload_to="imagenes/libro/portadas/")
    isbn = models.CharField(verbose_name="isbn", max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


class Autor(models.Model):
    nombre = models.CharField(verbose_name='Nombre del autor', max_length=80)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=80)
    pseudonimo = models.CharField(verbose_name='Pseudónimo', max_length=100)
    nacionalidad = models.CharField(verbose_name='Nacionalidad', max_length=100)
    fechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    fechaFallecimiento = models.DateField(verbose_name='Fecha de fallecimiento', null=True, blank=True)
    foto = models.ImageField(verbose_name='Imagen del autor', upload_to='images/autor/foto')

    def __str__(self):
        return "{0} {1} -- {2}".format(self.nombre, self.apellidos, self.nacionalidad)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Editorial(models.Model):
    nombre = models.CharField(verbose_name="Editorial", max_length=100, unique=True)
    telefono = models.CharField(verbose_name="teléfono", max_length=15, null=True, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editorales"