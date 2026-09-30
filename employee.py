from flask import Flask
app=Flask(__name__)
@app.route('/employee/<int:emp_id>/<name>/<department>')
def employee(emp_id,name,department):
    return f"""
<h1>employee profile</h1>
<b>employee id:</b>{emp_id}<br><br>
<b>name:</b>{name}<br><br>
<b>department:</b>{department}<br><br>
"""
if __name__=="__main__":
    app.run(debug=True)

No.
Command
Used for / Task
1
git --version
Check installed Git version
2
git config --global user.name "Your Name"
Set Git username
3
git config --global user.email "your@email.com"
Set Git email
4
git config --list
Display Git configuration
5
git init
Create a new local Git repository
6
git clone <URL>
Copy/clone an existing GitLab/GitHub repository to local system
7
cd project-folder
Move into the project/repository folder
8
git status
Check current repository status
9
touch file.py
Create a new file
10
vim file.py
Create/edit a file using Vim
11
git add file.py
Add one file to staging area
12
git add .
Add all changed/new files to staging
13
git commit -m "Initial commit"
Save staged changes as a commit
14
git log
Display commit history
15
git remote -v
Display connected remote repository URL
16
git remote add origin <URL>
Connect local repository to GitLab repository
17
git push -u origin main
Push local main branch to GitLab
18
git pull origin main
Get latest changes from GitLab
19
git branch
Display existing branches
20
git branch feature
Create a new branch named feature
21
git switch feature
Switch to the feature branch
22
git switch -c feature
Create and switch to a new branch
23
git branch -d feature
Delete a local branch
24
git merge feature
Merge feature branch into current branch
25
git diff
Show changes made in files
26
git restore file.py
Discard unstaged changes in a fi
