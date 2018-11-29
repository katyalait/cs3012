from .suggest_git import Suggest
from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from github import *
from random import *
from datetime import *

class LineChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],

    }

    def get_datasets(self, dates):
        data = []
        for date in dates:
            data.append({
            'y': dates[date],
            'x': date
            })
        return [DataSet(
            type='line',
            label='Activity',
            data=data,
        )]

class RadarChart(Chart):
    chart_type = 'radar'

    def get_labels(self, languages):
        list = []
        for language in languages:
            list.append(language)
        return list

    def get_datasets(self, languages):
        dataset = []
        for language in languages:
            dataset.append(languages[language])

        return [ DataSet(
        label="Repositories",
        data = dataset,
        color =(255, 99, 132),
        )

        ]
class BarChart(Chart):
    chart_type = 'bar'

    def initialise(self):
        self.following = []

    def get_labels(self, following):
        return self.following

    def get_datasets(self, following_contributions):
        data = {}
        for user in following_contributions:
            if len(data)< 7:
                data.update({user: following_contributions[user]})
            else:
                for line in data:
                    current = data[line]
                    res = following_contributions[user]
                    if res > current:
                        del data[line]
                        data[follow] = following_contributions[follow]
                        break
        return_data = []
        for line in data:
            self.following.append(line) # get label
            return_data.append(data[line]) #get data
        colors = [
            rgba(255, 99, 132, 0.2),
            rgba(54, 162, 235, 0.2),
            rgba(255, 206, 86, 0.2),
            rgba(75, 192, 192, 0.2),
            rgba(153, 102, 255, 0.2),
            rgba(255, 159, 64, 0.2)
        ]

        return [DataSet(
                        data=return_data,
                        borderWidth=1,
                        backgroundColor=colors,
                        borderColor=colors)]
