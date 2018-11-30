from django import forms
from github import Github
from .models import Login

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ['username', 'password']

    def clean(self):
        cd = self.cleaned_data
        usr = cd['username']
        pwd = cd['password']
        try:
            g = Github(usr, pwd)
            access = True
        except:
            access = False
            print("Wrong login")
            raise forms.ValidationError("Incorrect login details.")
        return cd
