from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import LoginForm, GitForm
from .access_functions import start, repo

def get_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'main/index.html', {'form': form})


def index(request):
    if request.method == 'POST':
        form = GitForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thank you!")

    else:
        form = GitForm()
    return render(request, 'main/select.html', {'form': form})
