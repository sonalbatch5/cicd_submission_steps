import requests
import os
import sys
# Configuration

GITHUB_USER = "sonalbatch5"
REPO_NAME = "cicd_project"
LAST_COMMIT_FILE = "last_commit.txt"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/commits"
// Hide the access token for security reason
ACCESS_TOKEN = "xxxxxx"

# Function to get the latest commit SHA


# Function to get the latest commit SHA
def get_latest_commit_sha():
    headers = {
        "Authorization": f"token {ACCESS_TOKEN}"
    }
    response = requests.get(GITHUB_API_URL, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    commits = response.json()
    if commits:
        return commits[0]['sha']
    return None

# Function to read the last commit SHA from a file
def read_last_commit_sha():
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, 'r') as file:
            return file.read().strip()
    return None

# Function to write the latest commit SHA to a file
def write_last_commit_sha(commit_sha):
    with open(LAST_COMMIT_FILE, 'w') as file:
        file.write(commit_sha)

# Check for new commits
def check_for_new_commits():
    latest_commit_sha = get_latest_commit_sha()
    if not latest_commit_sha:
        print("No commits found in the repository.")
        return 0 

    last_commit_sha = read_last_commit_sha()

    if latest_commit_sha != last_commit_sha:
        print("New commit found!")
        write_last_commit_sha(latest_commit_sha)
        return 1  
    else:
        print("No new commits since the last check.")
        return 0 

# Run the check
if __name__ == "__main__":
    if check_for_new_commits():
        sys.exit(0)  # New commit found
    else:
        sys.exit(1)  # No new commit
