# <a href="https://play.picoctf.org/practice/challenge/391">Bit-O-Asm-1</a>

![s21420006062025](https://a.okmd.dev/md/6843135356e68.png)  
The code provided was this:
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```
As we can see there a line that goes:
```
<+15>:    mov    eax,0x30
```
Thus, the number in the register is:  
30<sub>16</sub> which is 48<sub>10</sub>

### Answer:
```
picoCTF{48}
```

### References and Links:
*NULL*