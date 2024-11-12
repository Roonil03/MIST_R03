# <a href="https://play.picoctf.org/practice/challenge/65">vault-door-7</a>
![s10152611122024](https://a.okmd.dev/md/6732dd695bbe9.png)

This one was a fun one to crack. The basic TL;DR of it was that 4 characters are grouped together, their bit values are gathered and it is converted into an integer, that is used to store the values.

I opened the file and was greeted to the following code in the password checker:
```
return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734291511
            && x[6] == 960049251
            && x[7] == 1681089078;
```

it was definitely looking as though there are going to be a lot of padding and numbering that I would be needing to do.

#### First Strategy:
I first purely tried to reverse engineer the entire problem.<br>
The main thing that I did was convert all the integers into bit strings, then split them into substrings and find their character values and print those values.
So here was the code that I did:
```
s[0] = Integer.toBinaryString(1096770097);
        s[1] = Integer.toBinaryString(1952395366);
        s[2] = Integer.toBinaryString(1600270708);
        s[3] = Integer.toBinaryString(1601398833);
        s[4] = Integer.toBinaryString(1716808014);
        s[5] = Integer.toBinaryString(1734291511);
        s[6] = Integer.toBinaryString(960049251");
        s[7] = Integer.toBinaryString(1681089078);
        char[] pass = new char[32];
        for (int i = 0; i < s.length; i++) {
            if (s[i].length() != 32) {
                while (s[i].length() < 32) {
                    s[i] = "0" + s[i];
                }
            }
            System.out.println(s[i] + " " + s[i].length());
        }
        int count = 0;
        for (int i = 0; i < s.length; i++) {
            for (int j = 0; j < 4; j++, count++) {
                int byteValue = Integer.parseInt(s[i].substring(j * 8, (j + 1) * 8), 2);
                pass[count] = (char) Integer.bitCount(byteValue);
            }
        }
        System.out.println(count);
        System.out.print("picoCTF{");
        for(int i = 0; i<32;i++)
        {
            System.out.print(pass[i]);
        }
        System.out.println("}");
```

By this, I could try and see if there was anything that I could get, and I ended up getting an output with a lot of weird characters to say the least:
```
01000001010111110110001000110001 32
01110100010111110011000001100110 32
01011111011000100011000101110100 32
01011111011100110110100000110001 32
01100110010101000110100101001110 32
01100111010111110011000000110111 32
00111001001110010011000001100011 32
01100100001100110110001000110110 32
32
picoCTF{☻♠♥♥♦♠☻♦♠♥♥♦♠♣♥♥♦♥♦♦♣♠☻♣♦♦☻♦♥♦♥♦}
Enter vault password: picoCTF{☻♠♥♥♦♠☻♦♠♥♥♦♠♣♥♥♦♥♦♦♣♠☻♣♦♦☻♦♥♦♥♦}
Access denied!
```

Clearly the appraoch that I was working with was not working, so time to find a new strategy to deal with this problem.

#### Second Strategy:
After scowering the net, I learnt that the integer itself could be converted to it's hex form in Java, so all I needed to do was remove the ``Integer.toBinaryString`` method and directly convert it into int.
So, I altered the program to do the following functionality:
```
        String s[] = new String[8];
        s[0] = ("1096770097");
        s[1] = ("1952395366");
        s[2] = ("1600270708");
        s[3] = ("1601398833");
        s[4] = ("1716808014");
        s[5] = ("1734291511");
        s[6] = ("960049251");
        s[7] = ("1681089078");
                String n[] = new String[8];
        for(int i = 0; i< n.length;i++)
        {
            n[i] = Integer.toHexString(Integer.parseInt(s[i]));
        }
        for(int i = 0; i<n.length;i++)
        {
            System.out.print(n[i]);
        }
        System.out.println("");
```
This gave the entire output in hex, which I could put into a Hex-ASCII convertor and get the output that I required. On running the program, this was what I got in the terminal:
```
415f6231745f30665f6231745f7368316654694e675f30373939306364336236
Enter vault password: 
```

Now all I needed to do was put this hex in to the convertor:<br>
![s10245311122024](https://a.okmd.dev/md/6732df9fcf36a.png)

Which ended up giving me this as the output:
```
A_b1t_0f_b1t_sh1fTiNg_07990cd3b6
```

If we put this in the program output by altering the program a little:
```
        String userInput = scanner.next();
	    //String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(userInput)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
```
We get this in the output:
```
Enter vault password: A_b1t_0f_b1t_sh1fTiNg_07990cd3b6
Access granted.
```

Giving us the answer to this problem.


### Answer:
```
picoCTF{A_b1t_0f_b1t_sh1fTiNg_07990cd3b6}
```

### References and Links:
- <a href="https://www.javatpoint.com/java-integer-bitcount-method">``bitCount()`` method</a>
- <a href="https://www.educative.io/answers/how-to-convert-an-integer-to-binary-in-java">`toBinaryString()` method</a>
- <a href="https://www.tutorialspoint.com/convert-integer-to-hex-string-in-java#:~:text=toHexString()%20method%20in%20Java,int%20values%20to%20hex%20string.">`toHexString()` method</a>
- <a href="https://www.rapidtables.com/convert/number/hex-to-ascii.html">Hex to ASCII Convert</a>