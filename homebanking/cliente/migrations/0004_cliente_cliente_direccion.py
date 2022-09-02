# Generated by Django 4.1 on 2022-08-30 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("direccion", "0002_alter_direccion_options"),
        ("cliente", "0003_remove_cliente_cliente_direccion"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="cliente_direccion",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="direccion.direccion",
                verbose_name="Direccion",
            ),
        ),
    ]