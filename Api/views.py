from rest_framework import viewsets

from .serializers import HeroSerializer, PersonaSerializer, ProductoSerializer, ProveedoresSerializer, PatologiaSerializer, PacienteSerializer, MedicoSerializer, DosificacionSerializer, DiagnosticoSerializer, RecetasDetSerializer, RecetasEncSerializer,ApiModelSerializer
from .models import Hero, Persona, Producto, Proveedores, Patologia, Paciente, Medico, Dosificacion, Diagnostico, RecetasDet, RecetasEnc, Api
from .utils import admin_only

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all().order_by('nombre')
    serializer_class = PersonaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer

class PatologiaViewSet(viewsets.ModelViewSet):
    queryset = Patologia.objects.all()
    serializer_class = PatologiaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class =  MedicoSerializer

class DosificacionViewSet(viewsets.ModelViewSet):
    queryset = Dosificacion.objects.all()
    serializer_class = DosificacionSerializer

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class RecetasViewSet(viewsets.ModelViewSet):
    queryset = RecetasEnc.objects.all()
    serializer_class = RecetasEncSerializer

class RecetasDetViewSet(viewsets.ModelViewSet):
    queryset = RecetasDet.objects.all()
    serializer_class = RecetasDetSerializer

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiModelSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

