#!/bin/bash
rootdir=/home/tor/rsc/ctrl-foundation
dlist[0]=book/ebook
dlist[1]=course/ecourse
dlist[2]=talk/etalk

for dir in "${dlist[@]}"
do
    echo '>>> listing: '$dir
    ls -1 -R $rootdir/$dir > $rootdir/$dir/LIST.txt
done

