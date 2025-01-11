from django.urls import path
from . import views 

urlpatterns = [
    path('formcontact',views.formcontact,name='formcontact')
]