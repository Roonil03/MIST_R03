# <a href="https://play.picoctf.org/practice/challenge/12">vault-door-1</a>

![s09481711082024](https://a.okmd.dev/md/672d910cd1f08.png)

In this challenge, I first began with looking at the source code of the java file that was given to us. It was clear that we needed to match the password, and the password was given to us in this format:
```
 public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
```

This would mean that I would need to write a method that instead of checking uses these characters to form a password...<br>
And therefore, I sat with that creating this java snippet:
```
char arr[] = new char[32];
               arr[0]  = 'd';
               arr[29] = '9' ;
               arr[4]  = 'r' ;
               arr[2] = '5' ;
               arr[23] = 'r' ;
               arr[3] = 'c' ;
               arr[17] = '4' ;
               arr[1]  = '3' ;
               arr[7]  = 'b' ;
               arr[10] = '_' ;
               arr[5]  = '4' ;
               arr[9] = '3' ;
               arr[11] = 't' ;
               arr[15] = 'c' ;
               arr[8] = 'l' ;
               arr[12] = 'H' ;
               arr[20] = 'c' ;
               arr[14] = '_' ;
               arr[6] = 'm' ;
               arr[24] = '5' ;
               arr[18] = 'r' ;
               arr[13] = '3' ;
               arr[19] = '4' ;
               arr[21] = 'T' ;
               arr[16] = 'H' ;
               arr[27] = '5' ;
               arr[30] = '2' ;
               arr[25] = '_' ;
               arr[22] = '3' ;
               arr[28] = '0' ;
               arr[26] = '7' ;
               arr[31] = 'e';
        for(int i = 0; i< 32;i++)
        {
            System.out.print(arr[i]);
        }
```

I used this in the ``main`` method to get the output that was required and found the flag as a text message,

### Answer:
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```

### References and Links:
<i>NULL</i>