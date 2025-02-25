from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
