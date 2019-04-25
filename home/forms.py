from django import forms


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
        widget=forms.TextArea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mesajınız'
            }
        )
    )
