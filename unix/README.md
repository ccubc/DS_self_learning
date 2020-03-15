# The Unix Workbench

### Useful terminal commands:
* `ls`: list files and directories; `ls -l`: long list (more detailed information)
* `mkdir`: create a new directory
* `cd`: change directories
* `rm`: remove files and directories
* `pwd`: print working directory

### About directory:
* `/`: root directory, e.g. use `cd /` to change to root directory
* `~`: home directory, to cd to home directory: use any one of (1) `cd ` (2) `cd ~` (3) `cd /Users/username`

### Creation and Inspection
* `touch journal-2020-03-14.txt`: create a new file in the current directory
* `wc todo.txt`: word count command, # lines, # words, # characters
* `cat todo.txt todo.txt`: concatenate files and print them to terminal
* `less Documents/a-tale-of-two-cities.txt`: print a preview of multi-page files (print the first several lines)
* `head document.txt`: print the head of the document
* `tail document.txt`: print the tail of the document
* `echo "I'm in the file." > echo-output.txt`: use `>` for **output redirection**
* `echo "I have been appended." >> echo-output.txt`: use `>>` to **append** text to the end of a file.
* nano is a simple text editor in terminal.


### Migration and Destruction: moving, renaming, copying, deleting files and folders
* `mv journal-2020-03-14.txt Journal`: move the file journal-2020-03-14.txt to the Journal folder
* `mv Journal Documents`: move the Journal folder to Documents folder
* `mv todo.txt todo-2020-03-14.txt`: use mv to rename file and folders
* `cp echo-out.txt Desktop`: copy a file from one location to another
* `cp -r Documents Desktop`: copy a file folder, r means recursive, every underlying directory structure will be copied
* `rm echo-out.txt`: remove file or folder, i.e. permanently delete, not recommended (no way to undo)

