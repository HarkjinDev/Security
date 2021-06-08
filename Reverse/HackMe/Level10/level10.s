// This is /home/level10/program/level10's assembly code

0x08048470 <main+0>:    push   %ebp
0x08048471 <main+1>:    mov    %esp,%ebp
0x08048473 <main+3>:    sub    $0x8,%esp
0x08048476 <main+6>:    sub    $0x4,%esp
0x08048479 <main+9>:    push   $0x3b6		        // 3) OCT 1666
0x0804847e <main+14>:   push   $0x404		        // 2) DEC 1028
0x08048483 <main+19>:   push   $0x1d6a		        // 1) DEC 7530
0x08048488 <main+24>:   call   0x804832c <shmget>	// shmget(7530,1028,1666)
0x0804848d <main+29>:   add    $0x10,%esp
0x08048490 <main+32>:   mov    %eax,%eax
0x08048492 <main+34>:   mov    %eax,0x80496d0           // int shmid = shmget(7530,1028,1666)
0x08048497 <main+39>:   sub    $0x4,%esp
0x0804849a <main+42>:   push   $0x0		        // 3) 0
0x0804849c <main+44>:   push   $0x0		        // 2) 0
0x0804849e <main+46>:   pushl  0x80496d0		// 1) shmid
0x080484a4 <main+52>:   call   0x804834c <shmat>	// shmat(shmid,0,0)
0x080484a9 <main+57>:   add    $0x10,%esp
0x080484ac <main+60>:   mov    %eax,0x80496cc           // char text = shmat(shmid,0,0)
0x080484b1 <main+65>:   sub    $0x8,%esp
0x080484b4 <main+68>:   push   $0x8048560		// "멍멍: level11의 패스워드는?\n구타: what!@#$?\n"
0x080484b9 <main+73>:   pushl  0x80496cc		// text
0x080484bf <main+79>:   call   0x804835c <strcpy>	// strcpy(text, "멍멍: level11의 패스워드는?\n구타: what!@#$?\n")
0x080484c4 <main+84>:   add    $0x10,%esp
0x080484c7 <main+87>:   leave
0x080484c8 <main+88>:   ret
0x080484c9 <main+89>:   lea    0x0(%esi),%esi
0x080484cc <main+92>:   nop
0x080484cd <main+93>:   nop
0x080484ce <main+94>:   nop
0x080484cf <main+95>:   nop
