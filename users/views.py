from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.forms import UserForm, UserProfileForm
from users.models import Userprofile


def home(request):
    return render(request, 'users/home.html')


def user_logout(request):
    messages.success(request, "You logged out successfully")
    logout(request)
    return redirect('home')


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, 'Register Successfull')
            return redirect('home')

        else:
            messages.error(request, 'Please correct the error below')

    context = {

        'form_user' : form_user,
        'form_profile' : form_profile,
    }

    return render(request, 'users/register.html', context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()

        if user:
            login(request, user)
            messages.success(request, 'Login is successfull')
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    context = {

        'form' : form
    }

    return render(request, 'users/user_login.html', context)

def user_profile(request):
    user = request.user
    profile = Userprofile.objects.get(user=user)
    form_user = UserForm(instance=profile)
    form_profile = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form_user = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form_user.is_valid():
            messages.success(request, "Your profile has been updated!!")
            form_user.save()
            return redirect('home')

    context = {
        
        'form_profile' : form_profile,
        'form_user' : form_user,
        'user' :user,
        'profile' : profile,
    }

    return render (request, 'users/user_profile.html', context)



