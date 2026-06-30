from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=100)
    sueldo_profesor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='sueldo')
    
    curso_profesor = models.IntegerField() 

    def __str__(self):
        return self.nombre_profesor