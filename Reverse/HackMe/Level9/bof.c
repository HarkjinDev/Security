#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

main(){

        char buf2[10];
        char buf[10];

        printf("It can be overflow : ");
        fgets(buf,40,stdin);
        
        # show the buffer memory address
        printf("&buf=0x%x, &buf2=0x%x, distance=0x000000%x / %d byte\n",buf, buf2, buf2-buf, buf2-buf);

        if ( strncmp(buf2, "go", 2) == 0 )
        {
                printf("Good Skill!\n");
        setreuid( 3010, 3010 );
        system("/bin/bash");
        }

}
