# <a href="https://play.picoctf.org/practice/challenge/60">vault-door-3</a>

![s15534211102024](https://a.okmd.dev/md/673089b033307.png)

There is a new java file that that we can see, that stores the password required for this challenge.<br>
Therefore, after downloading the file, i went straight into VSC to open and see what was present in the contents of the file.

Post inspection of this file, I realized that there was a simple text that was provided in the end, that could help us find the answer:
```
return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
```

So, now my mind went to try and find a way to descramble this scramble so that the answer that we get can be given correctly.

#### First Strategy:
The First method I used was to just convert all the ``+`` to ``-`` and vice versa to see if there was anything can could be gotten via that. 
```
String password = input;
    char[] buffer = new char[32];
    int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23+i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46+i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        System.out.println(s);
```

Well, that ended up causing an out of bonds error which was something that I was somewhat expecting, so I scrapped this method and went forward with it.

#### Second Strategy:
Second method that I used to solve this problem was to try and manually decrypt the password. I wanted to try and see what I could get if I manually did it, so i added a simple code snippet that did this:
```
String bwa = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41";
    for(int i = 0; i<bwa.length();i++)
        {
            System.out.println(i + " " + Character.toString(bwa.charAt(i)));
        }
```
That added the indices of each character next to them that made it easier for me to solve the problem. In the end, due to some form of human error that I made because I was sleepy, or I don't know, I kept getting the wrong answer.<br>
This made me drop this method to solve this problem and try finding a more efficient method to solve this...

#### Third Strategy:
What I did was that I tried using the scramble itself as an input and trying to see what I could do with the problem, so using these changes that I made:
```
boolean aweasdawdaw = vaultDoor.checkPassword("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
```
```
 String s = new String(buffer);
        System.out.println("picoCTF{" + s + "}");
```
I got the following as an output for the entire thing:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
Enter vault password: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
picoCTF{jU5t_a_sna_3lpm12g94c_u_4_m7ra41}
Access granted.
```

So that was one stupid way to get the solution, but the answer was found nonetheless.

### Answer:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
```

### References and Links:
<i>NULL</i>