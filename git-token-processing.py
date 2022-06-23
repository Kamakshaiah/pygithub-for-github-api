# https://pygithub.readthedocs.io/en/latest/introduction.html#download-and-install
# https://pygithub.readthedocs.io/en/latest/examples.html
# https://www.thepythoncode.com/article/using-github-api-in-python

# https://stackoverflow.com/questions/59861312/how-to-get-the-list-of-source-repositories-of-a-user-organisation-on-github
import os

import base64
from github import Github
from pprint import pprint

filepath = 'D:\Work\git'
dir_path = 'D:\Work\git'
file_path = dir_path + '\github-token.txt'

assert os.path.isfile(file_path)

def read_token(file_path):
    with open(filepath, 'r') as token:
        tkn = token.read()
        return tkn

tkn = read_token(file_path)
print(tkn)



# Github username
username = "Kamakshaiah"
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)

for repo in user.get_repos():
    print(repo)

for r in u_name.get_repos():
    if r.stargazers_count == 0:
        continue
    else:
        print(r.name, r.stargazers_count)

for r in g.search_repositories('litreviewer'):
    print(r.stargazers_count)

for r in g.search_repositories('litreviewer'):
    print(r.forks_count)
