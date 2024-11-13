# <a href="https://play.picoctf.org/practice/challenge/10">vault-door-8</a>
![s08522111132024](https://a.okmd.dev/md/67341b712723a.png)

This was the final challenge in the vault door series. When I initially downloaded the code, it was all jumbled up and scrambled. Spent the next 5 mins just clearing the clutter of code that was provided to me, in hopes that I can at least see what is present in the code.<br>
After decluttering the code, this was what I found:
```
    public char[] scramble(String password) {
         /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray(); 
        for (int b=0; b<a.length; b++) {
            char c = a[b]; 
            c = switchBits(c,1,2); 
            c = switchBits(c,0,3); 
            /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ 
            c = switchBits(c,5,6); 
            c = switchBits(c,4,7);
            c = switchBits(c,0,1); 
            /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ 
            c = switchBits(c,3,4); 
            c = switchBits(c,2,5); 
            c = switchBits(c,6,7); 
            a[b] = c; 
        } 
        return a;
    } 
```

So the bits are getting scrambled as they come to us. If we take a look at the ``switchBits()`` method, we can see clearly that:
```
    public static char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit
        that was in position p2 to position p1. Precondition: p1 < p2 */ 
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); 
        /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ 
        char bit1 = (char)(c & mask1); 
        char bit2 = (char)(c & mask2); 
        /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ 
        char rest = (char)(c & ~(mask1 | mask2)); 
        char shift = (char)(p2 - p1); 
        char result = (char)((bit1<<shift) | (bit2>>shift) | rest); 
        return result;
    } 
```
The bits are getting swapped between the two positions given.
All we had to do to unscramble the mess would be to redo the scramble, in reverse order. I went further down into the code to see what values it was going to be comparing against:
```
        char[] expected = {
            0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 
        };
```

So, all we had to do was add a snippet of code that would decramble this message to give us the output that we desire:
```
            char [] w = {
               0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 
            };
            
            for(int i = 0; i< w.length;i++)
            {
                char c = w[i];
                c = switchBits(c,6,7);  
                c = switchBits(c,2,5);
                c = switchBits(c,3,4);
                c = switchBits(c,0,1);  
                c = switchBits(c,4,7);
                c = switchBits(c,5,6); 
                c = switchBits(c,0,3);  
                c = switchBits(c,1,2); 
                w[i] = c;
            }
            String s = new String(w);
            System.out.println(s);
```

I input this and tried getting the output on console:
```
s0m3_m0r3_b1t_sh1fTiNg_91c642112
Enter vault password: s0m3_m0r3_b1t_sh1fTiNg_91c642112
Access granted.
```

And it works!

### Answer:
```
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}
```

### References and Links:
<i>NULL</i>