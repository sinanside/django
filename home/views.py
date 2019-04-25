from django.shortcuts import render
from .forms import ContactForm, LoginForm
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
    if login_form.is_valid():
        print(login_form.cleaned_data)
    data = {
        'title': 'Login sayfası',
        'content': 'Lütfen giriş yapınız.',
        'form': login_form
    }
    return render(request, 'auth/login.html', data)
