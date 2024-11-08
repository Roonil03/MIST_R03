# <a href="https://play.picoctf.org/practice/challenge/7">vault-door-training</a>
![s09274111082024](https://a.okmd.dev/md/672d8c3e0a60a.png)

After reading the problem statement, I thought that I would be needing to change the source code of the file in order to get some message that would be encrypted, in turn leading me to the flag of this question...

Therefore, I booted up my ``WSL`` and got the file into my system.
```
wget https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java
```
```
--2024-11-08 03:56:00--  https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 943 [application/octet-stream]
Saving to: ‘VaultDoorTraining.java’

VaultDoorTraining.java                 100%[============================================================================>]     943  --.-KB/s    in 0s

2024-11-08 03:56:01 (327 MB/s) - ‘VaultDoorTraining.java’ saved [943/943]
```

After getting the file into my system, I ``cat`` the file to see what was present in the file.
```
 cat VaultDoorTraining.java
```
```
class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");
    }
}
```

and there was the flag just sitting there in the program itself. I just copy pasted the flag and got my answer.

Post this, as usual, I promptly deleted the file from my system:
```
rm VaultDoorTraining.java
```
### Answer:
```
picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}
```

### References and Links:
<i>NULL</i>