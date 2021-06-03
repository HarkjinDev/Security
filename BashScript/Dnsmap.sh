#!/bin/bash

# Description:
# This tool is the advanced of the command "host"
# The first sector of output is checking the existence of the domain's host names (ex www, ftp)
# The second sector of output is the IP address list of the host names

# Usage:
# Dnsmap.sh <domain name>

if [ $# -ne 1 ] ; then
	echo "Usage : . Dnsmap.sh <domain name>"
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


