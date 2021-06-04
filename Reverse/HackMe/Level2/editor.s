# This is /usr/bin/editor's assembly code

0x08048360 <main+0>:    push   %ebp
0x08048361 <main+1>:    mov    %esp,%ebp
0x08048363 <main+3>:    sub    $0x8,%esp
0x08048366 <main+6>:    and    $0xfffffff0,%esp
0x08048369 <main+9>:    mov    $0x0,%eax
0x0804836e <main+14>:   sub    %eax,%esp
0x08048370 <main+16>:   sub    $0x8,%esp
0x08048373 <main+19>:   push   $0xbbb
0x08048378 <main+24>:   push   $0xbbb
0x0804837d <main+29>:   call   0x80482a0 <setreuid>
0x08048382 <main+34>:   add    $0x10,%esp
0x08048385 <main+37>:   sub    $0xc,%esp
0x08048388 <main+40>:   push   $0x8048444
0x0804838d <main+45>:   call   0x8048280 <system>
0x08048392 <main+50>:   add    $0x10,%esp
0x08048395 <main+53>:   leave
0x08048396 <main+54>:   ret
0x08048397 <main+55>:   nop
