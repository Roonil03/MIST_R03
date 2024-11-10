# <a href="https://play.picoctf.org/practice/challenge/71">vault-door-4</a>
![s16094511102024](https://a.okmd.dev/md/67308d72c1c53.png)

This problem seems to be much simpler than the one I solved before. 

So i just opened the file, anticipating someting much easier than what I solved in vault-door-3.

Opening the file, I noticed the myBytes array had stored the entire thing in the array itself:
```
byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ,
            'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
        };
```
Since in the ``checkPassword`` method, it was converting the string input into the byte form as well. Therefore, all I needed to do was convert this into a string.<br>
So I went into the ``main`` method to add this snippet of code that would print the correct flag into the output console:
```
byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ,
            'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
        };
        String str = new String(myBytes);
        System.out.println("picoCTF{" + str + "}");
```
And sure enough, running it on the terminal, we got this output:
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
Enter vault password: picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
Access granted.
```

So that was the answer.

<i>
Also another point to note, I really loved the text art that was done in this problem statement:</i>

```
I made myself dizzy converting all of these numbers into different bases, 
so I just *know* that this vault will be impenetrable. This will make Dr.
Evil like me better than all of the other minions--especially Minion
#5620--I just know it!
    
     .:::.   .:::.
    :::::::.:::::::
    :::::::::::::::
    ':::::::::::::'
      ':::::::::'
        ':::::'
          ':'
-Minion #7781
```

### Answer:
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
```

### References and Links:
- <a href="https://www.javatpoint.com/java-string-getbytes">getBytes()</a>
- <a href="https://www.quora.com/How-do-you-convert-bytes-to-character-in-Java#:~:text=In%20Java%2C%20you%20can%20convert%20bytes%20to%20characters%20using%20the,str%20%3D%20new%20String(byteArray)%3B">byte array to String</a>