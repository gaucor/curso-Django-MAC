from django.db import models

# Create your models here.
class Libro(models.Model):
    Titulo= models.CharField(max_length=150)


    def str_(self):
        return self.titulo