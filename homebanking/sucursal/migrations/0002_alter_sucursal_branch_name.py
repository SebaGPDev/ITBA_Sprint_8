# Generated by Django 4.1 on 2022-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sucursal", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sucursal",
            name="branch_name",
            field=models.CharField(max_length=255),
        ),
    ]
