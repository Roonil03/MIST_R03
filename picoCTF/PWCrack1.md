# <a href="https://play.picoctf.org/practice/challenge/245">PW Crack 1</a>

![s21521206062025](https://a.okmd.dev/md/684315b5d864f.png)  
After getting the hint, I initially started with reading both the files and seeing if anything was hidden in the files. The encrypted file was useless, so then I checked up on the Python file. Then I found some interesting things.

```Python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
```

So, all I had to do was input `691d` when the program was running, and I would get the flag.

That is exactly what I did, and I ended up getting the flag in that way:
```
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```

### Answer:
```
picoCTF{545h_r1ng1ng_56891419}
```

### References and Links:
*NULL*
