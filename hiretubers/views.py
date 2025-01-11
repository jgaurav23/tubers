from django.shortcuts import render,redirect
from .models import Hiretuber


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        tuber_id = request.POST.get("tuber_id")
        tuber_name = request.POST.get("tuber_name")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        state = request.POST.get("state")
        message = request.POST.get("message")
        user_id = request.POST.get("user_id")
        event_datetime = request.POST.get("event_datetime")

        hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,
                city=city,phone=phone,email=email,state=state,message=message,user_id=user_id, event_date_time=event_datetime)
        hiretuber.save()
        return redirect('youtubers')