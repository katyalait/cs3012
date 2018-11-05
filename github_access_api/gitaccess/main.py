from github import Github
import getpass
#creating access through access token
g = ""
repo = ""
owner = ""
known_repo_contributors = []

def start():
    username = input("Please put in your username: ")
    password = getpass.getpass("Please provide your password: ")
    g = Github(username, password)
    error = True
    while(error):
        try:
            repo_to_use = input("Please put in the git repo you wish to interrogate: ")
            repo = g.get_repo(repo_to_use)
            error = False
        except:
            print("Incorrect repo please try again")
    return repo

#collects all the contributors for a git
def collect_contributors():
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
repo = start()
contributors = collect_contributors()
followers = []
known_repo_contributors = find_most_popular(contributors, 0)
most_popular_contributor = known_repo_contributors.pop()

print("The contributor to this repo most followed by other contributors is " + str(most_popular_contributor.name) +"\nLogin name: " + str(most_popular_contributor.login))
print("Contributors following user: ")
for follower in known_repo_contributors:
    print("\t-" + str(follower.login))
