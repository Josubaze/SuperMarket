# Generated by Django 4.2.2 on 2023-06-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_alter_cliente_options_alter_producto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
