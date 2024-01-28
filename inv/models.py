from django.db import models

#Para Signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo

# Create your models here.
class Persona(ClaseModelo):
    cedula = models.CharField(
        max_length=10,
        unique=True
    )
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    edad = models.IntegerField(default=0)
    genero = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.cedula} - {self.apellido} {self.nombre}"

    def save(self):
        self.apellido = self.apellido.upper()
        self.nombre = self.nombre.upper()
        super(Persona, self).save()

    class Meta:
        verbose_name_plural = "Personas"


class Proveedores(ClaseModelo):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.persona)

    def save(self):
        super(Proveedores, self).save()

    class Meta:
        verbose_name_plural = 'Proveedores'

class Medico(ClaseModelo):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.persona)

    def save(self):
        super(Medico, self).save()

    class Meta:
        verbose_name_plural = 'Medicos'

class Patologia(ClaseModelo):
    patologia = models.CharField(
        max_length=200,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.patologia)

    def save(self):
        self.patologia = self.patologia.upper()
        super(Patologia, self).save()

    class Meta:
        verbose_name_plural = "Patologias"


class Paciente(ClaseModelo):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    patologia = models.ForeignKey(Patologia, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.persona.cedula} - {self.persona.apellido} {self.persona.nombre} - {self.patologia}"

    def save(self):
        super(Paciente, self).save()

    class Meta:
        verbose_name_plural = "Pacientes"
        unique_together = ('persona','patologia')


class Dosificacion(ClaseModelo):
    cantidad = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.cantidad)

    def save(self):
        super(Dosificacion, self).save()

    class Meta:
        verbose_name_plural = "Dosificaciones"


class Diagnostico(ClaseModelo):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.paciente)

    def save(self):
        self.observacion = self.observacion.upper()
        self.diagnostico = self.diagnostico.upper()
        super(Diagnostico, self).save()

    class Meta:
        verbose_name_plural = 'Diagnosticos'
        unique_together = ('paciente', 'observacion')


class Producto(ClaseModelo):
    nombre = models.CharField(
        max_length=100,
        unique=False
    )
    presentacion = models.CharField(max_length=80)
    fecha_elaboracion = models.DateField(null=True, blank=True)
    fecha_caducidad = models.DateField(null=True, blank=True)
    existencia = models.IntegerField(default=0)
    costo = models.FloatField(default=0)
    pvp = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nombre}"

    def save(self):
        self.nombre = self.nombre.upper()
        self.presentacion = self.presentacion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "Productos"


class RecetasEnc(ClaseModelo):
    fecha_receta=models.DateField(null=True, blank=True)
    observacion=models.TextField(blank=True, null=True)
    no_receta=models.CharField(max_length=100)

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        super(RecetasEnc, self).save()

    class Meta:
        verbose_name_plural = "Encabezado Recetas"
        verbose_name = "Encabezado Receta"


class RecetasDet(ClaseModelo):
    receta=models.ForeignKey(RecetasEnc, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        super(RecetasDet, self).save()

    class Mega:
        verbose_name_plural = "Detalles Recetas"
        verbose_name = "Detalle Receta"


@receiver(post_delete, sender=RecetasDet)
def detalle_receta_borrar(sender, instance, **kwargs):
    id_producto = instance.producto.id
    id_receta = instance.receta.id

    enc = RecetasEnc.objects.filter(pk=id_receta).first()
    if enc:
        enc.save()

    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=RecetasDet)
def detalle_compra_guardar(sender, instance, **kwargs):
    id_producto = instance.producto.id

    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()
