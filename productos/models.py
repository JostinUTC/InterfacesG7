from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre_materia = models.CharField(max_length=100)
    precio_materia = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name='precio')
    creditos_materia = models.IntegerField()
    num_estudiantes_materia = models.IntegerField()

    def __str__(self):
        return self.nombre_materia


