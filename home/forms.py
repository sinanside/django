from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Adınızı Giriniz'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email adresiniz'
            }
        ))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mesajınız'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Kullanıcı Adınız'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Şifreniz'
            }
        )
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Kullanıcı Adınız'
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'mail adresiniz'
            }
        )
    )
    password = forms.CharField(label="Şifre",
                               widget=forms.PasswordInput(
                                   attrs={
                'class': 'form-control',
                'placeholder': 'Şifreniz'
            }
        )
                               )
    password2 = forms.CharField(label="Şifre Tekrarı",
                                widget=forms.PasswordInput(
                                    attrs={
                'class': 'form-control',
                'placeholder': 'Şifreniz'
            }
        )
                                )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exist():
            raise forms.ValidationError("Kullanıcı adı sistemde kayıtlı")
        return username

    def clean_email(self):
        username = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exist():
            raise forms.ValidationError("Email sistemde kayıtlı")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Şifre ve şifre tekrarı eşleşmiyor")
        return data
