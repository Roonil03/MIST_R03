# <a href="https://play.picoctf.org/practice/challenge/248"> PW Crack 4 </a>

![s21545306062025](https://a.okmd.dev/md/6843165775bea.png)  
This problem was similar to the previous problem, but this time, I had to actually alter the code so that I can be a little more efficient with the bruteforcing.

I first created a copy of the code, and then changed it to add a for-loop to iterate through the entire list of possible passwords.
```Python
pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f", "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1", "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee", "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d", "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9", "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837", "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e", "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]
    for i in range(100):
        user_pw = pos_pw_list[i]
        user_pw_hash = hash_pw(user_pw)
        if(user_pw_hash == correct_pw_hash):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        print(i, "That password is incorrect")
```

With this, I just simply ran the program to get this output:
```
Please enter correct password for flag: wae
0 That password is incorrect
1 That password is incorrect
2 That password is incorrect
3 That password is incorrect
4 That password is incorrect
5 That password is incorrect
6 That password is incorrect
7 That password is incorrect
8 That password is incorrect
9 That password is incorrect
10 That password is incorrect
11 That password is incorrect
12 That password is incorrect
13 That password is incorrect
14 That password is incorrect
15 That password is incorrect
16 That password is incorrect
17 That password is incorrect
18 That password is incorrect
19 That password is incorrect
20 That password is incorrect
21 That password is incorrect
22 That password is incorrect
23 That password is incorrect
24 That password is incorrect
25 That password is incorrect
26 That password is incorrect
27 That password is incorrect
28 That password is incorrect
29 That password is incorrect
30 That password is incorrect
31 That password is incorrect
32 That password is incorrect
33 That password is incorrect
34 That password is incorrect
35 That password is incorrect
36 That password is incorrect
37 That password is incorrect
38 That password is incorrect
39 That password is incorrect
40 That password is incorrect
41 That password is incorrect
42 That password is incorrect
43 That password is incorrect
44 That password is incorrect
45 That password is incorrect
46 That password is incorrect
47 That password is incorrect
48 That password is incorrect
49 That password is incorrect
50 That password is incorrect
51 That password is incorrect
52 That password is incorrect
53 That password is incorrect
54 That password is incorrect
55 That password is incorrect
56 That password is incorrect
57 That password is incorrect
58 That password is incorrect
59 That password is incorrect
60 That password is incorrect
61 That password is incorrect
62 That password is incorrect
63 That password is incorrect
64 That password is incorrect
65 That password is incorrect
66 That password is incorrect
67 That password is incorrect
68 That password is incorrect
69 That password is incorrect
70 That password is incorrect
71 That password is incorrect
72 That password is incorrect
73 That password is incorrect
74 That password is incorrect
75 That password is incorrect
76 That password is incorrect
77 That password is incorrect
78 That password is incorrect
79 That password is incorrect
80 That password is incorrect
81 That password is incorrect
82 That password is incorrect
83 That password is incorrect
84 That password is incorrect
85 That password is incorrect
86 That password is incorrect
87 That password is incorrect
88 That password is incorrect
89 That password is incorrect
90 That password is incorrect
91 That password is incorrect
92 That password is incorrect
93 That password is incorrect
94 That password is incorrect
95 That password is incorrect
96 That password is incorrect
97 That password is incorrect
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_cf341ff1}
```

And thus, with that I can determine that the 99th answer was the correct password for this problem.

### Answer:
```
picoCTF{fl45h_5pr1ng1ng_cf341ff1}
```

### References and Links:
*NULL*