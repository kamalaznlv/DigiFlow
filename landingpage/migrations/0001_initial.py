# Generated by Django 4.2.4 on 2024-03-07 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_submitted', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
