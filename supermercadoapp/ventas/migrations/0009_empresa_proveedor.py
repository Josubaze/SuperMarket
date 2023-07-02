# Generated by Django 4.2.1 on 2023-07-02 01:23

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_egreso_productosegreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('domicilio', models.CharField(max_length=255, null=True)),
                ('telefono', models.CharField(max_length=255, null=True)),
                ('imagen', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[100, 100], upload_to='empresa')),
                ('moneda', models.CharField(default='$', max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresa',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='proveedor')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'proveedores',
            },
        ),
    ]
