# <a href="https://play.picoctf.org/practice/challenge/72">asm3</a>

![s21381206062025](https://a.okmd.dev/md/6843126e416b2.png)  
This is the third iteration of this problem. This was the code that was given in the file:
```
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xa]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xc]
	<+15>:	add    ah,BYTE PTR [ebp+0xd]
	<+18>:	xor    ax,WORD PTR [ebp+0x10]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    
```

We are going to have to deal with asm3(0xd73346ed, 0xd48672ae, 0xd3c8b139)

First, we initialize eax and then XOR it with itself, netting a 0
Then, we get:
- eax as 0x3300 after `mov`-ing and `shl`-ing

Then we subtract, and add:
- making eax = 0x52
- then finally 0x7252

Then in the end, we get 0xc36b.

Thus, the answer is 0xc36b

### Answer:
```
0xc36b
```

### References and Links:
*NULL*