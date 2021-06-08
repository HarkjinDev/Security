# Level11

## This level's goal

- FSB(Format String Bug)

***

```
[level11@ftz level11]$ ls -l
total 28
-rwsr-x---    1 level12  level11     13733 Mar  8  2003 attackme
-rw-r-----    1 root     level11       168 Mar  8  2003 hint
drwxr-xr-x    2 root     level11      4096 Feb 24  2002 public_html
drwxrwxr-x    2 root     level11      4096 Jan 14  2009 tmp

[level11@ftz level11]$ cat hint

#include <stdio.h>
#include <stdlib.h>

int main( int argc, char *argv[] )
{
        char str[256];

        setreuid( 3092, 3092 );
        strcpy( str, argv[1] );
        printf( str );
}
```

The hint seems the vulnerability of FSB and BOF   
I will exploit with FSB

```
[level11@ftz level11]$ ./attackme
Segmentation fault
```

This seems that Segmentation falut will be printed if there is no argument and then the argv[1] is the value of garbage.
