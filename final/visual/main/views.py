from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import LoginForm
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
            #validate the form
            cd = form.cleaned_data
            try:
                #extract key for ref to user data
                user = get_object_or_404(Login, username=cd['username'])
                ref_id = user.id
            except:
                #save user information and get key for newly saved user
                form.save()
                user = get_object_or_404(Login, username=cd['username'])
                ref_id = user.id
            # redirect to show view and pass key for ref to user data
            base_url = reverse('show')
            query_string =  urlencode({'ref_id': ref_id})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = LoginForm()

    return render(request, 'main/index.html', {'form': form})


def show(request):
    #get user data through key
    ref_id = request.GET.get('ref_id')
    user = get_object_or_404(Login, pk=ref_id)

    # create LanguagesFind object and get languages user uses
    lf = LanguagesFind()
    languages = lf.get_languages(user.username, user.password)

    # create productivity object and get information on user productivity
    pr = Productivity()
    dates = pr.get_dates(user.username, user.password)


    # create suggest object and find suggested gits
    sg = Suggest(user.username, user.password)
    sg.get_suggested()
    suggested_repositories = sg.suggested_repositories
    suggested_list = []
    # populate list to use in template table
    for suggested in suggested_repositories:
        suggested_list.append({
        'name': suggested.name,
        'url': suggested.url,
        'contributors': len(list(suggested.get_contributors())),
        'forks_count': suggested.forks_count
        })

    # get the number of repos a user has for bar chart
    fpr = FollowingProductivity()
    followingprod = fpr.get_following(user.username, user.password)

    bar = BarChart() # associated with fpr
    bar.initialise() # initialise the global variable for labels
    radar = RadarChart() # associated with languages
    line = LineChart() # associated with productivity

    # render our template
    return render(request, 'main/select.html', {'suggested': suggested_list,
    'languages': languages, 'radar': radar, 'line': line, 'dates': dates, 'bar': bar, 'followingprod': followingprod,
    'username': user.username, 'ref_id': ref_id})

def log_out(request, ref_id):
    user = get_object_or_404(Login, pk=ref_id)
    user.delete()
    base_url = reverse('get_login')
    return redirect(base_url)
