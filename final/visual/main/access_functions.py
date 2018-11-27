from github import Github
import getpass
#creating access through access token

def start(username, password):
    access = False
    while(not access):
        try:
            g = Github(username, password)
            access = True
        except:
            return False

def repo(reponame):
    error = True
    while(error):
        try:
            repo = g.get_repo(repo_to_use)
            error = False
        except:
            return False
    return repo

#collects all the contributors for a git
def collect_contributors(repo):
    repo_contributors = []
    contributors = repo.get_contributors()
    print("Establishing repo contributors ...")
    for contributor in contributors:
        if(contributor!=owner):
            name = str(contributor.name)
            if name!="None":
                #print("Contributor: " + str(name))
                repo_contributors.append(contributor)
    #returns contributors in a list
    return repo_contributors

#finds the most popular of contributors to a git based on how many
#other contributors follow said user

def find_most_popular(repo_contributors, highest_following_of_contributors):
    most_popular_contributor = owner
    known_repo_contributors = []
    print("Searching contributor followers ... ")
    for contributor in repo_contributors:
        followers = contributor.get_followers()
        contributors_following_current = 0
        temp_followers_known = []
        for follower in followers:
            if follower in repo_contributors:
                contributors_following_current += 1
                print("Found follower " +str(follower.login) + " for " + str(contributor.login))
                temp_followers_known.append(follower)
        if contributors_following_current > highest_following_of_contributors:
            print("Found new popular contributor!")
            highest_following_of_contributors= contributors_following_current
            most_popular_contributor = contributor
            known_repo_contributors = temp_followers_known
    known_repo_contributors.append(most_popular_contributor)
    #returns the contributors to the git that follow the most popular contributor
    return known_repo_contributors
