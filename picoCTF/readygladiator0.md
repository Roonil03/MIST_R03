# <a href="https://play.picoctf.org/practice/challenge/368">Ready Gladiator 0</a>
![s16411311032024](https://a.okmd.dev/md/67275a5496c51.png)

Upon launching an instance of this challenge, we are given access to a nc to use the file on.

Initially I was unclear as to what corewars actually was, so I decided to look it up and read upon it's rules and the different movesets that it uses.

![s16423211032024](https://a.okmd.dev/md/67275aa255a84.png)

![s16424611032024](https://a.okmd.dev/md/67275ab06b000.png)

When I originally saw the link, I opened up my WSL and started working.
![s16441611032024](https://a.okmd.dev/md/67275b0a385c0.png)

when i first ran the command:
```
nc saturn.picoctf.net 63406 < imp.red
```

I was greated with the following next:
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
Try again. Your warrior (warrior 1) must lose all rounds, no ties.
```

Naturally I was inclined to first see what was present in the RED file...<br>
So i did `` cat imp.red`` and the following was the result:
```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

I realized that the mov was talking about the movement. If I changed that to NOP, then the bot wouldn't move at all... so I ``vi imp.red`` and changed the RED file's ``mov`` to ``NOP``.

After saving the file, I prompty ran the command again only to be greeted with a lovely flag:
```
;redcode
;name Imp Ex
;assert 1
NOP 0, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
NOP 0, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_be33d1f6}
```

That took some time, but it was surely fun to solve. 

Post the challenge, I prompty deleted the file by ``rm imp.red`` cause I like order :3

### Answer:
```
picoCTF{h3r0_t0_z3r0_4m1r1gh7_be33d1f6}
```

### References and Links:
- <a href="https://www.corewars.org">CoreWars</a>
- <a href="https://corewar.co.uk/standards/cwg.txt">CoreWars Instructions</a>
- <a href="http://www.koth.org/info/corewars_for_dummies/dummies.html">CoreWars For Dummies</a>
- <a href="https://www.redhat.com">Misc Information</a>
