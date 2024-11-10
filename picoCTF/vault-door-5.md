# <a href="https://play.picoctf.org/practice/challenge/77">vault-door-5</a>
![s16242911102024](https://a.okmd.dev/md/673090e6dce33.png)

This problem stated that we can use tools like the one present in <a href="https://encoding.tools/">``https://encoding.tools/``</a> and other decoding/encoding tools. So I downloaded the file and quickly went to see what was present in the code:

```
public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0";
        return base64Encoded.equals(expected);
    }
```
This time, they are haivng this seperated as three different string and encoding it in urlEncoding first and then into base64. Therefore, when I use the decoding tools, I have to make sure that the decoding that I do, I first use a base64 decoder and then a url decoder.

The first step I did was to convert the three strings into a singular string:
```
"JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0"
```

Then I went to the site and used the tools to first convert the text into base64 decoded text.
```
%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%65%33%31%35%32%62%66%34
```
This was what I got. Then I added the url decoder block to finally get this as the output:
```
c0nv3rt1ng_fr0m_ba5e_64_e3152bf4
```

In the end, it was forming a flowchart diagram that was looking like this:
![s16285611102024](https://a.okmd.dev/md/673091f1c67fa.png)

I used the text that I got in the Java program file, and as expected, it gave "``Access granted!``" output.
```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}
Enter vault password: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}
Access granted.
```

### Answer:
```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}
```

### References and Links:
- <a href= "https://encoding.tools/">Encoding/Decoding Tools</a>