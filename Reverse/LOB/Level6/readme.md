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
