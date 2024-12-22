# <a href="https://play.picoctf.org/practice/challenge/288">Power Cookie</a>

![s23484212222024](https://a.okmd.dev/md/67685806ad258.png)

With this, we can see that there are a few things to explore with this link, one is the `js` files and the other is it's interactions with requests.

At first, I inspected the site and saw that there was a js file called `guest.js` that contained the following contents:
```
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

With this, what I did next was find a way to check the `php` file, which just brought me to the site that stated that there is no guest feature.

The next thing I did is open burp and saw the request that it was sending when I press `Continue as guest`'s button.

It was evident that there was a variable to change, so I changed the isAdmin from 0 to 1.

and boom, there was the flag...

### Answer:
```
picoCTF{gr4d3_A_c00k13_65fd1e1a}
```