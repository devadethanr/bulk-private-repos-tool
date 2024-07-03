# bulk-private-repos-tool

This `README.md` file provides clear instructions on how to set up, configure, and use the script.
This script allows you to automate the process of making multiple GitHub repositories private using the GitHub API.

## Prerequisites
- Python 3.x
- `requests` library (install using `pip install requests`)
- GitHub Personal Access Token with `repo` scope

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/devadethanr/bulk-private-repos-tool.git
   cd make-repos-private

2. pip install requests

3. Generate a Personal Access Token:
Go to your GitHub settings.
Navigate to Developer settings -> Personal access tokens.
Click Generate new token, and select the repo scope.
Copy the generated token.

4. Configure the Script:
Open bulk-private-repos-tool.py in a text editor.
Replace your-username with your GitHub username.
Replace your-personal-access-token with your GitHub personal access token.
Add the names of the repositories you want to make private to the repositories list.

5. run
   `python make_repos_private.py`
