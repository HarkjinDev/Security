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
{ int crap;
  int check;
  char buf[20];
  fgets(buf,45,stdin);
  if (check==0xdeadbeef)
   {
     setreuid(3095,3095);
     system("/bin/sh");
   }
}
```
