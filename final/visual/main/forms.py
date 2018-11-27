from django import forms
from github import Github
from .access_functions import start, repo


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget = forms.PasswordInput)

    def clean(self):
        cd = self.cleaned_data
        usr = cd['username']
        pwd = cd['password']
        try:
            g = Github(usr, pwd)
            access = True
        except:
            access = False
        if access ==False:
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
