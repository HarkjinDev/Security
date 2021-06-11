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

