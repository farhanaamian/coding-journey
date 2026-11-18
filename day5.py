# DAY 5
# Your Day 5 (Friday) plan gets your code backed up online using Git (which tracks changes on your computer) and GitHub (the website that stores your code in the cloud)

# Step 1: Accounts & Installation
# •	Create a GitHub Account. Go to github.com
# , sign up for a free account, and remember your username and email address.
# •	Install Git. Download and install Git from git-scm.com using the default settings during installation.
# •	Verify Installation. Open your VS Code terminal (Ctrl + ~ on Windows or Cmd + ~ on Mac) and run git --version. If it prints a version number, you are ready.
# ________________________________________
# Step 2: One-Time Git Identity Setup
# Run these two commands in your VS Code terminal once so Git knows who is making changes (use the same email you used for GitHub):

# bash
# git config --global user.name "Your Name"
# git config --global user.email "your.email@example.com"

# Step 3: Create an Empty Repository on GitHub
# •	Start a New Repo. Log into GitHub, click the + icon in the top-right corner, and select New repository.
# •	Name It. Name the repository coding-journey (matching your desktop folder), leave it Public (or Private), and do not check "Add a README file" so it stays completely empty.
# •	Copy the URL. Click Create repository, then copy the HTTPS link shown on the setup screen (it looks like https://github.com).

# Step 4: Push Your Week 1 Files to GitHub
# Make sure your terminal in VS Code is open inside your coding-journey folder, then run these commands one by one:

# bash
# # 1. Turn your local folder into a Git repository
# git init

# # 2. Stage all your .py files for saving
# git add .

# # 3. Save a snapshot with a clear description
# git commit -m "Add Week 1 Python scripts (Days 2-4)"

# # 4. Rename the default branch to main
# git branch -M main

# # 5. Connect your folder to your GitHub repository (paste your actual URL)
# git remote add origin https://github.com

# # 6. Upload your code to GitHub
# git push -u origin main

# Note: On your very first git push, a browser window or pop-up will ask you to sign in to GitHub to authorize VS Code.

# Your Future Daily Workflow (Days 6 & 7)
# Once Step 4 is done, you never have to run git init, git branch, or git remote again for this folder. Every future day takes just three commands:
# bash
# git add .
# git commit -m "Complete Day 6 lists and loops"
# git push


