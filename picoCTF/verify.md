# <a href="https://play.picoctf.org/practice/challenge/450">Verify</a>
![s20310011042024](https://a.okmd.dev/md/6728e1b037b61.png)

A web forensics challenge... that is certainly something that I haven't solved in a long time. 

Reading the first hints, it was clear that I was going to be needing some manual reading to do...<br>
So I hoped on the net to figure out what exactly was this ``sha-256`` that they were talking about was exactly...
```
The  md5, sha1, sha224, sha256, sha384, sha512, sha512t224, sha512t256, 
rmd160, skein256, skein512, and skein1024 utilities  take  as  input  a
message	of  arbitrary  length and produce as output a "fingerprint" or
"message	digest"	of the input.

The  md5sum,  sha1sum,  sha224sum,  sha256sum,  sha384sum,   sha512sum,
sha512t224sum,  sha512t256sum, rmd160sum, skein256sum, skein512sum, and
skein1024sum utilities do the same, but with command-line  options  and
an  output  format  that	match those of their similary named GNU	utili-
ties.

The shasum utility does the same, but with command-line options and  an
output  format  that  match  those  of the similarly named utility that
ships with Perl.

In all cases, each file listed on the command line is  processed	 sepa-
rately.	 If no files are listed	on the command line, or	a file name is
given as	-, input is taken from stdin instead.

It is conjectured that it is computationally infeasible to produce  two
messages	having the same	message	digest,	or to produce any message hav-
ing  a given prespecified target	message	digest.	 The SHA-224 , SHA-256
, SHA-384 , SHA-512, RIPEMD-160,	and SKEIN algorithms are intended  for
digital signature applications, where a large file must be "compressed"
in  a  secure manner before being encrypted with	a private (secret) key
under a public-key cryptosystem such as RSA.

The MD5 and SHA-1 algorithms have been proven to	be vulnerable to prac-
tical collision attacks and should not be relied	upon to	produce	unique
outputs,	nor should they	be used	as part	of a  cryptographic  signature
scheme.	As of 2017-03-02, there	is no publicly known method to reverse
either algorithm, i.e., to find an input	that produces a	specific  out-
put.

SHA-512t256  is	a  version  of SHA-512 truncated to only 256 bits.  On
64-bit hardware,	 this  algorithm  is  approximately  50%  faster  than
SHA-256 but with	the same level of security.  The hashes	are not	inter-
changeable.

SHA-512t224  is identical to SHA-512t256, but with the digest truncated
to 224 bits.

It is recommended that all new applications use	SHA-512	 or  SKEIN-512
instead of one of the other hash	functions.
```

That still didn't clear up some doubts I had, so I did some more digging on what the sum suffixes were.
I went to search specifically for the ``sha256sum`` command as I felt that it had some importance with this question...
and sure enough, the online ``man`` page landed me on this:
```
Print or check SHA256 (256-bit) checksums. 
```

All I needed to do was ``grep`` the contents of the checksum after piping it, and we should have our flag...

So I logged in:
```
ssh -p 60435 ctf-player@rhea.picoctf.net
```
```
The authenticity of host '[rhea.picoctf.net]:60435 ([3.136.191.228]:60435)' can't be established.
ED25519 key fingerprint is SHA256:QKdv+RGJL0UYRDM66IiGQ5dsXOX7DQFqB7umTylh+IU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[rhea.picoctf.net]:60435' (ED25519) to the list of known hosts.
ctf-player@rhea.picoctf.net's password:
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1016-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.
```

That was certainly interesting...

I used ``ls`` to see what all files were present in the directory:
```
checksum.txt  decrypt.sh  files
```

Just ``cat`` the ``checksum.txt`` to get:
```
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
```

Now, all I had to do was use the command:
```
sha256sum files/* | grep 03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
```
Which would check for that checksum in all the files in ``files``.

The output we got was the name of the file:
```
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8  files/00011a60
```

Finally, all we need to do is use the ``decrypt.sh`` and get the final answer, with which we:
```
./decrypt.sh  files/00011a60
```
```
picoCTF{trust_but_verify_00011a60}
```
Have our flag!

### Answer:
```
picoCTF{trust_but_verify_00011a60}
```

### References and Links:
- <a href="https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm">SHA-256</a>
- <a href="https://man7.org/linux/man-pages/man1/grep.1.html">``man`` grep</a>
- <a href="https://man.freebsd.org/cgi/man.cgi?query=sha256&sektion=1">``man`` sha256</a>
- <a href="https://linux.die.net/man/1/sha256sum">``man`` sha256sum</a>