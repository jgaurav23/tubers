# Generated by Django 4.2.2 on 2023-08-03 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0004_alter_hiretuber_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
