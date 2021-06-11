# Level1

## This level's goal
- LEVEL1 (gate -> gremlin) : Simple BOF

***

```
[gate@localhost gate]$ ls -l
-rwsr-sr-x    1 gremlin  gremlin     11987 Feb 26  2010 gremlin
-rw-rw-r--    1 gate     gate          272 Mar 29  2010 gremlin.c

[gate@localhost gate]$ cat gremlin.c
/*
        The Lord of the BOF : The Fellowship of the BOF
        - gremlin
        - simple BOF
*/

int main(int argc, char *argv[])
{
    char buffer[256];
    if(argc < 2){
        printf("argv error\n");
        exit(0);
    }
    strcpy(buffer, argv[1]);
    printf("%s\n", buffer);
}
```
