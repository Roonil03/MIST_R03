# <a href="https://play.picoctf.org/practice/challenge/392">Bit-O-Asm-2</a>

![s21433606062025](https://a.okmd.dev/md/684313b20a443.png)  
This time, the code was using `DWORD`s and `QWORD`s.
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```
We load 0x9fe1a to location `rbp-0x4`.  
Then we get that number and load it into eax, making eax's value 0x9fe1a

Therefore, the answer becomes:
9fe1a<sub>16</sub> which is 654874<sub>10</sub>

### Answer:
```
picoCTF{654874}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=9FE1A">Hex to Decimal</a>
- <a href="https://stackoverflow.com/questions/23512281/what-does-the-the-dword-operand-do-in-assembly">DWORD Pointers</a>