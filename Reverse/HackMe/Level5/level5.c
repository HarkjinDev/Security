// This is the restore code of level5.s

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

main()
{
        char tmpfile[] = "/tmp/level5.tmp";
        int fd;

        fd = creat(tmpfile, 0x180);
        if (fd < 0)
        {
                printf("Can not creat a temporary file.\n");
                remove(tmpfile);
                exit(0);
        }
        else
        {
                write(fd, "next password : what the hell", 0x1f);
                close(fd);
                remove(tmpfile);
        }
        return 0;
}
