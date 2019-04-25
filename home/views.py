from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def home_view(request):
    data = {
    'isim': 'Umut'
    }
    return render(request,'home.html',data)


def about_view(request):
    data = {
        'isim': 'Umut'
    }
    return render(request, 'about.html', data)


def contact_view(request):
    contact_form = ContactForm(request.POST or None)
    data = {
        'title': 'İletişim sayfası',
        'content': 'İletişim formumuzu doldurunuz.',
        'form': contact_form
    }
    return render(request, 'contact.html', data)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    data = {
        'title': 'Login sayfası',
        'content': 'Lütfen giriş yapınız.',
        'form': login_form
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            print("hata")

    return render(request, 'auth/login.html', data)
