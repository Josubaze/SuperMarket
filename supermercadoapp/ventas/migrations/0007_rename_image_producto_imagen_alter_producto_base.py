# Generated by Django 4.2.1 on 2023-06-26 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_rename_cost_producto_base'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='image',
            new_name='imagen',
        ),
        migrations.AlterField(
            model_name='producto',
            name='base',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True),
        ),
    ]
