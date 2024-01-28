# models.py
from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Persona(models.Model):
    cedula = models.CharField(
        max_length=10,
    )
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    def __str__(self):
      return f"{self.cedula},{self.apellido}, {self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(
        max_length=100,
    )
    presentacion = models.CharField(max_length=80)
    costo = models.FloatField(default=0)
    pvp = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nombre}"

    def save(self, *args, **kwargs):
        super(Producto, self).save(*args, **kwargs)

class Proveedores(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.persona)

    def save(self, *args, **kwargs):
        super(Proveedores, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Proveedores'

class Medico(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.persona)

    def save(self, *args, **kwargs):
        super(Medico, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Medicos'


class Patologia(models.Model):
    patologia = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return '{}'.format(self.patologia)

    def save(self, *args, **kwargs):
        self.patologia = self.patologia.upper()
        super(Patologia, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Patologias"


class Paciente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    patologia = models.ForeignKey(Patologia, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.persona.cedula} - {self.persona.apellido} {self.persona.nombre} - {self.patologia}"

    def save(self, *args, **kwargs):
        # Lógica personalizada al guardar el modelo Paciente
        # Puedes agregar tu lógica aquí
        super(Paciente, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Pacientes"
        unique_together = ('persona', 'patologia')


class Dosificacion(models.Model):
    cantidad = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.cantidad)

    def save(self, *args, **kwargs):
        # Lógica personalizada al guardar el modelo Dosificacion
        # Puedes agregar tu lógica aquí
        super(Dosificacion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Dosificaciones"

class Diagnostico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.paciente)

    def save(self, *args, **kwargs):
        self.observacion = self.observacion.upper()
        self.diagnostico = self.diagnostico.upper()
        super(Diagnostico, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Diagnosticos'
        unique_together = ('paciente', 'observacion')

class RecetasEnc(models.Model):
    fecha_receta = models.DateField(null=True, blank=True)
    observacion = models.TextField(blank=True, null=True)
    no_receta = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self, *args, **kwargs):
        self.observacion = self.observacion.upper()
        super(RecetasEnc, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Encabezado Recetas"
        verbose_name = "Encabezado Receta"

class RecetasDet(models.Model):
    receta = models.ForeignKey(RecetasEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self, *args, **kwargs):
        super(RecetasDet, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Detalles Recetas"
        verbose_name = "Detalle Receta"

class Api(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self):
        super(Api, self).save()
