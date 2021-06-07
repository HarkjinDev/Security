// This is the restore code of level5.s

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define PERM 0x180

int main()
{
        int fd;
        char nextPass[] = "next password : what the hell\n";
        char *tempfile = "/tmp/level5.tmp;

        fd = create(tempFile, PERM);
        if(fd < 0)
        {
                printf("Can not create a temporary file.\n");
                remove(tempFile);
                exit(0);
        }
        else
        {
                write(fd, nextPass, strlen(nextPass));
                close(fd);
                remove(tempFile);
        }
        return 0;
}
