#!/bin/bash

[[ $# -gt 0 ]] && dir="$1" || dir="."

IFS=$'\n'
for f in $(find "$dir" -type f); do chmod 444 "$f"; done
for d in $(find "$dir" -type d); do chmod 555 "$d"; done

chown -R root:plex .
