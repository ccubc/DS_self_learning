## Better Terminal Experience with Zsh (using Prezto)

### Disclaimer
I am an *absolute newbie* to serious coding. Now that since my coworkers run their Python script on terminal, and that I'm required to use Git every day, I'm starting to use the Terminal a lot, or shell, console, command line, whatever you call that scary black and white window with only a cursor to navigate through. <br>
Fortunately a friend pointed me to this repo: [Prezto](https://github.com/sorin-ionescu/prezto), and it was so good that made me want to write this.
## Installing Prezto could:
* enable using alias to your daily commands (e.g., type gcm when you used to type git commit -m)
* display the git branch and the git status on the terminal, when you are in a git repo
* fast cd to a directory you've recently visited (whereas what I used to do is constantly cd and ls and pwd) by just typing part of that directory name
* syntax highlighting<br><br>
These are the features that I found extremely useful, but there must be more to find :) <br><br>
Below is a simple demo of ``using alias for git commit and displaying git branch and status``. Instead of typing `git branch`, you only need to type `gb` <br><br>
![demo](https://github.com/ccubc/DS_self_learning/blob/small_potato/unix/prezto_setup/demo.png "demo")

## How to Install and Set up Prezto on Mac OS
#### 1. Install Prezto
Just follow the install instructions [HERE](https://github.com/sorin-ionescu/prezto). It's just 4 copy and pastes to your terminal.

#### 2. Enable the Submodules Including git

1. run this in the terminal to open the .zpreztorc file and add the submodules to it <br>
`open ~/.zpreztorc`
2. Scroll down the file until you see lines of submodules there, such as 'environment', 'terminal', 'editor', etc. <br>Then add 'git', 'fasd', 'syntax-highlighting' before the line of 'prompt'<br>
3. save and close the file
4. Open a new terminal window, you will see the lovely changes.

#### Adding Emojis to Your Terminal🐣
1. On Mac, you could access the emoji keypad with "Ctrl"+"Command"+"Space".
2. Open the file that governs the sorin theme asthetics (sorin theme is the default theme) by `open ~/.zprezto/modules/prompt/functions/prompt_sorin_setup`
3. Look for the section "set git-info parameters". You may add emoji here. For example, change the line `  zstyle ':prezto:module:git:info:modified' format ' %%B%F{4}✱%f%%b'` to `  zstyle ':prezto:module:git:info:modified' format ' %%B%F{4}✱%f%%b 🎃'`


#### Trouble shooting with Anaconda
If you have installed Anaconda before this, you might find that running `jupyter notebook` in zsh would throw an error with a message like "jupyter command not found". (I encountered this problem myself.) The reason being that when you installed Anaconda, it would write something in your .bash_profile, so that every time when starting a bash session, those commands would be run to tell the computer where to find the paths, etc. But after changing your shell to zsh, the computer no longer knows. After searching for the solutions and trying them out, I found the codes below ([from this post](https://github.com/conda/conda/issues/8492))solved my problem.<br>
`conda update conda` <br>
`conda init zsh`

