from rest_framework import serializers

from .models import Hero, Api
from inv.models import Persona,  Proveedores, Medico, Patologia, Paciente, Dosificacion, Diagnostico, Producto, RecetasEnc, RecetasDet

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Persona
         fields = ('cedula', 'nombre', 'apellido')

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PatologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patologia
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class DosificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosificacion
        fields = '__all__'

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class RecetasEncSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetasEnc
        fields = '__all__'

class RecetasDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetasDet
        fields = '__all__'

class ApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = '__all__'
