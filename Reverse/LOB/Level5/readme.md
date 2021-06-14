# Level5

## This level's goal
- LEVEL5 (orc -> wolfman) : egghunter + bufferhunter

***

```
[orc@localhost orc]$ bash2

[orc@localhost orc]$ ls -l
total 20
-rwsr-sr-x    1 wolfman  wolfman     12587 Feb 26  2010 wolfman
-rw-r--r--    1 root     root          581 Mar 29  2010 wolfman.c

[orc@localhost orc]$ cat wolfman.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - wolfman
        - egghunter + buffer hunter
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

        // buffer hunter
        memset(buffer, 0, 40);
}
```
