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
        # passed in dict contains the dates and the number describing activity as the value
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

    # gets the languages from the dict
    def get_labels(self, languages):
        list = []
        for language in languages:
            list.append(language)
        return list

    # extracts the value from the dict
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

    # creates a global variable that holds the names of the users represented on the bar chart
    def initialise(self):
        self.following = []

    def get_labels(self, following):
        return self.following

    def get_datasets(self, following_repos):
        data = {}
        # for each person the user follows
        for user in following_repos:
            # max number of users represented on the bar chart
            if len(data)< 7:
                # initial population
                data.update({user: following_repos[user]})
            else:
                # if any more users are found then we check the 6 currently in the dict
                for line in data:
                    # we extract the number of repos they have
                    current = data[line]
                    # we get the number of repos the person they follow has
                    res = following_repos[user]
                    # if the number of repos the person has happens to be greater than the one in the dict
                    if res > current:
                        # we delete that line in the dict
                        del data[line]
                        # create a new line in the dict for the person with the most repos
                        data[follow] = following_repos[follow]
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
