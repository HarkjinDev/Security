// This is the restore code of level10.s

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int shmid;
char *text;

int main( void ) {

        shmid = shmget((key_t)7530, 1028, 1666 | IPC_CREAT);
        text = shmat(shmid, (void *)0, 0);

        strcpy(text,"멍멍: level11의 패스워드는?\n구타: what!@#$?\n");

}
