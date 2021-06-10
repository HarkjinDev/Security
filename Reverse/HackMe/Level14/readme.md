# Level14

## This level's goal
- routine

***

```
[level14@ftz level14]$ ls -l
-rwsr-x---    1 level15  level14     13801 Dec 10  2002 attackme
-rw-r-----    1 root     level14       346 Dec 10  2002 hint

[level14@ftz level14]$ cat hint 

레벨14 이후로는 mainsource의 문제를 그대로 가져왔습니다.
(After level14, brought just main source's problem.)
버퍼 오버플로우, 포맷스트링을 학습하는데는 이 문제들이 최고의 효과를 가져다줍니다.
(those problems are the best effect for learning formoat strings and buffer overflow)

#include <stdio.h>
#include <unistd.h>

main()
{ 
  int crap;
  int check;
  char buf[20];
  fgets(buf,45,stdin);
  if (check==0xdeadbeef)
   {
     setreuid(3095,3095);
     system("/bin/sh");
   }
}

[level14@ftz level14]$ gdb -q attackme
(gdb) disass main
0x08048493 <main+3>:    sub    $0x38,%esp
```

0x38 means 56 bytes, and I need to get more information of memory size.

```
[level14@ftz tmp]$ cat distance.c

#include <stdio.h>
#include <unistd.h>

int main()
{
        int crap;
        int check;
        char buf[20];

        fgets(buf,45,stdin);
        if(check == 0xdeadbeef)
        {
                setreuid(3095,3095);
                system("/bin/sh");
        }
        printf("Input is : %s\n &buf : %p\n &check: %p\n &crap : %p\n", buf, buf, &check, &crap);
}

[level14@ftz tmp]$ gcc distance.c -o distance
[level14@ftz tmp]$ ./distance
AAAA
Input is : AAAA

&buf :   0xbffff8a0
&check:  0xbffff8c8
&crap :  0xbffff8cc
```

As above, I can understand the memory size.

Between buff and check : 0xbffff8c8 - 0xbffff8a0 = 0x00000028 (40 bytes)   
Between chek and crap  : 0xbffff8cc - 0xbffff8c8 = 0x00000004 (4bytes)

char buf(20 bytes) + dummy(20bytes) + check(4bytes) + crap(4bytes) + dummy(8bytes) + SFP(4bytes) + RET(4bytes)





