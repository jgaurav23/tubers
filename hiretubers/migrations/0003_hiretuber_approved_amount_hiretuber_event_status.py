# Generated by Django 4.2.2 on 2023-06-26 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0002_hiretuber_event_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiretuber',
            name='approved_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hiretuber',
            name='event_status',
            field=models.CharField(choices=[('APPROVED', 'Approved Event'), ('PENDING', 'Pending Event'), ('DISAPPROVED', 'Disapproved Event'), ('ENDED', 'Event Ended Successfully')], db_index=True, default='PENDING', max_length=100),
        ),
    ]