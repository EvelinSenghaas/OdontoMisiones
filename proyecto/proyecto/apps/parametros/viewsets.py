from rest_framework import viewsets
from .models import *
from .serializer import *

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer

class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer