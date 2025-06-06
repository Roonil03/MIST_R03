# <a href="https://play.picoctf.org/practice/challenge/246">PW Crack 2</a>

![s21530306062025](https://a.okmd.dev/md/684315e9baeed.png)  
The problem starts out similar to the previous one, but instead of the code having the password directly, it was stored as a hex.
```Python
if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
```
Therefore, all I did was convert this hexadecimal values to their corresponding ASCII values to get the password:
```
64 65 37 36

de76
```

And voila, the answer showcased itself in the program!
```
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
```

### Answer:
```
picoCTF{tr45h_51ng1ng_489dea9a}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/hex-to-ascii.html">Hex to String Convertor</a>
