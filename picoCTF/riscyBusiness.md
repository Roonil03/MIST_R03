# <a href="https://play.picoctf.org/practice/challenge/219">riscy business</a>


### First Strategy
The first thing that I did after getting the raw RISC File was trying to run it through Ghidra's decompiler and Code Browser to see what all I could pick up.

After three rounds of analysis, this was the defined strings that I could pick up:
```
.comment::00000000	GCC: (Arch Linux Repositories) 10.2.0	u8"GCC: (Arch Linux Repositories) 10.2.0"	utf8
.shstrtab::00000001	.shstrtab	u8".shstrtab"	utf8
.shstrtab::0000000b	.text	u8".text"	utf8
.shstrtab::00000011	.rodata	u8".rodata"	utf8
.shstrtab::00000019	.comment	u8".comment"	utf8
.shstrtab::00000022	.riscv.attributes	u8".riscv.attributes"	utf8
00010001	ELF	"ELF"	ds
00010248	You've gotten yourself into some riscy business...
Got yourself a flag for me?
> 	"You've gotten yourself into some riscy business...\nGot yourself a flag for me?\n> "	ds
000102a0	You need to take some more riscs than that.
	"You need to take some more riscs than that.\n"	ds
000102d0	That was a bit too riscy for me!
	"That was a bit too riscy for me!\n"	ds
000102f8	Success!
	"Success!\n"	ds
```

I then asked Perplexity to use it's decompiling feature to convert the assembly decompiled into a readable C, which code me this phrase:
```C
#include <stdio.h>
#include <string.h>

// Simplified from Ghidra's decompilation of main()
int main() {
    char input[64];
    char scrambled_flag[65] = { /* Extracted from memory */ };
    
    printf("Enter flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0; // Remove newline

    // Scramble input and compare
    for (int i = 0; i < 64; i++) {
        input[i] = ((input[i] << 4) | (input[i] >> 4)) & 0xFF; // Scramble step
    }

    if (memcmp(input, scrambled_flag, 64) == 0) {
        puts("Correct!");
    } else {
        puts("Incorrect!");
    }
    return 0;
}
```

So there's definitely some scrambling that is taking place. Looking more into the code on Ghidra, I found this and promptly added it to the C code as well:
```C
#include <stdio.h>
#include <string.h>

// Reconstructed from dynamic analysis
const char scrambled_flag[65] = {
    0x34, 0x6e, 0x79, 0x30, 0x34, 0x5f, 0x67, 0x30, 
    0x74, 0x5f, 0x72, 0x31, 0x73, 0x63, 0x76, 0x5f,
    0x68, 0x34, 0x72, 0x64, 0x77, 0x34, 0x72, 0x33,
    0x3f, 0x5f, 0x4c, 0x47, 0x55, 0x66, 0x77, 0x6c,
    0x38, 0x78, 0x79, 0x4d, 0x55, 0x6c, 0x70, 0x67,
    0x76, 0x7d, 0x00
};

void scramble(char *str) {
    for (int i = 0; i < 64; i++) {
        str[i] = ((str[i] << 4) | (str[i] >> 4)) & 0xFF;
    }
}

int main() {
    char input[65];
    printf("Enter flag: ");
    fgets(input, 65, stdin);
    input[strcspn(input, "\n")] = 0;
    
    scramble(input);
    
    if (strncmp(input, scrambled_flag, 64) == 0) {
        puts("Correct!");
    } else {
        puts("Incorrect!");
    }
    return 0;
}
```

It seemed that I would be needing some other tools as well to solve this problem. Thus, I installed qemu and gdb to make sure that I can work with this raw file...
```
sudo apt install qemu-user gdb-multiarch
```

After installing, I ran the commands:
```
qemu-riscv64 -g 1234 riscy & gdb-multiarch -q riscy -ex "target remote :1234" -ex "b *0x101c0" -ex "c"
```
and this was what happened:
```
[1] 20331
Reading symbols from riscy...
(No debugging symbols found in riscy)
Remote debugging using :1234
BFD: warning: system-supplied DSO at 0x2aaaab2ac000 has a corrupt string table index
0x0000000000010112 in ?? ()
Breakpoint 1 at 0x101c0
Continuing.
You've gotten yourself into some riscy business...
Got yourself a flag for me?
> x/64xb $a5



^C^[:q




^[^[^[^[^[

                                                                                                                        
^CThe target is not responding to interrupt requests.
Stop debugging it? (y or n) y
Disconnected from target.
(gdb) q

[1]+  Stopped                 qemu-riscv64 -g 1234 riscy
```

This was certainly irritating.
Nothing so far is working... The code is also not decompiling into something that I can use.

This is certainly a really good challenge.

I'll look into it again after some time has passed.

### Second Strategy

I tried reading the file on VSC using the normal text editor to give me this:
```
ELF          �         @       �         @ 8  @                                                  ��s   �G� 3� # � ����*��F�G 3���H �.�G ;����*�C ����h�# �����G�G'w�# �*�F ������ ����� �� # � ��#�� :�E ��	q���������� E�  ��Es   �G$ � )H�������
"�G��c��E��� 3��@s   %�M��� 	E�  ���s   E���G�ч�!F��� ����&��I	 � ��_�	�ɩ ��$A�9�����  ���  ��� � ��c������ E�  ���%Fs   E��� E�  ���
s   E����  �u�����D�4�:_P�g�:�oP�Ic�6ӓdFc��:Z�>@�  H
    You've gotten yourself into some riscy business...
Got yourself a flag for me?
>        You need to take some more riscs than that.
    That was a bit too riscy for me!
       Success!
 GCC: (Arch Linux Repositories) 10.2.0 A4   riscv *   rv64i2p0_m2p0_a2p0_f2p0_d2p0_c2p0  .shstrtab .text .rodata .comment .riscv.attributes                                                                                     x      x       �                                                     �                                    0                     &                             "     p                (      5                                                    ]      4                              
```
That was a lot of garbled by mess, but at least now I can come to know certain things about this data. 
There are some strings that are visible and are giving an output.

I then checked what could be debugged in this code:
```(gdb) run
Starting program: /home/roonil03/Downloads/riscy_debug 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Enter flag: x/64xb $a5
Incorrect!
[Inferior 1 (process 21599) exited normally]
(gdb) break main
Breakpoint 2 at 0x555555555266: file smth.c, line 12.
(gdb) run
Starting program: /home/roonil03/Downloads/riscy_debug 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 2, main () at smth.c:12
12      int main() {
(gdb) next
14          const char flag[65] = {
(gdb) next
23          printf("Enter flag: ");
(gdb) next
24          fgets(input, sizeof(input), stdin);
(gdb) next
Enter flag: something
25          input[strcspn(input, "\n")] = 0; // Remove newline
(gdb) next
27          scramble(input);
(gdb) next
29          if (strcmp(input, flag) == 0) {
(gdb) next
32              printf("Incorrect!\n");
(gdb) next
Incorrect!
35          return 0;
(gdb) next
36      }
(gdb) next
__libc_start_call_main (main=main@entry=0x555555555257 <main>, argc=argc@entry=1, argv=argv@entry=0x7fffffffdaf8) at ../sysdeps/nptl/libc_start_call_main.h:74
warning: 74     ../sysdeps/nptl/libc_start_call_main.h: No such file or directory
(gdb) next
[Inferior 1 (process 21737) exited normally]
(gdb) next
The program is not being run.
(gdb) break scramble
Breakpoint 3 at 0x5555555551f5: file smth.c, line 6.
(gdb) run
Starting program: /home/roonil03/Downloads/riscy_debug 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 2, main () at smth.c:12
12      int main() {
(gdb) next
14          const char flag[65] = {
(gdb) next
23          printf("Enter flag: ");
(gdb) next
24          fgets(input, sizeof(input), stdin);
(gdb) next
Enter flag: picoCTF{}
25          input[strcspn(input, "\n")] = 0; // Remove newline
(gdb) next
27          scramble(input);
(gdb) next

Breakpoint 3, scramble (str=0x7fffffffd940 "picoCTF{}") at smth.c:6
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) next
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) next
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) next
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) next
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) next
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) next
6           for (int i = 0; str[i]; i++) {
(gdb) next
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) 
6           for (int i = 0; str[i]; i++) {
(gdb) 
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) 
6           for (int i = 0; str[i]; i++) {
(gdb) 
8               str[i] = (str[i] << 4) | (str[i] >> 4);
(gdb) 
6           for (int i = 0; str[i]; i++) {
(gdb) 
10      }
(gdb) 
main () at smth.c:29
29          if (strcmp(input, flag) == 0) {
(gdb) 
32              printf("Incorrect!\n");
(gdb) 
Incorrect!
35          return 0;
(gdb) 
36      }
(gdb) 
__libc_start_call_main (main=main@entry=0x555555555257 <main>, argc=argc@entry=1, argv=argv@entry=0x7fffffffdaf8) at ../sysdeps/nptl/libc_start_call_main.h:74
warning: 74     ../sysdeps/nptl/libc_start_call_main.h: No such file or directory
```

This was what I got from it.  
This got me thinking as to how I could solve this one.

This was certainly an apporach that I could. Thus, I chose to take a break from this problem for sometime, and solve it later in the day.

### Third Strategy
It was using the gdb debugger to help in figuring out how exactly the code works.

And this time, I referred some documentation and came prepared so that I could view and see what the actual flag was.

```
(gdb) print (char*)flag
$1 = 0x7fffffffd980 "4ny04_g0t_r1scv_h4rdw4r3?_LGUfwl8xyMUlpgv}"
```
And, this was the biggest hit.

While debugging, it is evident what is going on with the characters:
```
6           for (int i = 0; str[i]; i++) {
(gdb) 
8               str[i] = (str[i] << 4) | (str[i] >> 4);
```
Since each character is 8 bits in length, this basically switches the hex positions.

`45` -> `(450) | (04)` -> `54`
> Since the first bit in 450 is gone due to only 1 byte limit.

Thus, with this, it was just a task of switching all the bits arou-...
```Go
package main

import "fmt"

func main() {
	s := []byte("4ny04_g0t_r1scv_h4rdw4r3?_LGUfwl8xyMUlpgv}")
	for i := 0; i < len(s); i++ {
		s[i] = ((s[i] << 4) | (s[i] >> 4))
	}
	fmt.Print(string(s))
}
```
```
C�C�vG�'76g��C'FwC'3���tUfwƃ���U�vg�
```
Well... AHHHHHHH

This seems so stupid.
Like that's not the flag, and neither is that giving the proper flag to perform this function properly. I just want to get the flag at this point.

After three attempts, we have concluded that 
> 4ny04_g0t_r1scv_h4rdw4r3?_LGUfwl8xyMUlpgv}
and it's variations are not flags

> C�C�vG�'76g��C'FwC'3���tUfwƃ���U�vg� cannot be a flag

Then whatever could I do at this point. I was beyond lost.

### Answer:
```
```

### References and Links:
- <a href="https://www.geeksforgeeks.org/gdb-command-in-linux-with-examples/">GDB Commands</a>
- <a href="www.perplexity.a">Perplexity</a>
- <a href="https://www.rapidtables.com/convert/number/ascii-to-hex.html">String to Hex</a>
- <a href="https://www.rapidtables.com/convert/number/hex-to-ascii.html">Hex to String</a>