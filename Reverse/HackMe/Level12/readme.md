# Level12

## This level's goal
- BOF(Buffer Overflow)
- Stack Buffer Overflow

***

```
[level12@ftz level12]$ cat hint
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main( void )
{
        char str[256];

        setreuid( 3093, 3093 );
        printf( "문장을 입력하세요.\n" );
        gets( str );
        printf( "%s\n", str );
}
```
