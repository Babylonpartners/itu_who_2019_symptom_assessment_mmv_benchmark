# Generated by Django 3.0.4 on 2020-04-20 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="case", name="name",),
    ]
