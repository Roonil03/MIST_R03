# <a href="https://play.picoctf.org/practice/challenge/45">vault-door-6</a>

![s11532011112024](https://a.okmd.dev/md/6731a2dc829d9.png)

In this problem statement, we can see that there is an ``XOR``encryption that is taking place over here...

All that needs to be done is find that main thing, since as the hint stated:
```
If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.
```

So, I opened the Java file to see what was present in the passwordChecker method.
```
byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
```

Again, there was a byte array that stored the various different data that needed to be compared with.

Then I saw this:
```
for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
```
This woudld mean that the passBytes that are being passed are actually having a simple operation with myBytes...<br>
Since,<br>
``passBytes[i] ^ 0x55 - myBytes[i] = 0``<br>
``passBytes[i] ^ 0x55 = myBytes[i]`` <br>
``myBytes[i] ^ 0x55 = passBytes[i]``<br>

Therefore, I input this code snippet in the main method:
```
byte[] myBytes = {
    0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
    0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
    0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
    0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
};
System.out.print("picoCTF{");
byte[] passBytes = new byte[32];
for(int i = 0; i<32; i++)
{
    passBytes[i] = (byte)(myBytes[i] ^ 0x55);
}
System.out.print(new String(passBytes));
System.out.println("}");
```

And we get the flag in the console of the terminal window:
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}
Enter vault password: picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}
Access granted.
```

### Answer:
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}
```

### References and Links:
<i>NULL</i>