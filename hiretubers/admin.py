from django.contrib import admin
from .models import Hiretuber
# Register your models here.

@admin.register(Hiretuber)
class HiretuberAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','tuber_name')

    
