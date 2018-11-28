from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import LoginForm, GitForm
from .chart import SuggestedMapping, BubbleChart, RadarChart
from .languages import LanguagesFind
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
    chart = SuggestedMapping(user.username, user.password)
    suggested_repositories = chart.get_repos()
    contributors = []
    forks_count = []
    date = []
    names = []
    for suggested in suggested_repositories:
        names.append(suggested.name)
        contributors.append(len(list(suggested.get_contributors())))
        forks_count.append(suggested.forks_count)
        date.append(suggested.updated_at)


    bubble = BubbleChart()
    radar = RadarChart()
    lf = LanguagesFind()
    languages = lf.get_languages(user.username, user.password)

    return render(request, 'main/select.html', {'bubble_chart': bubble, 'contributors': contributors,
    'forks_count': forks_count, 'date': date, 'names': names, 'languages': languages, 'radar': radar})
