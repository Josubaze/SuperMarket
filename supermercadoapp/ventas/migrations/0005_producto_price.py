# Generated by Django 4.2.1 on 2023-06-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_alter_producto_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True),
        ),
    ]
