## Git cheatsheet

### Useful terminal commands:
* `ls`: list files and directories
* `mkdir`: create a new directory
* `cd`: change directories
* `rm`: remove files and directories
* `pwd`: print working directory


### Create a Git Repo
* `git init`: create brand new repos from scratch on your computer
* `git clone`: copy existing repos from somewhere else to your local computer  <br>
When cloning a repo, make sure the terminal's current working directory isn't located in a Git repo. (cannot nest Git repos). Git clone will create a new directory. 
```
git clone https://github.com/...  # clone a repo
git clone https://github.com/... new_repo_name  # clone a repo and rename
```

* `git status`: check the status of the repo

### Review a Repo's History
Commits should be frequent and descriptive.
* `git log`: displays information about the existing commits 
* `git show`: displays information about the most recent commit 
* `git log --oneline`: displays just the short SHA and the commit message
* `git log --stat`: shows number of files changed and number of added/removed lines
* `git log -p` or `git log --patch`: display the actual changes made to a file
* `git log -p SHA` or `git show SHA`: display the changes in a specific commit

#### Keyboard shortcuts for pager: 
* up/down arrow: scroll up/down
* Q: get out of the pager <br><br>

#### contents displayed in the git log:
* the SHA: it's a unique ID for each commit
* the author
* the date
* the commit message

### Add Commits To A Repo
* `git add`: add a file to the staging index
* `git commit -m "commit message" `: add a file from the staging index to the repo
* `git diff`: show uncommitted changes
* '.gitignore' file: list the names of files to ignore

### Branching, and Merging
* `git branch`: allows multiple lines of development so that one can make changes without affecting the `master` branch, this command can be used to list all branch names in the repository, create new branches, and delete branches<br>
* `git checkout`: switch between different branches and tags
* `git merge`: combines changes on different branches
<br><br>
The workflow to use branches: <br>
* `git branch sidebar`: create a branch called sidebar
* `git checkout sidebar`: to make commits to the `sidebar` branch instead of the `master` branch, this command will switch to the `sidebar` branch
* `git branch -d sidebar`: delete the `sidebar` branch (Git won't let you delete a branch if you are currently on this branch, or if this branch contains unique commits that aren't on any other branch. To force delete, use `git branch -D sidebar`)
* `git merge sidebar`: make sure you're on the `master` branch and run this line to merge the `sidebar` branch
* A merge conflict will occur if the exact same lines are changed in separate branches.
<br>

### Undoing Changes
* `git commit --amend`: alter the most-recent commit
* `git revert SHA`: reverses given commit
* `git reset`: erases commits (this is dangerous!)

### Tagging
* `git tag <tag name>`: add tags to specific commits, e.g., specifying this commit completes 'version 1.0'
* `git tag <tag name> <reference of commit>`: create a tag from a past commit; `<reference of commit>` can be part of the SHA number
* `git tag` or `gt`: list all tags
* `git tag -l "v1.*"` or `gtl`: list all tags starting with "v1."
* `git tag -a <tag name> -m "annotated tag message"`: create an annotated tag
* `git show <tag name>`: print out the difference in this tag
* `git push origin <tag name>`: push a specific tag to remote
* `git push --tags` or `gpt`: push all tags to remote
* `git tag -d <tag name>`: delete tags from local
* `git push origin -d <tag name>`: delete tags from remote
* `git checkout -b <branch name> <tag name>`: create a branch from a tag and checkout the branch









