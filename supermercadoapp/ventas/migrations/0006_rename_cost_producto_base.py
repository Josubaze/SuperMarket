# Generated by Django 4.2.1 on 2023-06-25 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_producto_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cost',
            new_name='base',
        ),
    ]
