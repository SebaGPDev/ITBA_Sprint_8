# Generated by Django 4.1 on 2022-09-02 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cuenta", "0002_remove_cuenta_cuenta_tipo_cuenta_tipo_cuenta"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TipoCuenta",
        ),
    ]
