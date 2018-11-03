from github import Github

#creating access through access token
g = Github("4df439e89aaaa3d4e55b1ad70f31efede72c06c2")
repo = g.get_repo("phadej/github")
contents = repo.get_contents("")
owner = repo.owner
#gets the contents of main directory, returns as a ContentFile JSON object
for content_file in contents:
    print(content_file)

events = repo.get_events()
for event in events:
    print(event)

issues = repo.get_issues()
for issue in issues:
    print(issue)
    issue_events = issue.get_events()
    for issue_event in issue_events:
        actor = issue_event.actor
        if(actor!=owner):
            print("\tEvents: " + str(issue_event))
            print("\t\tActor: " + str(actor) + "Followed by: " + str(actor.followers))

contributors = repo.get_contributors()
for contributor in contributors:
    if(contributor!=owner):
        name = contributor.name
        print("Contributor: " + str(name))
