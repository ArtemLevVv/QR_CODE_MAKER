from django import forms

class User_Form(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={"class": "name", "placeholder": "Введіть ім'я"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "email", "placeholder": "Введіть e-mail"}),
        label='',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "password", "placeholder": "Введіть пароль"}),
        label='',
    )
    second_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "p_password", "placeholder": "Повторіть пароль"}),
        label='',
    )

class Login_Form(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={"class": "name", "placeholder": "Введіть ім'я"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "password", "placeholder": "Введіть пароль"}),
        label='',
    )