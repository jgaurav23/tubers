# Generated by Django 4.2.2 on 2023-08-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0003_hiretuber_approved_amount_hiretuber_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
