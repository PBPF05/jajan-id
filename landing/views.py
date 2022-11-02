from django.shortcuts import  render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib import messages
from django.shortcuts import redirect
from .models import User

# Create your views here.

def show_landing(request):
    context = {}
    return render(request, "landing.html", context)

def register(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        if (User.objects.filter(username=username) or User.objects.filter(email=email)):
            messages.info(request, "Username or email already taken!")
        elif (password == repeat_password):
            user = User.objects.create_user(username=username, email=email, password=password)
            if (request.POST.get("seller_choice") == "yes"):
                user.is_seller = True
                seller_profile = DoctorProfile.objects.create(profile = user_profile)
                seller_profile.save()
            user.save()
            user_profile.save()
            return redirect("landing:login")
        else:
            messages.info(request, "Password and repeat password is different!")
    return render(request, "register.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("landing:landing")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    
    return render(request, 'login.html', context)

# Handling logout function
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('landing:login'))
    response.delete_cookie('last_login')
    return response