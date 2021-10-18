from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from  .models import extendeduser
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        #  check if a user exist
        # with the username and password
    
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(showuserdata)
            # return HttpResponse("Logged In!")
        else:
            return render(request, 'home.html', {'error': "Invalid Login credentials."} )
    else:
        return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        # to create a User
        if request.POST['password'] == request.POST['passwordagain']:
            # both the passwords matched
            # now check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password= request.POST['password'])
                add = request.POST['address']
                ema = request.POST['email']
                newextendeduser = extendeduser(address=add, email=ema, user= user )
                newextendeduser.save()
                # this line can login the user rightnow
                auth.login(request, user)
                return redirect(home)
                # return HttpResponse("Signned Up!")
        else:
            return render(request, 'register.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect(home)

@login_required(login_url='/accounts/login')
def showuserdata(request):
    datas = extendeduser.objects.filter(user = request.user)
    return render(request, "showdata.html", {'data': datas} )