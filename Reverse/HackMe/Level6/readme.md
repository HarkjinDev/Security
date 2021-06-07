# Level6

## This level's goal

- singnal() function vulnerability
- singnal Control(Handling, Trap)

***
```
hint - 인포샵 bbs의 텔넷 접속 메뉴에서 많이 사용되던 해킹 방법이다.

  #####################################
  ##                                 ##
  ##         텔넷 접속 서비스        ##
  ##                                 ##
  ##                                 ##
  ##     1. 하이텔     2. 나우누리   ##
  ##     3. 천리안                   ##
  ##                                 ##
  #####################################

접속하고 싶은 bbs를 선택하세요 : 
```

```
hint - 인포샵 bbs의 텔넷 접속 메뉴에서 많이 사용되던 해킹 방법이다.

<CTRL + C>

[level6@ftz level6]$
```

```
[level6@ftz level6]$ ls -al
total 100
-rw-r--r--    1 root     root          163 Mar  5  2003 .bashrc
-rw-r--r--    1 root     root           72 Nov 23  2000 hint
-rw-r-----    1 root     level6         36 Mar 24  2000 password
drwxrwxr-x    2 root     level6       4096 Jan 14  2009 tmp
-rwxr-x---    1 root     level6      14910 Mar  5  2003 tn

[level6@ftz level6]$ cat .bashrc
# .bashrc

# User specific aliases and functions

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
export PS1="[\u@\h \W]\$ "
./tn
logout

[level6@ftz level6]$ file tn
tn: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), for GNU/Linux 2.2.5, dynamically linked (uses shared libs), not stripped

[level6@ftz level6]$ cat password
Level7 password is "come together".
```


