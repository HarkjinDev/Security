# Level8

## This level's goal
- LEVEL8 (orge -> troll) : check argc

***

```
[orge@localhost orge]$ bash2

[orge@localhost orge]$ ls -l
total 20
-rwsr-sr-x    1 troll    troll       12693 Mar  1  2010 troll
-rw-r--r--    1 root     root          772 Mar 29  2010 troll.c

[orge@localhost orge]$ cat troll.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - troll
        - check argc + argv hunter
*/

#include <stdio.h>
#include <stdlib.h>

extern char **environ;

main(int argc, char *argv[])
{
        char buffer[40];
        int i;

        // here is changed
        if(argc != 2){
                printf("argc must be two!\n");
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

        // one more!
        memset(argv[1], 0, strlen(argv[1]));
}
```

In the code, there is some changed code that you only use argv[0] and argv[1] and 
