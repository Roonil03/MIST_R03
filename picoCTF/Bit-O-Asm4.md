# <a href="https://play.picoctf.org/practice/challenge/394">Bit-O-Asm-4</a>

![s21460106062025](https://a.okmd.dev/md/68431444000b7.png)  
Being the last challenge in this series, this was the code that was given to us:
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

Here, we first load the value 0x9fe1a into the `rba-0x4` position, and then we subtract 0x65 from it after not jumping. Now that we can finally jump, we skip the statement and then head to the mov command autoamtically.

Here, we load the balue 0x9fe1a - 0x65 to get 0x0x9fdb5

Where we get:
9fdb5<sub>16</sub> = 654773<sub>10</sub>

### Answer:
```
picoCTF{654773}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/hex-to-decimal.html">Hex and Decimal Convertor</a>