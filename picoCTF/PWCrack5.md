# <a href="https://play.picoctf.org/practice/challenge/249"> PW Crack 5</a>

![s21560106062025](https://a.okmd.dev/md/6843169b96c3f.png)  
This time, they gave us an entire textfile of possible combinations that could be the password.  
Thus, I altered the python script to read the file as input and test out each and every possible combination.
```Python
filename = "dictionary.txt"
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            str = line.strip()
            if not str:
                continue
            user_pw = str
            user_pw_hash = hash_pw(str)
            if( user_pw_hash == correct_pw_hash ):
                print(line_num, "Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), user_pw)
                print(decryption)
                return
```

Thus, with this, I could iterate through and see which combination ended up giving us the answer, and sure enough, it was a pretty hard number to manually brute-force
```
Please enter correct password for flag: wea
32352 Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_40f26f81}
```

Thus, at the 32,353<sup>rd</sup> number, I got my answer!

### Answer:
```
picoCTF{h45h_sl1ng1ng_40f26f81}
```

### References and Links:
*NULL*
