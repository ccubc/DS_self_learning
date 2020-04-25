## Better Terminal Experience with Prezto

### Disclaimer
I am an *absolute newby* to serious coding. Now that since my coworkers run their Python script on terminal (whereas where I used to do is either Jupyter Notebook or Spider), and that I'm required to use Git every day, I'm starting to use the Terminal a lot, or shell, console, command line, whatever you call that scary black and white window with only a cursor to navigate through. <br>
Fortunately a friend pointed me to this repo: [Prezto](https://github.com/sorin-ionescu/prezto), and it was so good that made me want to write this.
## Installing Prezto could:
* enable using alias to your daily commands (e.g., type gcm when you used to type git commit -m)
* display the git branch and the git status on the terminal, when you are in a git repo
* fast cd to a directory you've recently visited (whereas what I used to do is constantly cd and ls and pwd) by just typing part of that directory name
* syntax highlighting<br><br>
These are the features that I found extremely useful, but there must be more to find :) <br><br>
Below is a simple demo of ``using alias for git commit and displaying git branch and status``. Instead of typing `git branch`, you only need to type `gb`
![demo](https://github.com/ccubc/DS_self_learning/blob/small_potato/unix/prezto_setup/demo.png "demo")

## How to Install and Set up Prezto
#### 1. Install Prezto
Just follow the install instructions [HERE](https://github.com/sorin-ionescu/prezto). It's just 4 copy and pastes to your terminal.

#### 2. Enable the Submodules Including git
1. cd to your home directory by type cd followed by a space and then hit enter in your terminal<br>
`cd ` <br>
2. look for the hidden file: .zpreztorc<br>
`ls -a` <br>
check whether the .zpreztorc is there --- it should be, then continue to next step <br>
3. enter this file and add the submodules to it <br>
`nano .zpreztorc`
4. You will enter nano, which is a text editor on your terminal. <br>Use your cursor to scroll down the file until you see lines of submodules there, such as 'environment', 'terminal', 'editor', etc. <br>Then add 'git', 'fasd', 'syntax-highlighting' before the line of 'prompt'<br>
5. After you are done adding those, hit Ctr + X (this will exit) <br>
It will ask you whether to save changes, so hit Y <br>
It will ask you whether to the name to write is .zpreztorc, so hit enter <br>
6. Open a new terminal window, you will see the lovely changes.

