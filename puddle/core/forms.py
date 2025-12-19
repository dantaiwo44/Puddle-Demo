from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField( widget= forms.TextInput(
        attrs={
            'class': 'w-full py-4 px-6 rounded-xl'} )
    )
    password = forms.CharField( label='Password',
                 widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'w-full py-4 px-6 rounded-xl'} ) )

class SignUpForm(UserCreationForm):
    username = forms.CharField( widget= forms.TextInput(
        attrs={
            'class': 'w-full py-4 px-6 rounded-xl'} )
    )
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(
        attrs={
            'class': 'w-full py-4 px-6 rounded-xl'} ),
            help_text='Required. Inform a valid email address.')
    password1 = forms.CharField( label='Password',
                 widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'w-full py-4 px-6 rounded-xl'} ) )
    password2 = forms.CharField( label='Password',
                 widget=forms.PasswordInput(attrs={
            'placeholder': 'RepeatPassword',
            'class': 'w-full py-4 px-6 rounded-xl'} ) )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )  