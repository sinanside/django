from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.


def home_view(request):
    data = {
        'isim': 'Umut',
        'gizli_icerik': "Çok gizli içerik"
    }
    return render(request, 'home.html', data)

def ledyaksondur_view(request):
    data = {
        'isim': 'Umut',
        'gizli_icerik': "Çok gizli içerik"
    }
    return render(request, 'ledyaksondur.html', data)

def python_page(request):
    data = {
        'isim': 'Umut',
        'gizli_icerik': "Çok gizli içerik"
    }
    return render(request, 'python.html', data)

def hakkımızda_view(request):
    data = {
        'isim': 'Umut',
        'gizli_icerik': "Çok gizli içerik"
    }
    return render(request, 'hakkımızda.html', data)

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


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    data = {
        'title': 'Kayıt sayfası',
        'content': 'Kayıt sayfamız.',
        'form': register_form
    }
    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'auth/register.html', data)
