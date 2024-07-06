#!/bin/bash

# Directory where your local git repository is located
REPO_DIR="/home/ubuntu/cicd_project"

# Path to the Python script
PYTHON_SCRIPT="/home/ubuntu/get_latest_commit.py"

# Navigate to the repository directory
cd "$REPO_DIR" || exit

# Run the Python script to check for new commits
python3 "$PYTHON_SCRIPT"

# Check the exit status of the Python script
if [ $? -eq 0 ]; then
    echo "New commits found. Pulling changes..."
    git pull origin main
    echo "Changes pulled and merged."
    echo "Copying changes in /var/www/html directory"
    cp -rf index.html /var/www/html/
    echo "Restating nginx service"
    systemctl restart nginx
else
    echo "No new commits found. No changes to pull."
    systemctl restart nginx
fi
