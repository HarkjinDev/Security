# Level20 (Final Level)

## This level's goal
-

***

```
[level20@ftz level20]$ ls -l
-rwsr-sr-x    1 clear    clear       11777 Jun 18  2008 attackme
-rw-r-----    1 root     level20       133 May 13  2002 hint

[level20@ftz level20]$ cat hint

#include <stdio.h>
main(int argc,char **argv)
{ char bleh[80];
  setreuid(3101,3101);
  fgets(bleh,79,stdin);
  printf(bleh);
}
```

