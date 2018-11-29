from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import LoginForm, GitForm
from .chart import RadarChart, LineChart, BarChart
from .productivity import Productivity, FollowingProductivity
from .languages import LanguagesFind
from .suggest_git import Suggest
from .models import Login
from urllib.parse import urlencode
from jchart import Chart
import github

def get_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        ref_id = 0
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = get_object_or_404(Login, username=cd['username'])
                ref_id = user.id
            except:
                print("User not found in database")
                form.save()
                user = get_object_or_404(Login, username=cd['username'])
                ref_id = user.id
            base_url = reverse('show')
            query_string =  urlencode({'ref_id': ref_id})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = LoginForm()

    return render(request, 'main/index.html', {'form': form})


def show(request):
    ref_id = request.GET.get('ref_id')
    user = get_object_or_404(Login, pk=ref_id)

    sg = Suggest(user.username, user.password)
    sg.get_suggested()
    suggested_repositories = sg.suggested_repositories

    lf = LanguagesFind()
    languages = lf.get_languages(user.username, user.password)

    pr = Productivity()
    dates = pr.get_dates(user.username, user.password)
    suggested_list = []
    for suggested in suggested_repositories:
        suggested_list.append({
        'name': suggested.name,
        'url': suggested.url,
        'contributors': len(list(suggested.get_contributors())),
        'forks_count': suggested.forks_count
        })
    fpr = FollowingProductivity()
    followingprod = fpr.get_following(user.username, user.password)
    
    bar = BarChart()
    bar.initialise()
    radar = RadarChart()
    line = LineChart()

    return render(request, 'main/select.html', {'suggested': suggested_list,
    'languages': languages, 'radar': radar, 'line': line, 'dates': dates, 'bar': bar, 'followingprod': followingprod,
    'username': user.username})
