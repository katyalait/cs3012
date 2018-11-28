from .suggest_git import Suggest

class Chart():

    def __init__(self, username, password):

        self.__suggest = Suggest(username, password)
        self.__suggest.get_suggested()

        self.__suggest.get_suggested()
        self.__suggested_repos = self.__suggest.suggested_repositories

    def get_repos(self):
        return self.__suggested_repos
