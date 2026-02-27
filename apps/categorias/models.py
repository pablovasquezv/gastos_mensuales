from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(
        max_length=10, 
        choices=[('INGRESO', 'Ingreso'), ('GASTO', 'Gasto')],
        default='GASTO'
    )
    color = models.CharField(max_length=7, default='#10b981')  # Verde por defecto
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
          return f"{self.nombre} - {self.tipo}"