from github import Github

class LanguagesFind():
    def __init__(self):
        self.__languages = {}
        self.__frequency = []

    def get_languages(self, username, password):
        #create github object
        g = Github(username, password)

        gitrepos = g.get_user().get_repos()
        
        for repo in gitrepos:
            language = repo.language
            try:
                res = self.__languages[language]
                self.__languages[language] = res+1
            except:
                self.__languages[language] = 1
        return self.__languages
