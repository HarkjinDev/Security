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
