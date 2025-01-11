from django.contrib import admin
from .models import Slider,Team,WebsiteInfo
from django.utils.html import format_html

# WE OVERWRITE THE ADMIN PANEL
class TeamAdmin(admin.ModelAdmin):
        
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url)) 

#This Method manage the table data in accending order "created_date is table value"
#Second Way Do It
    def get_queryset(self,request):
        queryset = super(TeamAdmin,self).get_queryset(request)
        queryset = queryset.order_by('created_date')
        return queryset
        
    list_display = ('id','myphoto','first_name','role','created_date')
    list_display_links = ('first_name','id')
    search_fields = ('first_name','role','last_name')

class SliderAdmin(admin.ModelAdmin):
    def slider_photo(self,object):
        return format_html('<img src="{}" width="120" height="40" />'.format(object.photo.url))

    list_display = ('slider_photo','headline','button_text')

class WebsiteInfoAdmin(admin.ModelAdmin):
    list_display = ('email','phone','address')

   

admin.site.register(Slider,SliderAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(WebsiteInfo,WebsiteInfoAdmin)