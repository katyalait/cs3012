from .suggest_git import Suggest
from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from github import *
from random import *
from datetime import *

class SuggestedMapping():

    def __init__(self, username, password):

        self.__suggest = Suggest(username, password)
        self.__suggest.get_suggested()
        self.__suggested_repos = self.__suggest.suggested_repositories

    def get_repos(self):
        return self.__suggested_repos


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
        label="Languages",
        data = dataset,
        color =(179, 181, 198),
        )

        ]
class BubbleChart(Chart):
    chart_type = 'bubble'
    scales = { 'xAxes': [Axes(type='time')],
        }

    def get_labels(self, contributors, forks_count, date):
        labels = []
        for contributor in contributors:
            string = "Label" + str(contributor)
            labels.append(string)
        return labels
    def get_datasets(self, contributors, forks_count, date):
        data = []
        index = len(contributors)
        for i in range(0,index-1):
            print("Int issue is with :" + str(contributors[i]))

            contributor = contributors[i]*3 #scale
            forks_counted = forks_count[i]
            last_updated_month = date[i].month
            last_updated_year = date[i].year
            print("Month: " + str(last_updated_month) + " Year: " + str(last_updated_year))
            last_updated = date[i]
            if last_updated_year >= 2017 and last_updated_month >9:
                data.append(
                {
                'x': last_updated,
                'y': forks_counted,
                'r': contributor
                }
                )

        return [DataSet(label="Suggested Repositories",
                        data=data,
                        backgroundColor='#FF6384',
                        hoverBackgroundColor='#FF6384',
                        borderColor='red'),
                #DataSet(label = "Test", data = {'x': '2018-11-12', 'y': 14, 'r': 13}, backgroundColor='#FF6384', hoverBackgroundColor='#FF6384',
                #        borderColor='red'
                #        )
                ]
