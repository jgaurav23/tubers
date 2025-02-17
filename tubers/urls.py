""" tubers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings


admin.site.site_header = "HireTube Admin Login"
admin.site.index_title = "Welcome HireTube Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webpages.urls')),
    path('youtubers/',include('youtubers.urls')),
    path('hiretubers/',include('hiretubers.urls')),
    path('accounts/',include('accounts.urls')),
    path('formcontact/',include('formcontact.urls')),
    path('socialaccounts/', include('allauth.urls')),
     path('oauth/', include('social_django.urls', namespace='social'))
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
