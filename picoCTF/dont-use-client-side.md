# <a href="https://play.picoctf.org/practice/challenge/66">dont-use-client-side</a>

![s01123312222024](https://a.okmd.dev/md/67671a2d2a585.png)

There was directly a site that we had to go off with, so all that I could do is explore this. WHen I opened the link, the first  thing that I did is check the inspect element and the code behind the site, and I found something really interseting in the `<script>` component.
```
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '723c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_7') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'e}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
```

Thus, I could see that it was the password (aka the flag) that was deconstructed into smaller substrings, so it just a small task to just join them together.<br>
And thus with that, I managed to concatenate all of them for the answer:

### Answer:
```
picoCTF{no_clients_plz_7723ce}
```