# Generated by Django 4.1 on 2022-08-31 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cuenta", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movimiento",
            fields=[
                (
                    "movimiento_transaccion_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "movimiento_tipo_operacion",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("movimiento_monto", models.IntegerField()),
                ("movimiento_cambiado", models.CharField(max_length=255)),
                (
                    "movimiento_cuenta",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cuenta.cuenta",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movimiento",
                "verbose_name_plural": "Movimientos",
                "db_table": "movimientos",
            },
        ),
    ]