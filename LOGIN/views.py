
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from .models import User

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
        print("PASswooor " +"="*40,pass1)
        print("PASswooor " +"="*40, make_password(pass1))
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username = username, email = email,
                 password = pass1,first_name = fname, last_name = lname)
        

        myuser.save()

        messages.success(request, 'Your acount hse been created')

        return redirect('signin')
       
    return render(request, 'Signup.html')

def Signin(request):

        if request.method == "POST":
           
           
    
            uname = request.POST['uname']
            # print(email)
            password = request.POST['pass1']
            
           
            user = authenticate(request ,username = uname, password = password)
            print("User ====",user)
            
            if user is not None:
            
                login(request, user)
                print(request.user.id)
                fname = user.first_name
                print(fname)
                return render(request, 'success.html', {'fname' : fname})
                
                
            else:
                messages.error(request, "invalid")
            

        return render(request, 'Signin.html')

def Signout(request):
    return render(request, 'Signout.html')

