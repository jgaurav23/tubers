from django.db import models

# Create your models here.
class Slider(models.Model):
    headline     =   models.CharField( max_length=250)
    subtital     =   models.CharField( max_length=250)
    button_text  =   models.CharField( max_length=250)
    photo        =   models.ImageField( upload_to='media/slider/%Y/') 
    event_link   =   models.CharField( max_length=100, blank=True) 
    created_date =   models.DateTimeField( auto_now_add=True)  
     
    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name   =  models.CharField( max_length=100) 
    last_name    =  models.CharField( max_length=100) 
    role         =  models.CharField( max_length=100)
    fb_link      =  models.CharField( max_length=100, blank=True)  
    insta_link   =  models.CharField( max_length=100, blank=True)
    photo        =  models.ImageField( upload_to="media/team/%Y/%m/%d/")
    created_date =  models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.role  


class WebsiteInfo(models.Model):
    email       = models.EmailField(max_length=254)
    phone       = models.IntegerField()
    address     = models.CharField(max_length=50)
    fb_link     = models.CharField(max_length=150, blank=True)
    insta_link  = models.CharField(max_length=150, blank=True)
    twt_link    = models.CharField(max_length=150, blank=True)
    yt_link     = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.address 