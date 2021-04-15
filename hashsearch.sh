#!/bin/bash -
#
# Cybersecurity Ops with bash
# hashsearch.sh
#
# Description: 
# Recursively search a given directory for a file that
# matches a given SHA-1 hash
#
# Usage:
# hashsearch.sh <hash> <directory>
#   hash - SHA-1 hash value to file to find
#   directory - Top directory to start search
#

HASH=$1
DIR=${2:-.}	# default is here, cwd

# convert pathname into an absolute path
function mkabspath ()				# <6>
{
    if [[ $1 == /* ]]				# <7>
    then
    	ABS=$1
    else
    	ABS="$PWD/$1"				# <8>
    fi
}

find $DIR -type f |				# <1>
while read fn
do  
    # sda1sum printouts hash value + blank + filename
    # ex) 6a90fe898fed98bbe *hasfile.txt
    THISONE=$(sha1sum "$fn")			# <2>
    
    # only has hash value(need to erase blank and filename)
    # {VAR%%WORD} : Delete long matched words from the end of variable
    # this( *) means blank + *(means filename)
    THISONE=${THISONE%% *}			# <3>
    if [[ $THISONE == $HASH ]]
    then
	mkabspath "$fn"				# <4>
	echo $ABS				# <5>
    fi
done