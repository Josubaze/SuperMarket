# Generated by Django 4.2.1 on 2023-07-07 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0013_producto_iva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='iva',
        ),
    ]
