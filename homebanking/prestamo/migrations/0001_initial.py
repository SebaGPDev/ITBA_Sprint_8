# Generated by Django 4.1 on 2022-08-31 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cliente", "0006_cliente_branch"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoPrestamo",
            fields=[
                ("type_id", models.AutoField(primary_key=True, serialize=False)),
                ("loan_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Tipo prestamo",
                "verbose_name_plural": "Tipo prestamos",
                "db_table": "tipoprestamo",
            },
        ),
        migrations.CreateModel(
            name="Prestamo",
            fields=[
                ("loan_id", models.AutoField(primary_key=True, serialize=False)),
                ("loan_date", models.DateField()),
                ("loan_total", models.IntegerField()),
                ("loan_preapproval", models.IntegerField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.cliente",
                    ),
                ),
                (
                    "loan_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prestamo.tipoprestamo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Prestamo",
                "verbose_name_plural": "Prestamos",
                "db_table": "prestamo",
            },
        ),
    ]