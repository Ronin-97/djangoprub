# Generated by Django 4.2.1 on 2023-07-28 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existencia',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='RecetasEnc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_receta', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('no_receta', models.CharField(max_length=100)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.paciente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Receta',
                'verbose_name_plural': 'Encabezado Recetas',
            },
        ),
        migrations.CreateModel(
            name='RecetasDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.BigIntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.producto')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.recetasenc')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]