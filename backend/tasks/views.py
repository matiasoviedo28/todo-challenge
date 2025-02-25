from django_filters import rest_framework as filters
from rest_framework import viewsets, filters as drf_filters
from .models import Tarea
from .serializers import TareaSerializer
import logging
logger = logging.getLogger(__name__)


class TareaFilter(filters.FilterSet):
    fecha_creacion = filters.DateFromToRangeFilter()

    class Meta:
        model = Tarea
        fields = ['fecha_creacion']

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('-fecha_creacion')
    serializer_class = TareaSerializer
    filter_backends = [filters.DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = TareaFilter
    search_fields = ['titulo', 'descripcion']
    def list(self, request, *args, **kwargs):

        logger.info("Se accedió a la lista de tareas")
        return super().list(request, *args, **kwargs)
