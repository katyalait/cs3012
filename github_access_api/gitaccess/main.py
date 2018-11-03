from github import Github

#creating access through access token
g = Github("68b126c142c7c1a646b0c53a316fcf0d4be7ac5c")
repo = g.get_repo("phadej/github")
owner = repo.owner
known_repo_contributors = []

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

    return repo_contributors

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
    return known_repo_contributors

contributors = collect_contributors()
followers = []
known_repo_contributors = find_most_popular(contributors, 0)
most_popular_contributor = known_repo_contributors.pop()

print("The contributor to the Haskell repo most followed by other contributors is " + str(most_popular_contributor.name) +"\nLogin name: " + str(most_popular_contributor.login))
print("Contributors following user: ")
for follower in known_repo_contributors:
    print("\t-" + str(follower.login))
