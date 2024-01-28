from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json
from django.db.models import Sum

from .models import Persona, Proveedores, Medico, Patologia, Paciente, Dosificacion, Diagnostico, Producto, \
     RecetasEnc, RecetasDet
from .forms import PersonaForm, MedicoForm, ProveedoresForm, PatologiaForm, PacienteForm, DosificacionForm, \
     DiagnosticoForm, ProductoForm, RecetasEncForm

# Create your views here.
class PersonaView(LoginRequiredMixin, generic.ListView):
    model = Persona
    template_name = "inv/persona_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class PersonaNew(LoginRequiredMixin, generic.CreateView):
    model = Persona
    template_name = "inv/persona_form.html"
    context_object_name = "obj"
    form_class = PersonaForm
    success_url = reverse_lazy("inv:persona_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PersonaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Persona
    template_name = "inv/persona_form.html"
    context_object_name = "obj"
    form_class = PersonaForm
    success_url = reverse_lazy("inv:persona_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def persona_inactivar(request, id):
    persona = Persona.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not persona:
        return redirect("inv:persona_list")

    if request.method=='GET':
        contexto={'obj':persona}

    if request.method=='POST':
        persona.estado=False
        persona.save()
        return redirect("inv:persona_list")

    return render(request, template_name, contexto)


class ProveedoresView(LoginRequiredMixin, generic.ListView):
    model = Proveedores
    template_name = "inv/proveedor_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProveedoresNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedores
    template_name = "inv/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedoresForm
    success_url = reverse_lazy("inv:proveedor_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedoresEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedores
    template_name = "inv/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedoresForm
    success_url = reverse_lazy("inv:proveedor_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def proveedores_inactivar(request, id):
    proveedor = Proveedores.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not proveedor:
        return redirect("inv:proveedor_list")

    if request.method=='GET':
        contexto={'obj':proveedor}

    if request.method=='POST':
        proveedor.estado=False
        proveedor.save()
        return redirect("inv:proveedor_list")

    return render(request, template_name, contexto)


class MedicoView(LoginRequiredMixin, generic.ListView):
    model = Medico
    template_name = "inv/medico_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class MedicoNew(LoginRequiredMixin, generic.CreateView):
    model = Medico
    template_name = "inv/medico_form.html"
    context_object_name = "obj"
    form_class = MedicoForm
    success_url = reverse_lazy("inv:medico_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MedicoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Medico
    template_name = "inv/medico_form.html"
    context_object_name = "obj"
    form_class = MedicoForm
    success_url = reverse_lazy("inv:medico_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def medico_inactivar(request, id):
    medico = Medico.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not medico:
        return redirect("inv:medico_list")

    if request.method=='GET':
        contexto={'obj':medico}

    if request.method=='POST':
        medico.estado=False
        medico.save()
        return redirect("inv:medico_list")

    return render(request, template_name, contexto)


class PatologiaView(LoginRequiredMixin, generic.ListView):
    model = Patologia
    template_name = "inv/patologia_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class PatologiaNew(LoginRequiredMixin, generic.CreateView):
    model = Patologia
    template_name = "inv/patologia_form.html"
    context_object_name = "obj"
    form_class = PatologiaForm
    success_url = reverse_lazy("inv:patologia_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PatologiaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Patologia
    template_name = "inv/patologia_form.html"
    context_object_name = "obj"
    form_class = PatologiaForm
    success_url = reverse_lazy("inv:patologia_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def patologia_inactivar(request, id):
    patologia = Patologia.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not patologia:
        return redirect("inv:patologia_list")

    if request.method=='GET':
        contexto={'obj':patologia}

    if request.method=='POST':
        patologia.estado=False
        patologia.save()
        return redirect("inv:patologia_list")

    return render(request, template_name, contexto)


class PacienteView(LoginRequiredMixin, generic.ListView):
    model = Paciente
    template_name = "inv/paciente_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class PacienteNew(LoginRequiredMixin, generic.CreateView):
    model = Paciente
    template_name = "inv/paciente_form.html"
    context_object_name = "obj"
    form_class = PacienteForm
    success_url = reverse_lazy("inv:paciente_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PacienteEdit(LoginRequiredMixin, generic.UpdateView):
    model = Paciente
    template_name = "inv/paciente_form.html"
    context_object_name = "obj"
    form_class = PacienteForm
    success_url = reverse_lazy("inv:paciente_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def paciente_inactivar(request, id):
    paciente = Paciente.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not paciente:
        return redirect("inv:paciente_list")

    if request.method=='GET':
        contexto={'obj':paciente}

    if request.method=='POST':
        paciente.estado=False
        paciente.save()
        return redirect("inv:paciente_list")

    return render(request, template_name, contexto)


class DosificacionView(LoginRequiredMixin, generic.ListView):
    model = Dosificacion
    template_name = "inv/dosificacion_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class DosificacionNew(LoginRequiredMixin, generic.CreateView):
    model = Dosificacion
    template_name = "inv/dosificacion_form.html"
    context_object_name = "obj"
    form_class = DosificacionForm
    success_url = reverse_lazy("inv:dosificacion_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class DosificacionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Dosificacion
    template_name = "inv/dosificacion_form.html"
    context_object_name = "obj"
    form_class = DosificacionForm
    success_url = reverse_lazy("inv:dosificacion_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def dosificacion_inactivar(request, id):
    dosificacion = Dosificacion.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not dosificacion:
        return redirect("inv:dosificacion_list")

    if request.method=='GET':
        contexto={'obj':dosificacion}

    if request.method=='POST':
        dosificacion.estado=False
        dosificacion.save()
        return redirect("inv:dosificacion_list")

    return render(request, template_name, contexto)


class DiagnosticoView(LoginRequiredMixin, generic.ListView):
    model = Diagnostico
    template_name = "inv/diagnostico_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class DiagnosticoNew(LoginRequiredMixin, generic.CreateView):
    model = Diagnostico
    template_name = "inv/diagnostico_form.html"
    context_object_name = "obj"
    form_class = DiagnosticoForm
    success_url = reverse_lazy("inv:diagnostico_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class DiagnosticoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Diagnostico
    template_name = "inv/diagnostico_form.html"
    context_object_name = "obj"
    form_class = DiagnosticoForm
    success_url = reverse_lazy("inv:diagnostico_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def diagnostico_inactivar(request, id):
    diagnostico = Diagnostico.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not diagnostico:
        return redirect("inv:diagnostico_list")

    if request.method=='GET':
        contexto={'obj':diagnostico}

    if request.method=='POST':
        diagnostico.estado=False
        diagnostico.save()
        return redirect("inv:diagnostico_list")

    return render(request, template_name, contexto)


class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/catalogos_del.html"

    if not producto:
        return redirect("inv:producto_list")

    if request.method=='GET':
        contexto={'obj':producto}

    if request.method=='POST':
        producto.estado=False
        producto.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)


class RecetasView(LoginRequiredMixin, generic.ListView):
    model = RecetasEnc
    template_name = "inv/recetas_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


def recetas(request, receta_id=None):
    template_name = "inv/recetas.html"
    prod = Producto.objects.filter(estado=True)
    medi = Medico.objects.filter(estado=True)
    form_recetas = {}
    contexto = {}

    if request.method == 'GET':
        form_recetas = RecetasEncForm()
        enc = RecetasEnc.objects.filter(pk=receta_id).first()

        if enc:
            det = RecetasDet.objects.filter(receta=enc)
            fecha_receta = datetime.date.isoformat(enc.fecha_receta)
            e = {
                'fecha_receta': fecha_receta,
                'paciente': enc.paciente,
                'medico': enc.medico,
                'observacion': enc.observacion,
                'no_receta': enc.no_receta
            }
            form_recetas = RecetasEncForm(e)
        else:
            det = None

        contexto = {'productos': prod, 'medicos': medi, 'encabezado': enc, 'detalle': det, 'form_enc': form_recetas}

    if request.method == 'POST':
        fecha_receta = request.POST.get("fecha_receta")
        observacion = request.POST.get("observacion")
        no_receta = request.POST.get("no_receta")
        paciente = request.POST.get("paciente")
        medico = request.POST.get("medico")

        if not receta_id:
            paciente = Paciente.objects.get(pk=paciente)
            medico = Medico.objects.get(pk=medico)

            enc = RecetasEnc(
                fecha_receta=fecha_receta,
                observacion=observacion,
                no_receta=no_receta,
                paciente=paciente,
                medico=medico,
                uc=request.user
            )

            if enc:
                enc.save()
                receta_id = enc.id
        else:
            enc = RecetasEnc.objects.filter(pk=receta_id).first()
            if enc:
                enc.fecha_receta = fecha_receta
                enc.observacion = observacion
                enc.no_receta = no_receta
                enc.um = request.user.id
                enc.save()

        if not receta_id:
            return redirect("inv:recetas_list")

        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")

        prod = Producto.objects.get(pk=producto)

        det = RecetasDet(
            receta=enc,
            producto=prod,
            cantidad=cantidad,
            uc=request.user
        )

        if det:
            det.save()

            enc.save()

        return redirect("inv:recetas_edit", receta_id=receta_id)

    return render(request, template_name, contexto)


class RecetaDetDelete(LoginRequiredMixin, generic.DeleteView):
    model = RecetasDet
    template_name = "inv/compras_det_del.html"
    context_object_name = 'obj'

    def get_success_url(self):
        receta_id = self.kwargs['receta_id']
        return reverse_lazy('inv:recetas_edit', kwargs={'receta_id': receta_id})