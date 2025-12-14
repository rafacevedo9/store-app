# products/infrastructure/models.py

from django.db import models

class Producto(models.Model):
    # Requisitos exactos de la actividad[cite: 19, 20, 21, 22]:
    id = models.AutoField(primary_key=True)  # Identificador único
    nombre = models.CharField(max_length=200) # Nombre del producto
    descripcion = models.TextField()          # Descripción breve
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Valor numérico

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos' # Buenas prácticas SQL