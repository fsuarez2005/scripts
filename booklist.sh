#!/usr/bin/env zsh



#echo "1. Think and Grow Rich by Napoleon Hill - http://amzn.to/2zr0Hck"|
gsed -n 's/[[:digit:]]\+\. \(.*\) by \(.*\) - \(.*\)/\1\t\2/p'