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
from project_django.middleware import inject_toko
from .models import User, Profile
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt    
import json

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
        is_seller = False
        if (User.objects.filter(username=username) or User.objects.filter(email=email)):
            messages.info(request, "Username or email already taken!")
        elif (password == repeat_password):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            if (request.POST.get("seller_choice") == "yes"):
                is_seller = True
            profile = Profile.objects.create(user=user, name=username, email=email, is_seller=is_seller)
            profile.save()
            print(profile.is_seller)
            print(profile.user)
            print(user.profile)
            return redirect("landing:login")
        else:
            messages.info(request, "Password and repeat password is different!")
    return render(request, "register.html")

@csrf_exempt
def register_flutter(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    confirm_pass = data['confirm_password']
    print(username)
    print(password)
    print(confirm_pass)

    if (password == confirm_pass):
        try:
        #Cek jika username atau email sudah terdaftar
            user = User.objects.get(username=username)
            print(user)
            return JsonResponse({'status':'register gagal'})
        except (User.DoesNotExist):
        #Jika username belum terdaftar
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'status':'register berhasil', 'username':username, 'password':password})

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

@csrf_exempt
def login_flutter(request):
    print("MASUK DISINI")
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    if request.method == 'POST':
        user = authenticate(username=username, password=password)
        temp = User.objects.get(username=username)
        print(temp.id)
        print("AUTENTHICATE")
        print(username)
        print(password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": True,
                "username": request.user.username,
                "id": temp.id,
                "message": "Successfully Logged In!"
            }, status=200)

        else:
             return JsonResponse({
                "status": False,
                "message": "Failed to Login!"
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, your username/password may be wrong."
        }, status=401)

@csrf_exempt
def logout_flutter(request):
    logout(request)
    return JsonResponse({
            "status": True,
            "message": "Berhasil"
        }, status=200)


# Handling logout function
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('landing:login'))
    response.delete_cookie('last_login')
    return response