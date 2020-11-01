### Terminal tricks
From [this page](http://www.snazzylabs.com/five-advanced-tricks-for-mac-users/)
* show full file path in finder: `defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES; killall Finder`
* eliminate the Dock reveal delay: `defaults write com.apple.dock autohide-time-modifier -float 0.12;killall Dock`

### use iTerm instead of the default Terminal, set up specific terminal profile that pops out with hot keys