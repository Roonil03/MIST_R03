# <a href="https://play.picoctf.org/practice/challenge/106">ARMssembly 3</a>

![s21321406062025](https://a.okmd.dev/md/6843110828df1.png)

Another challenge in the series, the first thing that I did is convert the .s to a .c, and then see what I could manipulate.
Here's the code that I got generated from `Perplexity`:
```C
#include <stdio.h>
#include <stdlib.h>

int func2(int a) {
    return a + 3;
}

int func1(int n) {
    int result = 0;
    while (n != 0) {
        if (n & 1) {         
            result = func2(result);
        }
        n = n >> 1;          
    }
    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }
    
    int input = atoi(argv[1]);
    int result = func1(input);
    printf("Result: %d\n", result);
    
    return 0;
}
```

After editing the code a bit, I landed with this:
```C
#include <stdio.h>
#include <stdlib.h>

int func2(int a) {
    return a + 3;
}

unsigned int func1(unsigned int n) {
    unsigned int result = 0;
    while (n != 0) {
        if (n & 1) {  
            result = func2(result);
        }
        n = n >> 1;       
    }
    return result;
}

int main() {
    
    unsigned int input = (3350728462);
    unsigned int result = func1(input);
    printf("Result: %u\n", result);
    
    return 0;
}
```

After this was done, I ran the program and this was the output:  
`48`

I put this throught the Decimal to Hex to get the final answer!

### Answer:
```
picoCTF{00000030}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=48">Decimal to Hex Converter</a>
- <a href="https://www.programiz.com/c-programming/online-compiler/">Online C</a>
- <a href="https://www.perplexity.ai/">Perplexity</a>