from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=100)
    email = forms.EmailField(label='Email:', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Password:')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password:')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)