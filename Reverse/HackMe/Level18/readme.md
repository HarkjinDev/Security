# Level18

## This level's goal
- Pointer

***

```
[level18@ftz level18]$ ls -l
-rwsr-x---    1 level19  level18      6225 Jan 25  1999 attackme
-rw-r-----    1 root     level18      1272 Jan 25  1999 hint

[level18@ftz level18]$ cat hint

#include <stdio.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
void shellout(void);
int main()
{
  char string[100];
  int check;
  int x = 0;
  int count = 0;
  fd_set fds;
  printf("Enter your command: ");
  fflush(stdout);
  while(1)
    {
      if(count >= 100)
        printf("what are you trying to do?\n");
      if(check == 0xdeadbeef)
        shellout();
      else
        {
          FD_ZERO(&fds);
          FD_SET(STDIN_FILENO,&fds);

          if(select(FD_SETSIZE, &fds, NULL, NULL, NULL) >= 1)
            {
              if(FD_ISSET(fileno(stdin),&fds))
                {
                  read(fileno(stdin),&x,1);
                  switch(x)
                    {
                      case '\r':
                      case '\n':
                        printf("\a");
                        break;
                      case 0x08:
                        count--;
                        printf("\b \b");
                        break;
                      default:
                        string[count] = x;
                        count++;
                        break;
                    }
                }
            }
        }
    }
}

void shellout(void)
{
  setreuid(3099,3099);
  execl("/bin/sh","sh",NULL);
}
```

```
[level18@ftz tmp]$ gdb /home/level18/attackme
(gdb) disass main
0x08048553 <main+3>:    sub    $0x100,%esp

[level18@ftz tmp]$ cat distance.c

#include <stdio.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
void shellout(void);
int main()
{
  char string[100];
  int check;
  int x = 0;
  int count = 0;
  fd_set fds;
  printf(" &string:%p\n &check:%p\n &x:%p\n &count:%p\n &fds:%p\n", string, &check, &x, &count, &fds);
  printf(" fds's size : %d\n", sizeof(fds));
}

[level18@ftz tmp]$ gcc distance.c -o distance
[level18@ftz tmp]$ ./distance
 &string: 0xbfffe8e0
 &check:  0xbfffe8dc
 &x:      0xbfffe8d8
 &count:  0xbfffe8d4
 &fds:    0xbfffe850
 fds's size : 128
```

As above, total size(x100) means 256 bytes.

&string - &check = 0xbfffefe0 - 0xbfffefdc = 0x4 (4bytes)   
&check  - &x     = 0xbfffefdc - 0xbfffefd8 = 0x4 (4bytes)   
&x      - &count = 0xbfffefd8 - 0xbfffefd4 = 0x4 (4bytes)   
&count  - &fds   = 0xbfffefd4 - 0xbfffef50 = 0x84(132bytes)   
dummy1 = 132bytes - 128bytes   
dummy2 = 265 - ( 128 + 4 + 4 + 4 + 100 ) = 16bytes - 4bytes(SFP) = 12bytes

fds(128bytes) + dummy1(4bytes) + count(4bytes) + x(4bytes) + string(100bytes) + dummy2(12bytes) + SFP(4bytes) + RET(4bytes)
