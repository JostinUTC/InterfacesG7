from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Directiva(models.Model):
   
    nombre_directiva = models.CharField(max_length=100)
    cargo_directiva = models.CharField(max_length=100)
    presupuesto_directiva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='presupuesto')
    num_integrantes = models.IntegerField()

    def __str__(self):
      
        return self.nombre_directiva