#!/usr/bin/env zsh

SSHROOT="$HOME/.ssh"
KNOWNHOSTS="known_hosts"


IPADDR="168.231.65.165"

gsed "/${IPADDR}/ {d}" "$SSHROOT/$KNOWNHOSTS" > "$SSHROOT/${KNOWNHOSTS}.tmp"



