from github import Github

class Productivity():
    def __inti__(self):
        pass

    def get_dates(self, username, password):
        g = Github(username, password)
        user = g.get_user()
        dates = {}
        repos = user.get_repos()
        commits = []
        events = []
        for repo in repos:
            try:
                commits.append(repo.created_at)
                commits.append(repo.pushed_at)
                commits.append(repo.updated_at)
                found_commits = repo.get_commits(sha=NotSet, path=NotSet, since=NotSet, until=NotSet, author=user)
                for commit in found_commits:
                    status.get_statuses()[0]
                    commits.append(status.created_at)

            except:
                pass
            try:
                found_events = repo.get_events()
                for event in found_events:
                    events.append(event)
            except:
                pass

        for commit in commits:
            date = commit
            try:
                res = dates[date]
                dates[date] = res+1
            except:
                dates[date] = 1
        for events in events:
            date = event.created_at
            try:
                res = dates[date]
                dates[date] = res+1
            except:
                dates[date] = 1

        return dates

class FollowingProductivity():

    def __init__(self):
        self.following_productivity = {}
        self.user = ""

    def get_following(self, username, password):
        g = Github(username, password)
        print("Loggin in " + str(username))
        self.user = g.get_user()
        users_following = self.user.get_following()
        for user_f in users_following:
            repos = user_f.public_repos
            self.following_productivity[user_f.login] = repos
        return self.following_productivity
