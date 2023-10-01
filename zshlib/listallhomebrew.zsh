#!/bin/zsh

# get a list of all available Homebrew packages
# with descriptions

MAXPARALLEL=10

brew search "/.*"|xargs -P $MAXPARALLEL -I % brew desc --eval-all % 

