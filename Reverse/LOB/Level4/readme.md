# Level4

## This level's goal
- LEVEL4 (goblin -> orc) : egghunter

***

```
[goblin@localhost goblin]$ bash2
[goblin@localhost goblin]$ ls -l
total 20
-rwsr-sr-x    1 orc      orc         12567 Feb 26  2010 orc
-rw-r--r--    1 root     root          505 Mar 29  2010 orc.c
[goblin@localhost goblin]$ cat orc.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - orc
        - egghunter
*/

#include <stdio.h>
#include <stdlib.h>

extern char **environ;

main(int argc, char *argv[])
{
        char buffer[40];
        int i;

        if(argc < 2){
                printf("argv error\n");
                exit(0);
        }

        // egghunter
        for(i=0; environ[i]; i++)
                memset(environ[i], 0, strlen(environ[i]));

        if(argv[1][47] != '\xbf')
        {
                printf("stack is still your friend.\n");
                exit(0);
        }

        strcpy(buffer, argv[1]);
        printf("%s\n", buffer);
}
```

In the code, there are two conditions.
1. the egghunter seems that you cannot use env variable.
2. the retrun address's first byte should be "0xbf"

```
[goblin@localhost goblin]$ cp orc orc2
[goblin@localhost goblin]$ gdb -q orc2

(gdb) disass main
0x80485bd <main+189>:   call   0x8048440 <strcpy>
0x80485c2 <main+194>:   add    $0x8,%esp
(gdb) break *0x80485c2
(gdb) run `python -c 'print "A"*47+"\xbf"'`
Starting program: /home/goblin/orc2 `python -c 'print "A"*47+"\xbf"'`

(gdb) x/64x $esp
0xbffffac4:     0xbffffad0      0xbffffc4a      0x00000015      0x41414141
0xbffffad4:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffffae4:     0x41414141      0x41414141      0x41414141      0x41414141
0xbffffaf4:     0x41414141      0x41414141      0xbf414141      0x00000000
0xbffffb04:     0xbffffb44      0xbffffb50      0x40013868      0x00000002
0xbffffb14:     0x08048450      0x00000000      0x08048471      0x08048500
0xbffffb24:     0x00000002      0xbffffb44      0x08048390      0x0804860c
0xbffffb34:     0x4000ae60      0xbffffb3c      0x40013e90      0x00000002
0xbffffb44:     0xbffffc38      0xbffffc4a      0x00000000      0xbffffc7b
0xbffffb54:     0xbffffc9d      0xbffffca7      0xbffffcb5      0xbffffcd4
0xbffffb64:     0xbffffce3      0xbffffcfb      0xbffffd17      0xbffffd36
0xbffffb74:     0xbffffd41      0xbffffd4f      0xbffffd91      0xbffffda3
0xbffffb84:     0xbffffdb8      0xbffffdc8      0xbffffdd4      0xbffffdf2
0xbffffb94:     0xbffffdfd      0xbffffe0e      0xbffffe1f      0xbffffe27
0xbffffba4:     0x00000000      0x00000003      0x08048034      0x00000004
0xbffffbb4:     0x00000020      0x00000005      0x00000006      0x00000006
```

