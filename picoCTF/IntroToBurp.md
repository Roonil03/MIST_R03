# <a href="https://play.picoctf.org/practice/challenge/419">IntroToBurp</a>

![s00575612222024](https://a.okmd.dev/md/676716bf36351.png)

After starting the instance, it was clear as the name suggested that I would be needing to use Burp to figure out the answer for this problem.

With that, I decided to explore what the site was doing initialy.
It started of with filling some normal details, like name, password, etc.<br>
Then there was a page that went 2fa OTP.

What happened here was, whatever you put, it would always return as:
```
Invalid OTP!
```

So I started BurpSuite and started intercepting the requests and posts.

Then what I did was focus on OTP part. At first I tried to find and see if there was any pasword that was hidden in the files iteslf... Which wasn't present.

Then I decided to look for an answer by looking into the otp, by just removing it from the `Raw`.
I just forwarded that request, and endedd up on this page:
```
Welcome, q you sucessfully bypassed the OTP request. Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_2e80f1fd}
```
and easily found the answer.

### Answer:
```
picoCTF{#0TP_Bypvss_SuCc3$S_2e80f1fd}
```

### References and Links:
<i>Null</i>