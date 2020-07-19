from rest_framework import serializers
from .models import *

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields= '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields= '__all__'

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields= '__all__'

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields= '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields= '__all__'