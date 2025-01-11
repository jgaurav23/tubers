from django.shortcuts import render,redirect
from .models import FormContact
from django.contrib import messages
# Create your views here.
def formcontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        companyname = request.POST.get('company_name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        formcontact = FormContact(name=name,phone=phone,email=email,companyname=companyname,subject=subject,message=message)
        formcontact.save()
        messages.success(request,'We Contact You Soon')
        return redirect('contact')