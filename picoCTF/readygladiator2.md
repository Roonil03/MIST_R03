# <a href="https://play.picoctf.org/practice/challenge/370">Ready Gladiator 2</a>
![s17233411032024](https://a.okmd.dev/md/6727644230b40.png)

<b>That hint was utterly useless to me.</b>

Time to get the file again...
```
wget https://artifacts.picoctf.net/c/281/imp.red
```
```
roonil03@Roonil:~$ wget https://artifacts.picoctf.net/c/281/imp.red
--2024-11-03 11:44:21--  https://artifacts.picoctf.net/c/281/imp.red
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 54.192.18.125, 54.192.18.66, 54.192.18.81, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|54.192.18.125|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45 [application/octet-stream]
Saving to: ‘imp.red’

imp.red                                100%[============================================================================>]      45  --.-KB/s    in 0s

2024-11-03 11:44:23 (15.0 MB/s) - ‘imp.red’ saved [45/45]
```

After getting the file, I just wanted to make sure that it the same file as the previosu ones, so I just did a simple ``cat`` to check and see if it was the same and sure enough, it was the same one.

```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

Since I have to beat all 100 rounds to make sure that I get the flag, I started to think about different strategies.

#### First Strategy:
I just inserted below the ``mov 0 1`` the lines:
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33
end
```

Then I ran the ``nc saturn.picoctf.net 51449 < imp.red`` and that got me this result:
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 0, 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 0
Ties: 100
Try again. Your warrior (warrior 1) must win 100 times.
```
#### Second Strategy:
I removed the ``mov`` to check and see if that would affect anything in the entire outcome, since that would become a simple bombing statement...<br>
And that netted me in getting 23 wins... 77 more to go.
```
;redcode
;name Imp Ex
;assert 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33
end

Rounds: 100
Warrior 1 wins: 23
Warrior 2 wins: 0
Ties: 77
Try again. Your warrior (warrior 1) must win 100 times.
```

### Third Strategy:
I was searching up ways to check and see if there was any way to make sure that a program will always win, and I found out a <i>Reddit</i> post that talked about a similar situation to mine. One of the comments in that post had this statement that I could try and use:
```
JMP 0, <-5
```

Now I removed the bombing statement and tested to check and see if this would work...
```
nc saturn.picoctf.net 51449 < imp.red
```
```
;redcode
;name Imp Ex
;assert 1
JMP 0, <-5
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
JMP 0, <-5
end

Rounds: 100
Warrior 1 wins: 100
Warrior 2 wins: 0
Ties: 0
You did it!
picoCTF{d3m0n_3xpung3r_47037b25}
```

And the flag has been found once again!

Post this, I promptly removed the ``imp.red`` file from my system using ``rm imp.red`` and we move forward!

### Answer:
```
picoCTF{d3m0n_3xpung3r_47037b25}
```

### References and Links:
- <a href="https://corewar.co.uk/standards/cwg.txt">CoreWars Guidelines</a>
- <a href="http://www.koth.org/info/corewars_for_dummies/dummies.html">CoreWars for Dummies</a>
- <a href="https://www.reddit.com/r/programminggames/comments/11vaxk8/beat_classic_imp_100_of_the_time_in_corewars/"><i>Reddit</i> Post</a>