
# Create your views here.


from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext

from bankingapp.forms import CustomerForm


#from . models import CustomerModel
#from . forms import CustomerForm
# Create your views here.
def base(request):
    return render(request, "base.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
    return render(request, "registration.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def newpage(request):
    return render(request, "newpage.html")


def customer(request):
        if request.method == 'POST':
            form = CustomerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("submit")
            else:
                return redirect("customer")
        else:
            context = {}
            context['form'] = CustomerForm
            return render(request, "form.html", context=context)


def submit(request):
    return render(request,"submit.html")




def logout(request):
    auth.logout(request)
    return redirect('/')
