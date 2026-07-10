from django.shortcuts import render
from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth import update_session_auth_hash
import requests

def register(request):
    if request.method == 'POST':
        print(request.POST)
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(password) < 8:
            messages.error(request,"Password must be at least 8 characters long!!!")
            return redirect('register')
        if not any(c.isupper() for c in password):
            messages.error(request,"Password must contain at least one uppercase letter!!!")
            return redirect('register')
        if not any(c.islower() for c in password):
            messages.error(request,"Password must contain at least one lowercase letter!!!")
            return redirect('register')
        if not any(c.isdigit() for c in password):
            messages.error(request,"Password must contain at least one digit!!!")
            return redirect('register')
        if not any(c in "!@#$%^&*()-+" for c in password):
            messages.error(request,"Password must contain at least one special character!!!")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!!!")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=fname,
            last_name=lname,
        )

        Profile.objects.create(user=user)

        messages.success(request, "Account created successfully!!!")
        return redirect('login_')
    return render(request, 'register.html')

def login_(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        requests.post('')
        
    return render(request,'login_.html')

def logout_(request):
    logout(request)
    messages.success(request,'logout successfull!!!!!!!')
    return redirect('login_')

def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request,'profile.html', {'profile': profile})

def reset(request):
    if request.method=='POST':
        if 'old_pass' in request.POST:
            old_pass=request.POST['old_pass']
            user=request.user
            u=authenticate(username=user,password=old_pass)
            print(u)
            if u:
                return render(request,'reset.html',{'new':True})
            else:
                messages.error(request,'enterd old pass is wrong!!!!!!')
                return redirect('reset')
        
    if 'new_pass' in request.POST:
        new_pass=request.POST['new_pass']
        user=User.objects.get(username=request.user)
        user.set_password(new_pass)
        update_session_auth_hash(request,user)
        user.save()
        messages.success(request,'passward updated successfully!!!')
        return redirect('profile')
    return render(request,'reset.html')

def forget(request):
    if request.method=='POST':
        if 'username' in request.POST:
            username=request.POST['username']
            try:
                user=User.objects.get(username=username)
                request.session['fp_user']=user.username
                return render(request,'forget.html',{'new':True})
            except:
                messages.error(request,'user doest exist!!!')
                return redirect(forget)
            
    if 'fnew_pass' in request.POST:
        fnew_pass=request.POST['fnew_pass']
        cfnew_pass=request.POST['cfnew_pass']
        username=request.session.get('fp_user')
        if not username:
            messages.error(request,'session got expierd...!!')
            return redirect('forget')
        
        u=User.objects.get(username=username)
        if u.check_password(fnew_pass):
            messages.error(request,'New password cannot be same as old password.!!!')
            return redirect('forget')
        
        if fnew_pass != cfnew_pass:
            messages.error(request,'Passwords do not match.')
            return redirect('forget')

        u.set_password(fnew_pass)
        u.save()
        del request.session['fp_user']
        messages.success(request,'password changend successfully!!!')
        return redirect('login_')
    return render(request,'forget.html')

def update(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.save()

        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()

        messages.success(request, 'Profile updated!!!!')
        return redirect('profile')

    return render(request, 'update.html', {
        'data': user,
        'profile': profile
    })
