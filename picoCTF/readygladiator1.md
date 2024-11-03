# <a href="https://play.picoctf.org/practice/challenge/369"> Ready Gladiator 1</a>

![s16593711032024](https://a.okmd.dev/md/67275ea4639d4.png)

This was another reverse engineering challenge that was related to corewars. I was already familiarized with it from the previous challenge, so all I did was regot the imp.red file again.
```
 wget https://artifacts.picoctf.net/c/407/imp.red
 ```
 ```
 --2024-11-03 11:23:53--  https://artifacts.picoctf.net/c/407/imp.red
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 18.67.161.51, 18.67.161.101, 18.67.161.8, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|18.67.161.51|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45 [application/octet-stream]
Saving to: ‘imp.red’

imp.red                                100%[============================================================================>]      45  --.-KB/s    in 0s

2024-11-03 11:23:54 (11.4 MB/s) - ‘imp.red’ saved [45/45]
```

After getting the file, it was time to ``cat`` the file and check and see what was present in the file again...
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```
Similar to last time, the mov was present. I wanted to test and see what the conditions were this time...
```
nc saturn.picoctf.net 64814 < imp.red
```
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 0
Ties: 100
Try again. Your warrior (warrior 1) must win at least once.
```

Similar to last time, the challenge here was editing the RED file to make it so that we would win at least once.<br>

At first I tried changing the ``mov`` to a ``mul`` to test and see what would happen.
Sure enough, what I expected to happen, happened:
```
;redcode
;name Imp Ex
;assert 1
mul 0, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mul 0, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
Try again. Your warrior (warrior 1) must win at least once.
```

While scrolling through the CoreWars for Dummies site, I noticed that they had a section on Bombing:
![s17055211032024](https://a.okmd.dev/md/6727601b85a9d.png)

Therefore, what I did was I used the statements that they had and used that to my advantage to hopefully win at least once. Using ``vi imp.red``, I changed the ``mul`` to:
```
;redcode
;name Imp Ex
;assert 1
ADD #10, #-1
MOV 2, @-1
JMP -2, 0
DAT #33, #33
end
```

with that, I ran the ``nc saturn.picoctf.net 64814 < imp.red`` command again and  I got to witness this:
```
\;redcode
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
Warrior 1 wins: 17
Warrior 2 wins: 0
Ties: 83
You did it!
picoCTF{1mp_1n_7h3_cr055h41r5_441be1fc}
```
And there is the flag for this challenge...

### Answer:
```
picoCTF{1mp_1n_7h3_cr055h41r5_441be1fc}
```

### References and Links:
- <a href="http://www.koth.org/info/corewars_for_dummies/dummies.html">CoreWars for Dummies </a>