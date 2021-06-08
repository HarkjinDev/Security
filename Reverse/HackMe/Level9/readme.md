# Level9

## This level's goal

- BOF(Buffer OverFlow)

***

```
[level9@ftz level9]$ cat hint

다음은 /usr/bin/bof의 소스이다.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

main(){

  char buf2[10];
  char buf[10];

  printf("It can be overflow : ");
  fgets(buf,40,stdin);

  if ( strncmp(buf2, "go", 2) == 0 )
   {
        printf("Good Skill!\n");
        setreuid( 3010, 3010 );
        system("/bin/bash");
   }

}

이를 이용하여 level10의 권한을 얻어라.
```
