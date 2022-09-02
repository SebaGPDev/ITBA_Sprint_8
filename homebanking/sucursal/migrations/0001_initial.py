# Generated by Django 4.1 on 2022-08-31 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("direccion", "0002_alter_direccion_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sucursal",
            fields=[
                ("branch_id", models.AutoField(primary_key=True, serialize=False)),
                ("branch_number", models.BinaryField()),
                ("branch_name", models.TextField()),
                (
                    "branch_address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="direccion.direccion",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sucursal",
                "verbose_name_plural": "Sucursales",
                "db_table": "sucursal",
                "ordering": ["-branch_id"],
            },
        ),
    ]