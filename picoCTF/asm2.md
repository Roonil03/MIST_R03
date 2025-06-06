# <a href="https://play.picoctf.org/practice/challenge/16">asm2</a>

![s21370906062025](https://a.okmd.dev/md/6843122f7fef8.png)  
This time the code was taking in two arguments for this code:
```
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    
```

This time, we start with 0x2d and 0x4
- Since we have loops, I am using my calculator for repeted calculations to prevent human mistakes
- After calculation, we land with 118 iterations.

Thus, we land with 0x2d + 118<sub>10</sub> = 163<sub>10</sub> = 0xa3

### Answer:
```
0xa3
```

### References and Links:
*NULL*