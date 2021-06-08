// This is /usr/bin/bof's assembly code

0x08048420 <main+0>:    push   %ebp
0x08048421 <main+1>:    mov    %esp,%ebp
0x08048423 <main+3>:    sub    $0x28,%esp
0x08048426 <main+6>:    and    $0xfffffff0,%esp
0x08048429 <main+9>:    mov    $0x0,%eax
0x0804842e <main+14>:   sub    %eax,%esp
0x08048430 <main+16>:   sub    $0xc,%esp
0x08048433 <main+19>:   push   $0x8048554
0x08048438 <main+24>:   call   0x8048350 <printf>
0x0804843d <main+29>:   add    $0x10,%esp
0x08048440 <main+32>:   sub    $0x4,%esp
0x08048443 <main+35>:   pushl  0x8049698
0x08048449 <main+41>:   push   $0x28
0x0804844b <main+43>:   lea    0xffffffd8(%ebp),%eax
0x0804844e <main+46>:   push   %eax
0x0804844f <main+47>:   call   0x8048320 <fgets>
0x08048454 <main+52>:   add    $0x10,%esp
0x08048457 <main+55>:   sub    $0x4,%esp
0x0804845a <main+58>:   push   $0x2
0x0804845c <main+60>:   push   $0x804856a
0x08048461 <main+65>:   lea    0xffffffe8(%ebp),%eax
0x08048464 <main+68>:   push   %eax
0x08048465 <main+69>:   call   0x8048330 <strncmp>
0x0804846a <main+74>:   add    $0x10,%esp
0x0804846d <main+77>:   test   %eax,%eax
0x0804846f <main+79>:   jne    0x80484a6 <main+134>
0x08048471 <main+81>:   sub    $0xc,%esp
0x08048474 <main+84>:   push   $0x804856d
0x08048479 <main+89>:   call   0x8048350 <printf>
0x0804847e <main+94>:   add    $0x10,%esp
0x08048481 <main+97>:   sub    $0x8,%esp
0x08048484 <main+100>:  push   $0xbc2
0x08048489 <main+105>:  push   $0xbc2
0x0804848e <main+110>:  call   0x8048360 <setreuid>
0x08048493 <main+115>:  add    $0x10,%esp
0x08048496 <main+118>:  sub    $0xc,%esp
0x08048499 <main+121>:  push   $0x804857a
0x0804849e <main+126>:  call   0x8048310 <system>
0x080484a3 <main+131>:  add    $0x10,%esp
0x080484a6 <main+134>:  leave
0x080484a7 <main+135>:  ret
