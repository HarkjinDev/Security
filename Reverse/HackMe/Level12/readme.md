# Level12

## This level's goal
- BOF(Buffer Overflow)
- Stack Buffer Overflow

***

```
[level12@ftz level12]$ cat hint

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( void )
{
        char str[256];

        setreuid( 3093, 3093 );
        printf( "문장을 입력하세요.\n" );
        gets( str );
        printf( "%s\n", str );
}
```

```
[level12@ftz level12]$ gdb -q attackme
(gdb) disas main
0x08048473 <main+3>:    sub    $0x108,%esp
0x080484bf <main+79>:   call   0x804834c <printf>
(gdb) b *0x080484bf
(gdb) run
Starting program: /home/level12/tmp/attackme
문장을 입력하시오.
AAAAAAAA

Breakpoint 1, 0x080484bf in main ()
(gdb) x/72x $esp
0xbffff450:     0x0804854c      0xbffff460      0xbffff480      0x00000001
0xbffff460:     0x41414141      0x41414141      0x00000000      0x078e530f
0xbffff470:     0xbffff510      0x40015a38      0x0029656e      0x00000000
0xbffff480:     0x4200b894      0x400160b0      0x00000000      0x00000000
0xbffff490:     0x00000000      0x00000000      0x00000000      0x4000807f
0xbffff4a0:     0x4001582c      0x00001f1f      0xbffff4d0      0xbffff4fc
0xbffff4b0:     0x4000be03      0x4001624c      0x00000000      0x0177ff8e
0xbffff4c0:     0x4000807f      0x4001582c      0x00000059      0x40015a38
0xbffff4d0:     0xbffff520      0x4000be03      0x40015bd4      0x40016380
0xbffff4e0:     0x00000001      0x00000000      0x4200dba3      0x420069e4
0xbffff4f0:     0x42130a14      0xbffffc26      0xbffff5b4      0xbffff534
0xbffff500:     0x4000bcc0      0x08049648      0x00000001      0x08048249
0xbffff510:     0x4210fd3c      0x42130a14      0xbffff538      0x4210fdf6
0xbffff520:     0x08049560      0x08049664      0x00000000      0x00000000
0xbffff530:     0x4210fdc0      0x42130a14      0xbffff558      0x08048451
0xbffff540:     0x08049560      0x08049664      0x4001582c      0x0804839e
0xbffff550:     0x080482e4      0x42130a14      0xbffff568      0x080482fa
0xbffff560:     0x4200af84      0x42130a14      0xbffff588      0x42015574
(gdb) x/x 0xbffff588
0xbffff588:     0x00000000
(gdb) x/s 0x42015574
0x42015574 <__libc_start_main+228>:      "\211ÁëX1É\213\203\204#"
```
