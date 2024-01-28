from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ApiViewSet

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'personas', views.PersonaViewSet)
router.register(r'producto', views.ProductoViewSet)
router.register(r'proveedor', views.ProveedoresViewSet)
router.register(r'Paciente', views.PacienteViewSet)
router.register(r'medico', views.MedicoViewSet)
router.register(r'patologia', views.PatologiaViewSet)
router.register(r'dosificacion', views.DosificacionViewSet)
router.register(r'diagnostico', views.DiagnosticoViewSet)
router.register(r'recetas', views.RecetasViewSet)
router.register(r'recetas', views.RecetasDetViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
