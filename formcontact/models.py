from django.db import models
from datetime import datetime
# Create your models here.
class FormContact(models.Model):
    name = models.CharField( max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    companyname = models.CharField( max_length=100)
    subject = models.CharField( max_length=100)
    message = models.CharField( max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name