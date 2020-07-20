from rest_framework import serializers
from .models import *

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields= '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields= '__all__'