from django.shortcuts import render
from .models import Slider,Team,WebsiteInfo
from youtubers.models import Youtuber
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    team_member = Team.objects.all()

    featured_youtuber = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-created_date')

    data = {
        'sliders':sliders,
        'team_members':team_member,
        'featured_youtuber':featured_youtuber,
        'all_tubers':all_tubers,
    }
    return render(request,'webpages/home.html',data)

def about(request):
    team_member = Team.objects.all()
    data = {
        'team_member':team_member
    }
    return render(request,'webpages/about.html',data)

def services(request):
     return render(request,'webpages/services.html')

def contact(request):
    websiteinfo = WebsiteInfo.objects.all()
    data = {
        'websiteinfo':websiteinfo
    }
    return render(request,'webpages/contact.html',data)

def websiteinfo(request):
    websiteinfo = WebsiteInfo.objects.all()
    data = {
        'websiteinfo':websiteinfo
    }
    return render(request,'base.html',data)