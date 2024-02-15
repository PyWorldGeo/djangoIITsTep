from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from .forms import AddHeroForm

# Create your views here.
def index(request):
    features = Product.objects.all()

    addhero = {}
    addhero['form'] = AddHeroForm()
    if request.method == 'POST':
        name = request.POST["name"]
        details = request.POST["details"]
        img_url = request.POST["img_url"]
        new_hero = Product(name=name, details=details,img_url=img_url)
        new_hero.save()

    return render(request, 'index.html', {"features": features, "addhero": addhero})





def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Is Already Used!')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Already Used!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')



        else:
            messages.info(request, "Passwords don't match!")
            return redirect('register')


    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "Username or Password is Incorrect!")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    list_of_posts = ["Nika", "Tatia", "Bakari", "Davit", "Avtandil"]
    return render(request, 'counter.html', {'posts': list_of_posts})

def post(request, var):
    return render(request, 'post.html', {'var': var})

@login_required
def profile(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['password1']
        new_password2 = request.POST['password2']



        current_user = request.user
        if check_password(old_password, current_user.password) and new_password1== new_password2:
            current_user.password = make_password(new_password1)
            current_user.save()
            messages.info(request, "პაროლი წარმატებით შეიცვალა!")
        else:
            messages.info(request, "პაროლი არ ემთხვევა!")
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')


