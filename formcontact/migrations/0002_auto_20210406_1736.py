# Generated by Django 3.1.7 on 2021-04-06 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formcontact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcontact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
