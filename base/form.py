from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control form-control-md  ', 
                'style': 'width: 300px;',
                
            }), 
            
            'email': forms.EmailInput(attrs={
                'class':'form-control  ', 
                'style': 'width: 300px;',
                
            }), 
            'password2': forms.PasswordInput(attrs={
                'class':'form-control ', 
                'style': 'width: 400px',
                
            }), 
            'password1': forms.PasswordInput(attrs={
                'class':'form-control', 
                'style': 'width: 400px',
                
            }), 
        }

        def save(self, commit=True):
            user = super(SignUpForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user