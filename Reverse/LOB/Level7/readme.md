# Level7

# This level's goal
- LEVEL7 (darkelf -> orge) : check argv[0]

***

```
[darkelf@localhost darkelf]$ bash2

[darkelf@localhost darkelf]$ ls -l
total 20
-rwsr-sr-x    1 orge     orge        12700 Mar  1  2010 orge
-rw-r--r--    1 root     root          800 Mar 29  2010 orge.c

[darkelf@localhost darkelf]$ cat orge.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - orge
        - check argv[0]
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

        // here is changed!
        if(strlen(argv[0]) != 77){
                printf("argv[0] error\n");
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
