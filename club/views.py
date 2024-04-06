from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Incorrect email or password!")
            return redirect('/login')

    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Succesfully log out")
    return redirect('/')

