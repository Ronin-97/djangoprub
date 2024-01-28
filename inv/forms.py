from django import forms

from .models import Persona, Proveedores, Medico, Patologia, Paciente, Dosificacion, Diagnostico, Producto, \
                    RecetasEnc

class PersonaForm(forms.ModelForm):
    fecha_nacimiento = forms.DateInput()
    correo = forms.EmailField(max_length=254)

    class Meta:
        model = Persona
        fields = ['cedula', 'apellido', 'nombre', 'edad', 'estado', \
                  'genero', 'fecha_nacimiento', 'correo',
                  'telefono', 'direccion']
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_nacimiento'].widget.attrs['readonly'] = True


class ProveedoresForm(forms.ModelForm):
    persona = forms.ModelChoiceField(
        queryset=Persona.objects.filter(estado=True)
        .order_by('cedula')
    )
    class Meta:
        model = Proveedores
        fields = ['persona', 'estado']
        labels = {'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['persona'].empty_label = "Seleccione Persona"
        self.fields['persona'].queryset = Persona.objects.all()
        self.fields['persona'].label_from_instance = lambda obj: f"{obj.cedula} - {obj.apellido} {obj.nombre}"


class MedicoForm(forms.ModelForm):
    persona = forms.ModelChoiceField(
        queryset=Persona.objects.filter(estado=True)
        .order_by('cedula')
    )
    class Meta:
        model = Medico
        fields = ['persona', 'estado']
        labels = {'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['persona'].empty_label = "Seleccione Persona"
        self.fields['persona'].queryset = Persona.objects.all()
        self.fields['persona'].label_from_instance = lambda obj: f"{obj.cedula} - {obj.apellido} {obj.nombre}"


class PatologiaForm(forms.ModelForm):
    class Meta:
        model = Patologia
        fields = ['patologia', 'estado']
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class PacienteForm(forms.ModelForm):
    persona = forms.ModelChoiceField(
        queryset=Persona.objects.filter(estado=True)
        .order_by('cedula')
    )
    patologia = forms.ModelChoiceField(
        queryset=Patologia.objects.filter(estado=True)
        .order_by('patologia')
    )
    class Meta:
        model = Paciente
        fields = ['persona', 'patologia', 'estado']
        labels = {'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['persona'].empty_label = "Seleccione Persona"
        self.fields['persona'].queryset = Persona.objects.all()
        self.fields['persona'].label_from_instance = lambda obj: f"{obj.cedula} - {obj.apellido} {obj.nombre}"
        self.fields['patologia'].empty_label = "Seleccione Patologia"


class DosificacionForm(forms.ModelForm):
    class Meta:
        model = Dosificacion
        fields = ['cantidad', 'estado']
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class DiagnosticoForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.filter(estado=True)
        .order_by('id')
    )
    class Meta:
        model = Diagnostico
        fields = ['paciente', 'observacion', 'diagnostico', 'estado']
        labels = {'estado':"Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['paciente'].empty_label = "Seleccione Paciente"
        self.fields['paciente'].queryset = Paciente.objects.all()
        self.fields['paciente'].label_from_instance = lambda obj: f"{obj.persona} - {obj.patologia}"


class ProductoForm(forms.ModelForm):
    fecha_elaboracion = forms.DateInput()
    fecha_caducidad = forms.DateInput()

    class Meta:
        model = Producto
        fields = ['nombre', 'presentacion', 'estado', \
                  'fecha_elaboracion', 'fecha_caducidad', 'existencia', \
                  'costo', 'pvp']
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_elaboracion'].widget.attrs['readonly'] = True
        self.fields['fecha_caducidad'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True


class RecetasEncForm(forms.ModelForm):
    fecha_receta = forms.DateInput()

    class Meta:
        model = RecetasEnc
        fields = ['paciente', 'medico', 'fecha_receta',
                  'observacion', 'no_receta']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_receta'].widget.attrs['readonly'] = True