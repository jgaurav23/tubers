# Generated by Django 4.2.2 on 2023-08-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_websiteinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='event_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
