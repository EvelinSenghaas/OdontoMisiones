from rest_framework import viewsets
from .models import *
from .serializer import ClienteSerializer
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer