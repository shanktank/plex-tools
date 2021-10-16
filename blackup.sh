#!/bin/bash

blackup="/black/blackup/"
files="Documents/Git Documents/Projects Documents/Text .history"
home="/home/user/"
log="/root/blackup.log"

exec 1 > $log
exec 2 > $log

echo $(date)
cd $home && for f in $files; do
    rsync -azhv --relative "$f" "$blackup"
done
echo
