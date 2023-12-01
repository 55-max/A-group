#!/bin/sh

HUB=`/usr/bin/lsusb -v 2>/dev/null | grep ^Bus | grep "Genesys Logic, Inc. Hub" | head -1`
BUS=`echo $HUB | awk '{print $2}'`
DEV=`echo $HUB | awk '{print $4}' | sed -e "s/\(.*\)\:/\1/p;d"`

for i in 1 2 3 4
do
     /usr/local/bin/hub-ctrl -b $BUS -d $DEV -P $i -p 0
done