from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from youtubers.models import Youtuber
from hiretubers.models import Hiretuber

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You Are Loged In')
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'username already exists')
                print('username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'email already exists')
                print('email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,
                                        email=email,password=password)
                user.save()
                messages.success(request,'Account created SuccessFully')
                print('Account created SuccessFully')
                return redirect('login')
        else:
            messages.warning(request,'Password Do Not Match')
            print('Password Do Not Match')  
            return redirect('register')

    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    user_id = request.user.id
    events = Hiretuber.objects.filter(user_id=user_id)
    data = {
        'events':events,
    }
    return render(request, 'accounts/dashboard.html', data)

@login_required(login_url='login')
def event_detail(request, id):
    event_detail = get_object_or_404(Hiretuber, pk=id)
    data = {
        'event_detail':event_detail,
    }
    return render(request, 'webpages/services.html', data)