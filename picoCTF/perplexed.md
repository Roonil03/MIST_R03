# <a href="https://play.picoctf.org/practice/challenge/458"> perplexed</a>

![s21510506062025](https://a.okmd.dev/md/684315737a3ae.png)  
This problem took me a while.

I realized that I hadn't installed a decompiler application yet, so the first thing I did is install Ghidra into my system.

After that I `chmod`-ed the bin file so that I can run and see what was taking place with the executible file.
```
$ chmod +x perplexed 
```
```
$ ./perplexed 
Enter the password: sljenrnq3
Wrong :(
```

It was clear that I had to find the code that was responsible for holding the actual password.

First I used `file` to get what type of file it was runnning:
```
$ file perplexed 
perplexed: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=85480b12e666f376909d57d282a1ef0f30e93db4, for GNU/Linux 3.2.0, not stripped
```

Then I decompiled the code to get some interesting results.  
Especially this part:
```
            0040140b  e8 50 fc ff ff         CALL            <EXTERNAL>::fgets                                                     char * fgets(char * __s, int __n, FILE 
            00401410  48 8d 85 f0          LEA              RAX=>local_118,[RBP + -0x110]
                              fe ff ff
            00401417  48 89 c7              MOV            RDI,RAX
             0040141a  e8 37 fd ff ff         CALL            check                                                                            undefined8 check(char * param_1)
             0040141f  89 45 fc               MOV            dword ptr [RBP + local_c],EAX
            00401422  83 7d fc 01          CMP             dword ptr [RBP + local_c],0x1
            00401426  75 11                   JNZ              LAB_00401439
            00401428  bf 25 20 40          MOV            EDI,s_Wrong_:(_00402025                                            = "Wrong :("
                              00
            0040142d  e8 fe fb ff ff          CALL            <EXTERNAL>::puts                                                     int puts(char * __s)
            00401432  b8 01 00 00         MOV            EAX,0x1
                              00
```
Which translated to this mainly:
```C
  fgets(local_118,0x100,stdin);
  uVar1 = check(local_118);
  local_c = (int)uVar1;
```

This made me check the `check()` function over there:
```
            00401189  48 ba b9 9d         MOV            RDX,-0x2d9620a4a5036247
                              fc 5a 5b df 
                              69 d2
            00401193  48 89 45 b0         MOV            qword ptr [RBP + local_58],RAX
            00401197  48 89 55 b8         MOV            qword ptr [RBP + local_50],RDX
            0040119b  48 b8 d2 fe          MOV            RAX,-0xb98120b12e4012e
                              1b ed f4 ed 
                              67 f4
             004011a5  48 89 45 bf          MOV            qword ptr [RBP + local_50+0x7],RAX
             004011a9  c7 45 ec 00         MOV            dword ptr [RBP + local_1c],0x0
                              00 00 00
            004011b0  c7 45 e8 00         MOV            dword ptr [RBP + local_20],0x0
                              00 00 00
            004011b7  c7 45 dc 00         MOV            dword ptr [RBP + local_2c],0x0
                              00 00 00
             004011be  c7 45 e4 00         MOV            dword ptr [RBP + local_24],0x0
                              00 00 00
```
This was the assembly part, which when I found the C function of it:
```
    local_58[0] = -0x1f;
    local_58[1] = -0x59;
    local_58[2] = '\x1e';
    local_58[3] = -8;
    local_58[4] = 'u';
    local_58[5] = '#';
    local_58[6] = '{';
    local_58[7] = 'a';
    local_58[8] = -0x47;
    local_58[9] = -99;
    local_58[10] = -4;
    local_58[0xb] = 'Z';
    local_58[0xc] = '[';
    local_58[0xd] = -0x21;
    local_58[0xe] = 'i';
    local_58[0xf] = 0xd2;
    local_58[0x10] = -2;
    local_58[0x11] = '\x1b';
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 'g';
    local_58[0x16] = -0xc;
```

Resulted in me finding this.  
With that, I patiently decoded each of the hex-es to get this:
```
code = [0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2, 0xfe, 0x1b, 0xed, 0x67, 0xf4]
```

I tried printing the hex characters by itself, but they ended up throwing random garbage values, which was entirely useless to me.

Thus, I decided to read up a little bit more on Ghidra to see if I could make something of the code that they had provided.  
And I am glad that I did that.

I had to change the sequence of the bits in a particular arrangement. Therefore, based on the decompiled code, I constructed a convertor in python:
```Python
secret = [0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2, 0xfe, 0x1b, 0xed, 0x67, 0xf4]
password = bytearray(27)
char_index, bit_index = 0, 0 
for i in range(len(secret)):
    for j in range(8):
        if bit_index == 0:
            bit_index = 1
        secret_bit = (secret[i] >> (7 - j))
        pass_mask = 1 << (7 - bit_index) 
        if secret[i] & secret_bit:
            password[char_index] |= pass_mask        
        bit_index += 1
        if bit_index == 8:
            bit_index = 0
            char_index += 1
            if char_index >= len(password):
                break
print(password.decode('ascii', errors='replace'))
```

This gave me this:
```
$ python3 pw.py 
saq{|f1owsy=7[oq}~?
```

which was clearly not the flag, but we were getting somewhere.

Modifying the code a bit, I finally landed with this:
```Python
code = [0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2, 0xfe, 0x1b, 0xed, 0xf4,0xed, 0x67, 0xf4]
password = bytearray(27)
char_index, bit_index = 0, 0 
for i in range(len(code)):
    for j in range(8):
        if bit_index == 0:
            bit_index = 1
        secret_bit = 1 << (7-j)# (secret[i] >> (7 - j))
        pass_mask = 1 << (7 - bit_index) 
        if code[i] &secret_bit:
            password[char_index] |= pass_mask        
        bit_index += 1
        if bit_index == 8:
            bit_index = 0
            char_index += 1
            if char_index >= len(password):
                break
print(password.decode('ascii', errors='replace'))
```
Additionally, I found two missing pieces to the code, that brought the final code to this:
```
code = [0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2, 0xfe, 0x1b, 0xed, 0xf4,0xed, 0x67, 0xf4]
```

Thus, with that, I finally got the answer printed!
```
$ python3 pw.py 
picoCTF{0n3_bi7_4t_a_7im3}
```

### Answer:
```
picoCTF{0n3_bi7_4t_a_7im3}
```

### References and Links:
- <a href="https://www.wikihow.com/Open-BIN-Files">Wikihow BIN Files</a>
- <a href="https://stackoverflow.com/questions/9477157/how-to-run-binary-file-in-linux">Running BIN files on Linux</a>
- <a href="https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html"> ASCII Convertor</a>
- <a href="https://www.perplexity.ai/">Perplexity to Generate the Python Script</a>
