# Generated by Django 4.1 on 2022-08-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TipoCliente",
            fields=[
                (
                    "tipo_cliente_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("tipo_nombre", models.CharField(max_length=255, unique=True)),
                ("tipo_tarjeta_debito", models.CharField(max_length=255)),
                ("tipo_tarjeta_cretido", models.CharField(max_length=255)),
                ("tipo_cuenta_corriente", models.CharField(max_length=255)),
                ("tipo_chequera", models.IntegerField()),
                (
                    "tipo_cuenta_dolar",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "tipo_cuenta_peso",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "retiro_diario",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "comision_transferencia",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("recepcion", models.CharField(blank=True, max_length=255, null=True)),
                ("monto_pre_aprobado", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Tipo cliente",
                "verbose_name_plural": "Tipo clientes",
                "db_table": "tipo_cliente",
                "ordering": ["-tipo_cliente_id"],
            },
        ),
    ]
