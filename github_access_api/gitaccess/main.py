from github import Github

#creating access through access token
g = Github("4df439e89aaaa3d4e55b1ad70f31efede72c06c2")
repo = g.get_repo("phadej/github")
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)
