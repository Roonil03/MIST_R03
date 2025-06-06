# <a href="https://play.picoctf.org/practice/challenge/247"> PW Crack 3</a>

![s21535906062025](https://a.okmd.dev/md/68431621a6add.png)  
This challenge I attempted by bruteforcing the possible combinations that were given.

Since there were only 7 possible correct answers, I tried them all:
```Python
# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
```

Therefore I tried for them all:
```Python
Please enter correct password for flag: f09e
That password is incorrect
```

Until I finally hit the correct password:
```Python
Please enter correct password for flag: 87ab
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```

With this, I completed the challenge and found the required flag!

### Answer:
```
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```

### References and Links:
*NULL*
