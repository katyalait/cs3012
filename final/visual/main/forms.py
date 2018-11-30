from django import forms
from github import Github
from .access_functions import start, repo
from .models import Login

class LoginForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
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


class GitForm(forms.Form):
    gitname = forms.CharField(label='Git Repo', max_length=100)

    def clean(self):
        cd = self.cleaned_data
        name = cd['gitname']
        error = True
        try:
            repo = g.get_repo(name)
            error = False
        except:
            error= True
        if error==True:
            raise forms.ValidationError("Invalid git repo name.")
        return cd
