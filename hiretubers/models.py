from django.db import models
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):
    APPROVED = 'APPROVED'
    PENDING = 'PENDING'
    DISAPPROVED = 'DISAPPROVED'
    ENDED = 'ENDED'

    EVENT_STATUS = (
        (APPROVED, 'Approved Event'),
        (PENDING, 'Pending Event'),
        (DISAPPROVED, 'Disapproved Event'),
        (ENDED, 'Event Ended Successfully'),
        )
    
    first_name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField( max_length=250)
    city = models.CharField( max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    state = models.CharField( max_length=250)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    event_date_time = models.DateTimeField(null=True)
    created_date = models.DateField(blank=True,default=datetime.now)
    approved_amount = models.IntegerField(null=True)
    event_status = models.CharField(max_length=100, choices=EVENT_STATUS, default=PENDING, db_index=True) 
    #db_index=True used for "Improved Query Performance, Efficient Sorting, Faster Lookup Operations, Join Optimization"


    

    def __str__(self):
        return self.email
    