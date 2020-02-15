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

