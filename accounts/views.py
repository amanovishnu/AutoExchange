from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, 'Passwords are not Same')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email
                )
                user.save()
                auth.login(request, user)
                messages.success(request, 'You are now Logged In')
                return redirect('dashboard')

    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have been logged out Successfully')
        return redirect('home')
    return redirect('dashboard')


@login_required()
def dashboard(request):
    user_id = request.user.id
    enquiries = Contact.objects.order_by('-created_date').filter(user_id = user_id)
    data = {
        'enquiries':enquiries
    }
    return render(request, 'accounts/dashboard.html', context=data)
