# Generated by Django 4.1.7 on 2023-03-24 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Elevation",
        ),
        migrations.DeleteModel(
            name="Zipcode",
        ),
    ]
