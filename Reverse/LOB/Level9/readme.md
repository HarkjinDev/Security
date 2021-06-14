# Level9

## This level's goal
- LEVEL9 (troll -> vampire) : check 0xbfff

***

```
[troll@localhost troll]$ bash2

[troll@localhost troll]$ ls -l
total 16
-rwsr-sr-x    1 vampire  vampire     12103 Mar  2  2010 vampire
-rw-r--r--    1 root     root          550 Mar 29  2010 vampire.c

[troll@localhost troll]$ cat vampire.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - vampire
        - check 0xbfff
*/

#include <stdio.h>
#include <stdlib.h>

main(int argc, char *argv[])
{
        char buffer[40];

        if(argc < 2){
                printf("argv error\n");
                exit(0);
        }

        if(argv[1][47] != '\xbf')
        {
                printf("stack is still your friend.\n");
                exit(0);
        }

        // here is changed!
        if(argv[1][46] == '\xff')
        {
                printf("but it's not forever\n");
                exit(0);
        }

        strcpy(buffer, argv[1]);
        printf("%s\n", buffer);
}
```

