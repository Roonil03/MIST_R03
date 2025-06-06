# <a href="https://play.picoctf.org/practice/challenge/20"> asm1 </a>

![s21361306062025](https://a.okmd.dev/md/684311f724a88.png)

This program initially gave us the source code in Assembly Format:
```asm1
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3a2
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x358
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x12
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x12
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x6fa
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0x12
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x12
	<+60>:	pop    ebp
	<+61>:	ret    
```

Breaking it down, let's start with ebp 0x6fa.

- Then you turn it to esp
- Then you start comparing...
    - First compare with 0x512 and then jump
- Then you compare again at +37 adn then compare with 0x67fa
    - Since it is lower, it doesn't shift
- Finally, we get it with subtracting, so that we get 0x6e8.

Thus, with that the answer that we got is: 0x6e8

### Answer:
```
0x6e8
```

### References and Links:
-  <a href="https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm">Assembly Conditions</a>