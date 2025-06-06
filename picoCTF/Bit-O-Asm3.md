# <a href="https://play.picoctf.org/practice/challenge/393">Bit-O-Asm-3</a>

![s21445306062025](https://a.okmd.dev/md/684313ff7461b.png)  
Now this is the assembly code that we got:
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```

Reverse working it, we can see that eax is loaded with the value 1f5, loaded into `rbp-0x4` and then got that value again without any manipulation in between.  
Therefore we add 0x27f868 with 0x1f5 to get 0x27fa5d

Thus the answer that we can get is:  
27fa5d<sub>16</sub> = 2619997<sub>10</sub>

### Answer:
```
picoCTF{2619997}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/hex-to-decimal.html">Hex to Decimal Convertor</a>