# Generated by Django 5.0.1 on 2024-01-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_dosificacion_patologia_producto_medico_paciente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]