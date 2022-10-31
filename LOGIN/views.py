import email
from email import message
from gzip import FNAME
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from httplib2 import Authentication

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        FName = request.POST['fname']
        LName = request.POST['lname']
        Email = request.POST['email']
        Pass1 = request.POST['pass1']
        Pass2 = request.POST['pass2']

        myuser = User.objects.create(username = username, Email = Email, Pass1 = Pass1)
        myuser.first_name = FName
        myuser.last_name = LName

        myuser.save()

        messages.success(request, 'your acount created successfully')

        return HttpResponse('Signin')

       
    return render(request, 'Signup.html')

def Signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = Authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)

        else:
            messages.error(request, "Bad")

    return render(request, 'Signin.html')

def Signout(request):
    return render(request, 'Signout.html')

