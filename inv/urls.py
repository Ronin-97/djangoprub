from django.urls import path

from .views import PersonaView, PersonaNew, PersonaEdit, persona_inactivar, \
     ProveedoresView, ProveedoresNew, ProveedoresEdit, proveedores_inactivar, \
     MedicoView, MedicoNew, MedicoEdit, medico_inactivar, \
     PatologiaView, PatologiaNew, PatologiaEdit, patologia_inactivar, \
     PacienteView, PacienteNew, PacienteEdit, paciente_inactivar, \
     DosificacionView, DosificacionNew, DosificacionEdit, dosificacion_inactivar, \
     DiagnosticoView, DiagnosticoNew, DiagnosticoEdit, diagnostico_inactivar, \
     ProductoView, ProductoNew, ProductoEdit, producto_inactivar, \
     RecetasView, recetas, RecetaDetDelete

urlpatterns = [
    path('personas/', PersonaView.as_view(), name='persona_list'),
    path('personas/new', PersonaNew.as_view(), name='persona_new'),
    path('personas/edit/<int:pk>', PersonaEdit.as_view(), name='persona_edit'),
    path('personas/inactivar/<int:id>', persona_inactivar, name='persona_inactivar'),

    path('proveedores/', ProveedoresView.as_view(), name='proveedor_list'),
    path('proveedores/new', ProveedoresNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>', ProveedoresEdit.as_view(), name='proveedor_edit'),
    path('proveedores/inactivar/<int:id>', proveedores_inactivar, name='proveedor_inactivar'),

    path('medicos/', MedicoView.as_view(), name='medico_list'),
    path('medicos/new', MedicoNew.as_view(), name='medico_new'),
    path('medicos/edit/<int:pk>', MedicoEdit.as_view(), name='medico_edit'),
    path('medicos/inactivar/<int:id>', medico_inactivar, name='medico_inactivar'),

    path('patologias/', PatologiaView.as_view(), name='patologia_list'),
    path('patologias/new', PatologiaNew.as_view(), name='patologia_new'),
    path('patologias/edit/<int:pk>', PatologiaEdit.as_view(), name='patologia_edit'),
    path('patologias/inactivar/<int:id>', patologia_inactivar, name='patologia_inactivar'),

    path('pacientes/', PacienteView.as_view(), name='paciente_list'),
    path('pacientes/new', PacienteNew.as_view(), name='paciente_new'),
    path('pacientes/edit/<int:pk>', PacienteEdit.as_view(), name='paciente_edit'),
    path('pacientes/inactivar/<int:id>', paciente_inactivar, name='paciente_inactivar'),

    path('dosificaciones/', DosificacionView.as_view(), name='dosificacion_list'),
    path('dosificaciones/new', DosificacionNew.as_view(), name='dosificacion_new'),
    path('dosificaciones/edit/<int:pk>', DosificacionEdit.as_view(), name='dosificacion_edit'),
    path('dosificaciones/inactivar/<int:id>', dosificacion_inactivar, name='dosificacion_inactivar'),

    path('diagnosticos/', DiagnosticoView.as_view(), name='diagnostico_list'),
    path('diagnosticos/new', DiagnosticoNew.as_view(), name='diagnostico_new'),
    path('diagnosticos/edit/<int:pk>', DiagnosticoEdit.as_view(), name='diagnostico_edit'),
    path('diagnosticos/inactivar/<int:id>', diagnostico_inactivar, name='diagnostico_inactivar'),

    path('productos/', ProductoView.as_view(), name='producto_list'),
    path('productos/new', ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('productos/inactivar/<int:id>', producto_inactivar, name='producto_inactivar'),

    path('recetas/', RecetasView.as_view(), name='recetas_list'),
    path('recetas/new', recetas, name='recetas_new'),
    path('recetas/edit/<int:receta_id>', recetas, name='recetas_edit'),
    path('recetas/<int:receta_id>/delete/<int:pk>', RecetaDetDelete.as_view(), name='recetas_del'),
]