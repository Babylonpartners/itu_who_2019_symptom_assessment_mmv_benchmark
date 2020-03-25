# Generated by Django 3.0.4 on 2020-03-25 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AIImplementation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('base_url', models.URLField()),
                ('health_endpoint', models.CharField(max_length=30)),
                ('solution_endpoint', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
