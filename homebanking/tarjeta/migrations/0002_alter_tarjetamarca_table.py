# Generated by Django 4.1 on 2022-08-31 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tarjeta", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="tarjetamarca",
            table="marcatarjeta",
        ),
    ]
