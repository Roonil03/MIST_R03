# <a href="https://play.picoctf.org/practice/challenge/433">format string 0</a>

![s15334812022024](https://a.okmd.dev/md/674d86072e7e1.png)

This challenge was meant to be very simple, so what I started of with is taking the `nc` and starting it up on my WSL.

As soon as I started it, I was greeted with this text:
```
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation:
```

For fun I wanted to see what would happen, so I just input:
```
Breakf@st_Burger
```
and it returned:
```
Try to serve him something of larger size!
```

and then it exited the program.<br>
The hint recommended that I try something related with formatting strings.

Therefore, I started the program agaain:
```
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: 
```

I tried to possibly simply break the string by inputting too many characters into the string input.
```
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
There is no such burger yet!
```

Well, that ended up revealing the flag in the end:
```
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}
```

### Answer:
```
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}
```

### References and Links:
- <a href="https://www.geeksforgeeks.org/format-specifiers-in-c/"> Format Specifiers</a>
