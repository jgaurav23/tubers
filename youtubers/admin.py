from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))
# 2nd way
# method To order the table data in accending 
#     def get_queryset(self,request):
#         queryset = super(TeamAdmin,self).get_queryset(request)
#         queryset = queryset.order_by('created_date')
#         return queryset

    list_display = ('id','name','subs_count','is_featured','myphoto')
    search_fields = ('name','camera_type','category')
    list_filter = ('city','camera_type')
    list_display_links = ('name','id',)
    list_editable = ('is_featured',)
    

admin.site.register(Youtuber,YtAdmin)