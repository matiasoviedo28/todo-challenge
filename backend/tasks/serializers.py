from rest_framework import serializers
from tasks.models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    """Serializador para validar los datos de Tarea."""

    completada = serializers.BooleanField(
        required=True, error_messages={"invalid": "El campo 'completada' debe ser True o False."}
    )

    titulo = serializers.CharField(
        required=True, allow_blank=False, error_messages={"blank": "El título no puede estar vacío."}
    )

    descripcion = serializers.CharField(
        required=True, allow_blank=False, error_messages={"blank": "La descripción no puede estar vacía."}
    )

    def validate(self, data):
        """Evita tareas duplicadas si todos los campos son iguales."""
        if Tarea.objects.filter(
            titulo=data["titulo"], 
            descripcion=data["descripcion"], 
            completada=data["completada"]
        ).exists():
            raise serializers.ValidationError("Ya existe una tarea con estos mismos datos.")
        return data

    class Meta:
        model = Tarea
        fields = '__all__'

