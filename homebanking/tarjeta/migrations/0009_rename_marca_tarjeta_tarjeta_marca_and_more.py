# Generated by Django 4.1 on 2022-09-02 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tarjeta", "0008_alter_tarjeta_marca_alter_tarjeta_tipo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tarjeta",
            old_name="marca",
            new_name="tarjeta_marca",
        ),
        migrations.RenameField(
            model_name="tarjeta",
            old_name="tipo",
            new_name="tarjeta_tipo",
        ),
    ]