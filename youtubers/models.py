from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField     

# Create your models here.
class Youtuber(models.Model):

    crew_choises = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choises = (
        ('canon','Canon'),
        ('nikon','Nikon'),
        ('sony','Sony'),
        ('red','Red'),
        ('fuji','Fuji'),
        ('panasonic','Panasonic'),
        ('Gopro','Gopro'),
        ('other','Other')
    )

    category_choises = (
        ('coder','Coder'),
        ('tech','Tech'),
        ('vlogs','Vlogs'),
        ('comedy','Comedy'),
        ('gamer','Gamer'),
        ('film_making','Film_Making'),
        ('food','food'),
        ('other','Other')
    )

    name = models.CharField( max_length=250)
    price = models.IntegerField()
    photo = models.ImageField( upload_to='media/ytubers/%Y/%m/')
    video_url = models.CharField( max_length=250)
    description = RichTextField()
    city = models.CharField( max_length=250)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choises, max_length=250,default=None)
    camera_type = models.CharField(choices=camera_choises, max_length=250)
    subs_count = models.CharField( max_length=250)
    category = models.CharField(choices=category_choises ,max_length=250)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField( default=datetime.now  , blank=True)  

    def __str__(self):
        return self.name

# 1st way
# method To order the table data in accending
    class Meta:
        ordering = ['id']


    

     