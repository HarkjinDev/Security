#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
        char *str;
        char *password="mate";

        str = malloc(0x64);
        printf("Insert The Password : ");
        fgets(str, 0x64, stdin);

        if (strncmp(str, password, 0x4)==0)
        {
                printf("\nCongratulation! next password is \"break the world\".\n\n");
                exit(0);
        }
        system("cat /bin/wrong.txt");
}
