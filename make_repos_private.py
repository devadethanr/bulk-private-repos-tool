import requests

# Replace with your GitHub username and personal access token
USERNAME = 'your username'
TOKEN = 'your key'

# List of repository names you want to make private
repositories = [
    'repo-1',
    'repo-2',
    'repo-3'
]

# Base URL for GitHub API
BASE_URL = 'https://api.github.com'

# Function to make a repository private
def make_repo_private(repo_name):
    """_summary_

    Args:
        repo_name (_type_): _description_
    """
    url = f'{BASE_URL}/repos/{USERNAME}/{repo_name}'
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'private': True
    }
    response = requests.patch(url, headers=headers, json=data, timeout=10)
    #remove timeout arg if request ends unexpectedly
    if response.status_code == 200:
        print(f'Repository {repo_name} is now private.')
    else:
        print(f'Failed to make {repo_name} private: {response.status_code}')

# Loop through the list of repositories and make each one private
for repo in repositories:
    make_repo_private(repo)
