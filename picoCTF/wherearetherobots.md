# <a href="https://play.picoctf.org/practice/challenge/4"> where are the robots</a>

![s01284312222024](https://a.okmd.dev/md/67671df6b0a67.png)

This was the introduction to get into Robots.txt and their subsection of problems in Web Exploitation.

So as soon as we got the site, we append the `/robots.txt` tag to the site to get access to this portion of the website:
```
User-agent: *
Disallow: /477ce.html
```
This means that for all users, this particular site is disallowed.

So all we need to do is instead of `/robots.txt`, all we need to do is append this particular link, and then we get out flag!

### Answer:
```
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
```