from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    if 'userid' not in request.session and 'registered' not in request.session:
        return redirect('/')
    else:    
        user = User.objects.last()
        context = {
            'username' : user.first_name,
        }
        return render(request, 'success.html', context)


def register(request):
    # validate input and return any errors
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="register")
        return redirect("/")
    else: 
        # hash password
        password_from_form = request.POST['password']
        hashed_password = bcrypt.hashpw(password_from_form.encode(), bcrypt.gensalt()).decode()
        # create user
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            # birthdate = request.POST['birthdate'],
            password = hashed_password
        )
        # redirect to /success
        request.session['registered'] = True
        return redirect('/swn')


def login(request):
    user = User.objects.filter(email=request.POST['login_email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            print(request.session['userid'])
            return redirect('/swn')
        else:
            messages.error(request, 'Password is incorrect.', extra_tags="login")
            return redirect('/')
    else:
        messages.error(request, 'User does not exist.', extra_tags="login")
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')



