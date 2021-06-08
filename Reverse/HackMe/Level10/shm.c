// This is getting the value of shared memory

#include <stdio.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#define BUFFSIZE 1024
#define KEY 7530

int main()
{
        int shm_id;
        void *shm_addr=(void *)0;
        char buf[BUFFSIZE];

        // shmget() : Creates share memory
        // key_t key : the key variable for reading share memory
        // (int size) : memory size
        // 0666 : share memory permission
        shm_id = shmget(KEY, BUFFSIZE, 0666);

        // shmat() : Attach the created share memory
        shm_addr = shmat(shm_id, (void *)0, 0);
        
        // memcpy() : Copy the value of memory
        memcpy(buf, shm_addr, BUFFSIZE);
        printf("%s", buf);

        // shmdt() : Detach the connected share memory
        shmdt(shm_addr);

        return 0;
}
