#!/bin/bash

if [ $# -ne 1 ] ; then
	echo "Usage : $0 <domain name>"
	exit 1
fi

DOMAIN=$1
TMP1=/tmp/tmp1
RESULT=/tmp/tmp2
> $RESULT

DICT=/tmp/dns.txt
> $DICT
cat << EOF >> $DICT
www
ftp
mail
ns
ns1
aaaaa
EOF

for i in $(cat $DICT)
do
	host $i.$DOMAIN > $TMP1
	if [ $? -eq 0 ] ; then
		echo "[  OK  ] $i.$DOMAIN"
		cat $TMP1 | sed 's/has address/:/' \
			| sed 's/is an alias for/:/' \
			| sed '/mail is handled/d' >> $RESULT
	fi
done
echo
echo "========== Result Output =========="
cat $RESULT
echo


