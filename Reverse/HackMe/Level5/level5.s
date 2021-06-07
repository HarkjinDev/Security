// This is /usr/bin/level5's assembly code

0x0804842c <main+0>:    push   %ebp
0x0804842d <main+1>:    mov    %esp,%ebp
0x0804842f <main+3>:    sub    $0x8,%esp
0x08048432 <main+6>:    and    $0xfffffff0,%esp
0x08048435 <main+9>:    mov    $0x0,%eax
0x0804843a <main+14>:   sub    %eax,%esp
0x0804843c <main+16>:   sub    $0x8,%esp
0x0804843f <main+19>:   push   $0x180
0x08048444 <main+24>:   push   $0x8048580
0x08048449 <main+29>:   call   0x804832c <creat>
0x0804844e <main+34>:   add    $0x10,%esp
0x08048451 <main+37>:   mov    %eax,0xfffffffc(%ebp)
0x08048454 <main+40>:   cmpl   $0x0,0xfffffffc(%ebp)
0x08048458 <main+44>:   jns    0x8048484 <main+88>
0x0804845a <main+46>:   sub    $0xc,%esp
0x0804845d <main+49>:   push   $0x80485a0
0x08048462 <main+54>:   call   0x804835c <printf>
0x08048467 <main+59>:   add    $0x10,%esp
0x0804846a <main+62>:   sub    $0xc,%esp
0x0804846d <main+65>:   push   $0x8048580
0x08048472 <main+70>:   call   0x804833c <remove>
0x08048477 <main+75>:   add    $0x10,%esp
0x0804847a <main+78>:   sub    $0xc,%esp
0x0804847d <main+81>:   push   $0x0
0x0804847f <main+83>:   call   0x804836c <exit>
0x08048484 <main+88>:   sub    $0x4,%esp
0x08048487 <main+91>:   push   $0x1f
0x08048489 <main+93>:   push   $0x80485e0
0x0804848e <main+98>:   pushl  0xfffffffc(%ebp)
0x08048491 <main+101>:  call   0x804830c <write>
0x08048496 <main+106>:  add    $0x10,%esp
0x08048499 <main+109>:  sub    $0xc,%esp
0x0804849c <main+112>:  pushl  0xfffffffc(%ebp)
0x0804849f <main+115>:  call   0x804831c <close>
0x080484a4 <main+120>:  add    $0x10,%esp
0x080484a7 <main+123>:  sub    $0xc,%esp
0x080484aa <main+126>:  push   $0x8048580
0x080484af <main+131>:  call   0x804833c <remove>
0x080484b4 <main+136>:  add    $0x10,%esp
0x080484b7 <main+139>:  leave
0x080484b8 <main+140>:  ret
0x080484b9 <main+141>:  nop
0x080484ba <main+142>:  nop
0x080484bb <main+143>:  nop
