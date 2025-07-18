# Intro to Cybersecurity - Cryptography:
## XOR:
The first thing I did is roam and check through the directories, where the challenge was present:
```
hacker@cryptography~xor:/$ ls -a
.           bin        dev   home   lib64   mnt  proc  sbin  tmp
..          boot       etc   lib    libx32  nix  root  srv   usr
.dockerenv  challenge  flag  lib32  media   opt  run   sys   var
hacker@cryptography~xor:/$ cat flag
cat: flag: Permission denied
hacker@cryptography~xor:/$ cat /challenge/
DESCRIPTION.md  run           
```
After finding the program `run`, I looked to see what was present in the file, and see if I could edit something with it...
```
hacker@cryptography~xor:/$ cat /challenge/run
#!/opt/pwn.college/python

import random
import sys

key = random.randrange(1, 256)
plain_secret = random.randrange(0, 256)
cipher_secret = plain_secret ^ key

print(f"The key: {key}")
print(f"Encrypted secret: {cipher_secret}")
if int(input("Decrypted secret? ")) == plain_secret:
    print("CORRECT! Your flag:")
    print(open("/flag").read())
else:
    print("INCORRECT!")
    sys.exit(1)
hacker@cryptography~xor:/$ nano /challenge/run 
```
However, since I didn't have write permissions, I couldn't change the file.  
Thus, I just ran the program and write a goLang program to give me the answer:
```
hacker@cryptography~xor:/$ /challenge/run 
The key: 252
Encrypted secret: 68
Decrypted secret? 184
CORRECT! Your flag:
pwn.college{ARKxVPH3jdsy6g5nDISMlwwx-Sl.ddjM3kDLyYjMxkzW}
```
```Go
package main
import "fmt"

func main() {
  fmt.Println(68 ^ 252)
}
```
### Answer:
```
pwn.college{ARKxVPH3jdsy6g5nDISMlwwx-Sl.ddjM3kDLyYjMxkzW}
```

## XORing Hex
This time, we'll be dealing with hex numbers:
```
hacker@cryptography~xoring-hex:~$ cat /challenge/run
#!/opt/pwn.college/python

import random
import sys

for n in range(10):
    print(f"Challenge number {n}...")

    key = random.randrange(1, 256)
    plain_secret = random.randrange(0, 256)
    cipher_secret = plain_secret ^ key

    print(f"The key: {key:#04x}")
    print(f"Encrypted secret: {cipher_secret:#04x}")
    answer = int(input("Decrypted secret? "), 16)
    print(f"You entered: {answer:#04x}, decimal {answer}.")
    if answer != plain_secret:
        print("INCORRECT!")
        sys.exit(1)

    print("Correct! Moving on.")

print("CORRECT! Your flag:")
print(open("/flag").read())
```
This time, I would need to do this challenge ten times to get the answer finally:
```
hacker@cryptography~xoring-hex:~$ /challenge/run 
Challenge number 0...
The key: 0xdf
Encrypted secret: 0x53
Decrypted secret? 140
You entered: 0x140, decimal 320.
INCORRECT!
hacker@cryptography~xoring-hex:~$ /challenge/run 
Challenge number 0...
The key: 0x8e
Encrypted secret: 0xec
Decrypted secret? 62
You entered: 0x62, decimal 98.
Correct! Moving on.
Challenge number 1...
The key: 0x08
Encrypted secret: 0x2e
Decrypted secret? 26
You entered: 0x26, decimal 38.
Correct! Moving on.
Challenge number 2...
The key: 0xb0
Encrypted secret: 0x88
Decrypted secret? 38
You entered: 0x38, decimal 56.
Correct! Moving on.
Challenge number 3...
The key: 0x15
Encrypted secret: 0xf0
Decrypted secret? e5
You entered: 0xe5, decimal 229.
Correct! Moving on.
Challenge number 4...
The key: 0x0a
Encrypted secret: 0xbe
Decrypted secret? b4
You entered: 0xb4, decimal 180.
Correct! Moving on.
Challenge number 5...
The key: 0xdb
Encrypted secret: 0x42
Decrypted secret? 99
You entered: 0x99, decimal 153.
Correct! Moving on.
Challenge number 6...
The key: 0x01
Encrypted secret: 0x16
Decrypted secret? 17
You entered: 0x17, decimal 23.
Correct! Moving on.
Challenge number 7...
The key: 0xf7
Encrypted secret: 0xe4
Decrypted secret? 13
You entered: 0x13, decimal 19.
Correct! Moving on.
Challenge number 8...
The key: 0x44
Encrypted secret: 0x3b
Decrypted secret? 7f
You entered: 0x7f, decimal 127.
Correct! Moving on.
Challenge number 9...
The key: 0x3e
Encrypted secret: 0x7e
Decrypted secret? 40
You entered: 0x40, decimal 64.
Correct! Moving on.
CORRECT! Your flag:
pwn.college{o84bnmEX06ROL8JTeuJT-lLiRbW.dBzM3kDLyYjMxkzW}
```
As you can see, I solved this using XOR with the help of goLang:
```Go
package main
import "fmt"

func main() {
  fmt.Printf("%x\n", 0x8e ^ 0xec)
  fmt.Printf("%x\n", 0x08 ^ 0x2e)
  fmt.Printf("%x\n", 0xb0 ^ 0x88)
  fmt.Printf("%x\n", 0x15 ^ 0xf0)
  fmt.Printf("%x\n", 0x0a ^ 0xbe)
  fmt.Printf("%x\n", 0xdb ^ 0x42)
  fmt.Printf("%x\n", 0x01 ^ 0x16)
  fmt.Printf("%x\n", 0xf7 ^ 0xe4)
  fmt.Printf("%x\n", 0x44 ^ 0x3b)
  fmt.Printf("%x\n", 0x3e ^ 0x7e)
}
```
Thus, with that, I got the answer...
### Answer:
```
pwn.college{o84bnmEX06ROL8JTeuJT-lLiRbW.dBzM3kDLyYjMxkzW}
```

## XORing ASCII
This time, I will need to alter the code to print characters.
```
hacker@cryptography~xoring-ascii:~$ cat /challenge/run 
#!/opt/pwn.college/python

import random
import string
import sys

if not sys.stdin.isatty():
    print("You must interact with me directly. No scripting this!")
    sys.exit(1)

for n in range(1, 10):
    print(f"Challenge number {n}...")
    pt_chr, ct_chr = random.sample(
        string.digits + string.ascii_letters + string.punctuation,
        2
    )
    key = ord(pt_chr) ^ ord(ct_chr)

    print(f"- Encrypted Character: {ct_chr}")
    print(f"- XOR Key: {key:#04x}")
    answer = input("- Decrypted Character? ").strip()
    if answer != pt_chr:
        print("Incorrect!")
        sys.exit(1)

    print("Correct! Moving on.")

print("You have mastered XORing ASCII! Your flag:")
print(open("/flag").read())
```
We will be doing this ten times again...  
Therefore I prepared a go script so that I can quickly get the answers:
```Go
package main
import "fmt"

func main() {
    for i:= 0; i < 10; i++{
        var x rune
        var y int
        fmt.Scanf("%c %x", &x, &y)
        fmt.Printf("%c\n", byte(x)^byte(y))
    }
}
```
Thus, I began:
```
hacker@cryptography~xoring-ascii:~$ /challenge/run 
Challenge number 1...
- Encrypted Character: a
- XOR Key: 0x09
- Decrypted Character? h
Correct! Moving on.
Challenge number 2...
- Encrypted Character: J
- XOR Key: 0x7c
- Decrypted Character? 6
Correct! Moving on.
Challenge number 3...
- Encrypted Character: %
- XOR Key: 0x10
- Decrypted Character? 5
Correct! Moving on.
Challenge number 4...
- Encrypted Character: u
- XOR Key: 0x19
- Decrypted Character? l
Correct! Moving on.
Challenge number 5...
- Encrypted Character: K
- XOR Key: 0x01
- Decrypted Character? J
Correct! Moving on.
Challenge number 6...
- Encrypted Character: D
- XOR Key: 0x07
- Decrypted Character? C
Correct! Moving on.
Challenge number 7...
- Encrypted Character: ~
- XOR Key: 0x2d
- Decrypted Character? S
Correct! Moving on.
Challenge number 8...
- Encrypted Character: D
- XOR Key: 0x1d
- Decrypted Character? Y
Correct! Moving on.
Challenge number 9...
- Encrypted Character: $
- XOR Key: 0x46
- Decrypted Character? b
Correct! Moving on.
You have mastered XORing ASCII! Your flag:
pwn.college{E3PR89n-_J4N14NAvuEnNVjmf2k.dhjM3kDLyYjMxkzW}
```
### Answer:
```
pwn.college{E3PR89n-_J4N14NAvuEnNVjmf2k.dhjM3kDLyYjMxkzW}
```

## XORing ASCII Strings
For this challenge, the hints recommended me to use `Python`, so I switched it up.  
Starting the challenge, this was the code that was provided:
```
hacker@cryptography~xoring-ascii-strings:~$ cat /challenge/run 
#!/opt/pwn.college/python

import random
import string
import sys

from Crypto.Util.strxor import strxor

valid_keys = "!#$%&()"
valid_chars = ''.join(
    c for c in string.ascii_letters
    if all(chr(ord(k)^ord(c)) in string.ascii_letters for k in valid_keys)
)

print(valid_keys, valid_chars)

for n in range(1, 10):
    print(f"Challenge number {n}...")

    key_str = ''.join(random.sample(valid_keys*10, 10))
    pt_str = ''.join(random.sample(valid_chars*10, 10))
    ct_str = strxor(pt_str.encode(), key_str.encode()).decode()

    print(f"- Encrypted String: {ct_str}")
    print(f"- XOR Key String: {key_str}")
    answer = input("- Decrypted String? ").strip()
    if answer != pt_str:
        print("Incorrect!")
        sys.exit(1)

    print("Correct! Moving on.")

print("You have mastered XORing ASCII! Your flag:")
print(open("/flag").read())
```
Therefore, this was the python3 script that I developed:
```Python
def strxor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])
for i in range(10):
    str1 = input("Enter first string: ").encode('latin-1')
    str2 = input("Enter second string: ").encode('latin-1')
    result = strxor(str1, str2)
    print("XOR result:", result.decode('latin-1'))
```

and with that, I solved the problem:
```
hacker@cryptography~xoring-ascii-strings:~$ /challenge/run 
!#$%&() bgjklmnopqBGJKLMNOPQ
Challenge number 1...
- Encrypted String: BkkhbcICDO
- XOR Key String: %&$$%!#!&%
- Decrypted String? gMOLGBjbbj
Correct! Moving on.
Challenge number 2...
- Encrypted String: oYIhDXTaBg
- XOR Key String: #)%$(($&%)
- Decrypted String? LplLlppGgN
Correct! Moving on.
Challenge number 3...
- Encrypted String: jLjFeIbIqi
- XOR Key String: (!&))#%%!%
- Decrypted String? BmLoLjGlPL
Correct! Moving on.
Challenge number 4...
- Encrypted String: FeTdfHhtUG
- XOR Key String: !($&$#%$$)
- Decrypted String? gMpBBkMPqn
Correct! Moving on.
Challenge number 5...
- Encrypted String: JiJNBMFDbd
- XOR Key String: &#$$%&)((#
- Decrypted String? lJnjgkolJG
Correct! Moving on.
Challenge number 6...
- Encrypted String: okLkPCgXTf
- XOR Key String: $$&)!(%)$(
- Decrypted String? KOjBqkBqpN
Correct! Moving on.
Challenge number 7...
- Encrypted String: BuoujnfNWA
- XOR Key String: (%!$&!$%&&
- Decrypted String? jPNQLOBkqg
Correct! Moving on.
Challenge number 8...
- Encrypted String: xsNIJCsALj
- XOR Key String: (#$&&)#&#(
- Decrypted String? PPjoljPgoB
Correct! Moving on.
Challenge number 9...
- Encrypted String: bHJdLgxnOh
- XOR Key String: )$(#!%)#(&
- Decrypted String? KlbGmBQMgN
Correct! Moving on.
You have mastered XORing ASCII! Your flag:
pwn.college{oklPiLqxtC3gqVctGRysjp7PciL.dljM3kDLyYjMxkzW}
```
### Answer:
```
pwn.college{oklPiLqxtC3gqVctGRysjp7PciL.dljM3kDLyYjMxkzW}
```

## One-time Pad:
It was time to learn about [one-time pad](https://en.wikipedia.org/wiki/One-time_pad) now. Something new, that I haven't touched at all, but it does seem interesting.  
This was the code that we got:
```
hacker@cryptography~one-time-pad:~$ cat /challenge/run 
#!/opt/pwn.college/python

from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor

flag = open("/flag", "rb").read()

key = get_random_bytes(len(flag))
ciphertext = strxor(flag, key)

print(f"One-Time Pad Key (hex): {key.hex()}")
print(f"Flag Ciphertext (hex): {ciphertext.hex()}")
```
Therefore, it was time to make a python script that gets the actual code for this:
```
hacker@cryptography~one-time-pad:~$ /challenge/run 
One-Time Pad Key (hex): a1453ba368064542bde9ef86620e1d03913ea06ee15032d76e00b4cd81cedf3216e541ce490b988af46a1a605872b1231ee6b4bd08954b42712f
Flag Ciphertext (hex): d132558d0b69292ed88e8afd2b54486aa87fe606d71a63b65c72f981c99cbc79658e028b0843d1a49038602e223ff56f67bfdef070fe31150c25
```
This was what I was working with:
```Python
ct_hex = input("Enter ciphertext (hex): ").strip()
key_hex = input("Enter key (hex): ").strip()
try:
    ct_bytes = bytes.fromhex(ct_hex)
    key_bytes = bytes.fromhex(key_hex)
except ValueError:
    print("Invalid hex input")
    exit()
if len(ct_bytes) != len(key_bytes):
    print("Error: Ciphertext and key must be the same length")
    exit()
plaintext = bytes([c ^ k for c, k in zip(ct_bytes, key_bytes)])
try:
    print("Decrypted:", plaintext.decode('utf-8'))
except UnicodeDecodeError:
    print("Decrypted (hex):", plaintext.hex())
```
and with this, I found the flag!
### Answer:
```
pwn.college{IZUi9AFh6JQa2rMLHRcKskCEAHI.dRzNzMDLyYjMxkzW}
```
## One-time Pad Tampering:
This time, I was lost as to how to start the challenge, since I couldn't find the initial `/challenge/run` program. So I started `cat`-ing all the files until I found something interesting:
```
hacker@cryptography~one-time-pad-tampering:/$ cat /challenge/dispatcher 
#!/opt/pwn.college/python

from Crypto.Util.strxor import strxor

key = open("/challenge/.key", "rb").read()
ciphertext = strxor(b"sleep", key[:5])

print(f"TASK: {ciphertext.hex()}")
hacker@cryptography~one-time-pad-tampering:/$ 
```
Well, this was big...  
This code basically taking five values of the key and then XOR-ing it to get your cipher text.   
Since we know that the word is `'sleep'`, therefore I was hoping that they use this same key to encrypt their other messages:
```
9c1c2eeea7
```
After running to the program used in the previous question, we get:
```
ef704b8bd7
```
So this was what the initial five digits of the key are, is what I presumed...  
Here was another code snippet that I found while digging through:
```
hacker@cryptography~one-time-pad-tampering:/$ cat /challenge/worker 
#!/opt/pwn.college/python

from Crypto.Util.strxor import strxor

import time
import sys

key = open("/challenge/.key", "rb").read()

while line := sys.stdin.readline():
    if not line.startswith("TASK: "):
        continue
    data = bytes.fromhex(line.split()[1])
    cipher_len = min(len(data), len(key))
    plaintext = strxor(data[:cipher_len], key[:cipher_len])

    print(f"Hex of plaintext: {plaintext.hex()}")
    print(f"Received command: {plaintext}")
    if plaintext == b"sleep":
        print("Sleeping!")
        time.sleep(1)
    elif plaintext == b"flag!":
        print("Victory! Your flag:")
        print(open("/flag").read())
    else:
        print("Unknown command!")
```
So I had to encrypt `flag!` and then put that as the input.
Thus, I encrypted it and got this:
```
891c2aecf6
```
With that, I put into the terminal:
```
hacker@cryptography~one-time-pad-tampering:/$ /challenge/worker 
TASK: 891c2aecf6
Hex of plaintext: 666c616721
Received command: b'flag!'
Victory! Your flag:
pwn.college{4ehnH2JnMb4MLRNHszAVCergx1C.QXzcTO2EDLyYjMxkzW}
```
and there's the flag!

### Answer:
```
pwn.college{4ehnH2JnMb4MLRNHszAVCergx1C.QXzcTO2EDLyYjMxkzW}
```

## Many-time Pad:
In this, we continue using the same program to get the key used to encrypt the messages:
```
hacker@cryptography~many-time-pad:~$ cat /challenge/run 
#!/opt/pwn.college/python

from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor

flag = open("/flag", "rb").read()

key = get_random_bytes(256)
ciphertext = strxor(flag, key[:len(flag)])

print(f"Flag Ciphertext (hex): {ciphertext.hex()}")

while True:
    plaintext = bytes.fromhex(input("Plaintext (hex): "))
    ciphertext = strxor(plaintext, key[:len(plaintext)])
    print(f"Ciphertext (hex): {ciphertext.hex()}")
```
Therefore, to get the flag, I ran it with plaintext `0`s:
```
hacker@cryptography~many-time-pad:~$ /challenge/run 
Flag Ciphertext (hex): 9fb7e3e1076c9d2389e842ee1edc26bdb9c82d2e45cd150fff67bae67fe9cd33f8132d1e0a2335a929f694c4e4ace08dc9a78ab429c52cb19a4a
Plaintext (hex): 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Ciphertext (hex): efc08dcf6403f14fec8f279575b3658ec8ff606906ab6765ab1dc9de4888fa04d53e7c5d43157f874da0ee8a9ee1a4c1b0fee0f951ae56e6e740
```
Thus, I think the key was found to be:  
`efc08dcf6403f14fec8f279575b3658ec8ff606906ab6765ab1dc9de4888fa04d53e7c5d43157f874da0ee8a9ee1a4c1b0fee0f951ae56e6e740`  
Thus, let me try deciphering the flag with the program used before to get:
```
Enter ciphertext (hex): efc08dcf6403f14fec8f279575b3658ec8ff606906ab6765ab1dc9de4888fa04d53e7c5d43157f874da0ee8a9ee1a4c1b0fee0f951ae56e6e740
Enter key (hex): 9fb7e3e1076c9d2389e842ee1edc26bdb9c82d2e45cd150fff67bae67fe9cd33f8132d1e0a2335a929f694c4e4ace08dc9a78ab429c52cb19a4a
Decrypted: pwn.college{koC3q7MGCfrjTzs87a77--QCI6J.dVzNzMDLyYjMxkzW}
```
and thus, the flag was found:
### Answer:
```
pwn.college{koC3q7MGCfrjTzs87a77--QCI6J.dVzNzMDLyYjMxkzW}
```
## AES:
We finally begin with AES encrpytion.  
It seems like we'll have to use pycryptodome from this challenge onwards, so I create a virtual local environment for running my python scripts.
```Python

```
and this was the cipher that we got:
```
hacker@cryptography~aes:~$ /challenge/run 
AES Key (hex): 88cd6f929c8152a0eea4d64e0ce47094
Flag Ciphertext (hex): ebc3c5b0ebd18c330d0df297fbab36d4fc19c2b34e998394609008344230db78fe9b62bd3c40eada091f847234131a1999e081e95314323a968e617f9e04bb63
```
After runnning it on the terminal, we get out flag!
### Anwer:
```
pwn.college{Un4BHv3YGK9AO_BEjz776_c2986.dZzNzMDLyYjMxkzW}
```

## AES-ECB-CPA:
Running the `cat`, we get:
```
hacker@cryptography~aes-ecb-cpa:~$ cat /challenge/run 
#!/opt/pwn.college/python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

flag = open("/flag", "rb").read()

key = get_random_bytes(16)
cipher = AES.new(key=key, mode=AES.MODE_ECB)

while True:
    print("Choose an action?")
    print("1. Encrypt chosen plaintext.")
    print("2. Encrypt part of the flag.")
    if (choice := int(input("Choice? "))) == 1:
        pt = input("Data? ").strip().encode()
    elif choice == 2:
        index = int(input("Index? "))
        length = int(input("Length? "))
        pt = flag[index:index+length]
    else:
        break

    ct = cipher.encrypt(pad(pt, cipher.block_size))
    print(f"Result: {ct.hex()}")
```
Thus, with that, we start creating a program for getting the flag:
```Python
```