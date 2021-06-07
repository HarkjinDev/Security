// This is the conversion of the singal code to binary and decimal and ascii code
// and get the level8's password

#include <stdio.h>

int binToInt(char *bin)
{
    int i=0;
    int count=0;

    while(bin[count])
    i=(i << 1) | (bin[count++] - '0');

    return i;
}

int main()
{
    char *bin="--_--_- --____- ---_-__ --__-_- ";
    char *ptr=bin;
    char dec[32];
    int i;
    int decimal[4];
    char cmd[100];

    // signal code
    printf("Reserved signals : %s\n", bin);

    // binary code
    for(i=0; i<strlen(bin); i++)
    {
        if      (*ptr == '-') dec[i]='1';
        else if (*ptr == '_') dec[i]='0';
        else if (*ptr == ' ') dec[i]='\0';
        ptr++;
    }
    printf("Changed binary   : %s %s %s %s \n", &dec[0], &dec[8], &dec[16], &dec[24]);
    
    // decimal code
    for(i=0; i<4; i++) decimal[i]=binToInt(&dec[i*8]);
    printf("Changed decimal  : %d %d %d %d\n", decimal[0], decimal[1], decimal[2], decimal[3]);

    // ascii code
    printf("Changed ascii    : %c %c %c %c\n", decimal[0], decimal[1], decimal[2], decimal[3]);

    // attack code
    sprintf(cmd, "(printf \"%c%c%c%c\n\" ; cat) | /bin/level7", decimal[0], decimal[1], decimal[2], decimal[3]);
    system(cmd);

    return 0;
}


