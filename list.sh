#!/bin/bash
rootdir=/home/tor/rsc/ctrl-foundation
dlist[0]=book/ebook

for dir in "${dlist[@]}"
do
    echo '>>> listing: '$dir
    ls -1 -R $rootdir/$dir > $rootdir/$dir/LIST.txt
done

