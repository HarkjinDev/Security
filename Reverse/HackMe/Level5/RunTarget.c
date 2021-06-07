#include <unistd.h>

// /usr/bin/level5 will make /tmp/level5.tmp

int main(void)
{
        int i;
        for(i=0; i<10; i++)
        {
                system("/usr/bin/level5 &");
        }
}
