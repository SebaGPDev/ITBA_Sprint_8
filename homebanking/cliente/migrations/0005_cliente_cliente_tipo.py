# Generated by Django 4.1 on 2022-08-30 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("TipoCliente", "0001_initial"),
        ("cliente", "0004_cliente_cliente_direccion"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="cliente_tipo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="TipoCliente.tipocliente",
                verbose_name="Tipo cliente",
            ),
        ),
    ]
