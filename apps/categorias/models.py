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
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
          return f"{self.nombre} - {self.tipo}"