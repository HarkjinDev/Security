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
