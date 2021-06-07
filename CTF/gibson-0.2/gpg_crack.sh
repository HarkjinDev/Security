#!/bin/bash
# Description:
# This is gpg's advanced tool to get output easily.

# Usage:
# gpg_crack.sh <wordlist_file> <decrypt_file> <output_file>

if [ $# -lt 3 ] ; then
        echo "Usage : gpg_crack.sh <wordlist_file> <decrypt_file> <output_file> "
        exit 1
fi 

WORDLIST=$1
DECRYPT=$2
OUTPUT=$3

for x in $(cat $WORDLIST)
do
        clear
        echo "[*] Trying : $x"
        echo "$x" | gpg --passphrase-fd 0 \
                        -q --batch --no-tty \
                        --allow-multiple-messages \
                        --ignore-mdc-error \
                        --output $OUTPUT \
                        --decrypt $DECRYPT
        if [ $? -eq 0 ] ; then
                echo "========== Decrypt Result ============"
                echo "[+] GPG passphrase is : {$x}"
                break
        else
                echo "[-] GPG passphrase not found"
        fi
done
