from django.shortcuts import render , redirect
from .forms import RegistrationForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate  
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import get_user_model

User = get_user_model()  # ⚠️ yahan parentheses bhool gaye

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Form invalid hai, errors dikhane ke liye same page render karo
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        user_input = request.POST.get('username_email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(email = user_input).first()
        if user_obj:
                username = user_obj.username
        else:
                username = user_input
      

        user = authenticate(username = username , password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            redirect('register')
    return render(request , 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('blog')