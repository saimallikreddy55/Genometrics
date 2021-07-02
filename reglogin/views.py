from django.contrib import messages
from .models import Register
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name,password=password)
        if  user is not None:
            auth.login(request,user)
            messages.info(request,'You Have Successfully LogedIn')
            return redirect('/')
        else:
            messages.info(request,'Invalid Details')
            return redirect('login')
    else:
        return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['re_password']

        if password1==password2:
            if Register.objects.filter(name=name).exists():
                messages.info(request,'Username Taken') 
                return redirect('register')
            elif Register.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                register = Register.objects.create(name=name,password1=password1,email=email)
                register.save();
                user = User.objects.create_user(username=name,password=password1,email=email)
                user.save();
                messages.info(request,'You Have Registerd')
                return redirect('login')
           
        else:
            messages.info(request,' Enterd Passwords doesnot Match...')
            return redirect('register')
        

    else:    
        return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

