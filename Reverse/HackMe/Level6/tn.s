// This is tn's assembly code

0x080484f8 <main+0>:    push   %ebp
0x080484f9 <main+1>:    mov    %esp,%ebp
0x080484fb <main+3>:    sub    $0x8,%esp
0x080484fe <main+6>:    sub    $0xc,%esp
0x08048501 <main+9>:    push   $0x80486f2   // cat hint
0x08048506 <main+14>:   call   0x8048384 <system>
0x0804850b <main+19>:   add    $0x10,%esp
0x0804850e <main+22>:   call   0x8048354 <getchar>
0x08048513 <main+27>:   sub    $0xc,%esp
0x08048516 <main+30>:   push   $0x80486fb   // clear
0x0804851b <main+35>:   call   0x8048384 <system>
0x08048520 <main+40>:   add    $0x10,%esp
0x08048523 <main+43>:   sub    $0xc,%esp
0x08048526 <main+46>:   push   $0x8048720
0x0804852b <main+51>:   call   0x80483c4 <printf>
0x08048530 <main+56>:   add    $0x10,%esp
0x08048533 <main+59>:   sub    $0xc,%esp
0x08048536 <main+62>:   push   $0x8048760
0x0804853b <main+67>:   call   0x80483c4 <printf>
0x08048540 <main+72>:   add    $0x10,%esp
0x08048543 <main+75>:   sub    $0xc,%esp
0x08048546 <main+78>:   push   $0x80487a0
0x0804854b <main+83>:   call   0x80483c4 <printf>
0x08048550 <main+88>:   add    $0x10,%esp
0x08048553 <main+91>:   sub    $0xc,%esp
0x08048556 <main+94>:   push   $0x8048760
0x0804855b <main+99>:   call   0x80483c4 <printf>
0x08048560 <main+104>:  add    $0x10,%esp
0x08048563 <main+107>:  sub    $0xc,%esp
0x08048566 <main+110>:  push   $0x8048760
0x0804856b <main+115>:  call   0x80483c4 <printf>
0x08048570 <main+120>:  add    $0x10,%esp
0x08048573 <main+123>:  sub    $0xc,%esp
0x08048576 <main+126>:  push   $0x80487e0
0x0804857b <main+131>:  call   0x80483c4 <printf>
0x08048580 <main+136>:  add    $0x10,%esp
0x08048583 <main+139>:  sub    $0xc,%esp
0x08048586 <main+142>:  push   $0x8048820
0x0804858b <main+147>:  call   0x80483c4 <printf>
0x08048590 <main+152>:  add    $0x10,%esp
0x08048593 <main+155>:  sub    $0xc,%esp
0x08048596 <main+158>:  push   $0x8048760
0x0804859b <main+163>:  call   0x80483c4 <printf>
0x080485a0 <main+168>:  add    $0x10,%esp
0x080485a3 <main+171>:  sub    $0xc,%esp
0x080485a6 <main+174>:  push   $0x8048860
0x080485ab <main+179>:  call   0x80483c4 <printf>
0x080485b0 <main+184>:  add    $0x10,%esp
0x080485b3 <main+187>:  sub    $0x8,%esp
0x080485b6 <main+190>:  push   $0x80484e0   // <sig_func>
0x080485bb <main+195>:  push   $0x2
0x080485bd <main+197>:  call   0x8048374 <signal>
0x080485c2 <main+202>:  add    $0x10,%esp
0x080485c5 <main+205>:  sub    $0xc,%esp
0x080485c8 <main+208>:  push   $0x80488a0
0x080485cd <main+213>:  call   0x80483c4 <printf>
0x080485d2 <main+218>:  add    $0x10,%esp
0x080485d5 <main+221>:  sub    $0x8,%esp
0x080485d8 <main+224>:  lea    0xfffffffc(%ebp),%eax
0x080485db <main+227>:  push   %eax
0x080485dc <main+228>:  push   $0x80488c3   // "%d"
0x080485e1 <main+233>:  call   0x8048394 <scanf>
0x080485e6 <main+238>:  add    $0x10,%esp
0x080485e9 <main+241>:  cmpl   $0x1,0xfffffffc(%ebp)
0x080485ed <main+245>:  jne    0x80485ff <main+263>
0x080485ef <main+247>:  sub    $0xc,%esp
0x080485f2 <main+250>:  push   $0x80488c6
0x080485f7 <main+255>:  call   0x8048384 <system>
0x080485fc <main+260>:  add    $0x10,%esp
0x080485ff <main+263>:  cmpl   $0x2,0xfffffffc(%ebp)
0x08048603 <main+267>:  jne    0x8048615 <main+285>
0x08048605 <main+269>:  sub    $0xc,%esp
0x08048608 <main+272>:  push   $0x80488db
0x0804860d <main+277>:  call   0x8048384 <system>
0x08048612 <main+282>:  add    $0x10,%esp
0x08048615 <main+285>:  cmpl   $0x3,0xfffffffc(%ebp)
0x08048619 <main+289>:  jne    0x804862b <main+307>
0x0804861b <main+291>:  sub    $0xc,%esp
0x0804861e <main+294>:  push   $0x80488f1
0x08048623 <main+299>:  call   0x8048384 <system>
0x08048628 <main+304>:  add    $0x10,%esp
0x0804862b <main+307>:  cmpl   $0x1,0xfffffffc(%ebp)
0x0804862f <main+311>:  je     0x804864d <main+341>
0x08048631 <main+313>:  cmpl   $0x2,0xfffffffc(%ebp)
0x08048635 <main+317>:  je     0x804864d <main+341>
0x08048637 <main+319>:  cmpl   $0x3,0xfffffffc(%ebp)
0x0804863b <main+323>:  je     0x804864d <main+341>
0x0804863d <main+325>:  sub    $0xc,%esp
0x08048640 <main+328>:  push   $0x8048920
0x08048645 <main+333>:  call   0x80483c4 <printf>
0x0804864a <main+338>:  add    $0x10,%esp
0x0804864d <main+341>:  leave
0x0804864e <main+342>:  ret
0x0804864f <main+343>:  nop
