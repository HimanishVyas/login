

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from httplib2 import Authentication

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create(username = username, email = email, password = pass1, is_staff = True, is_superuser = True)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Your acount hse been created')

        return redirect('signin')
       
    return render(request, 'Signup.html')

def Signin(request):
    return render(request, 'Signin.html')

def Signout(request):
    return render(request, 'Signout.html')

