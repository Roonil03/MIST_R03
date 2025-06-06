# <a href="https://play.picoctf.org/practice/challenge/150"> ARMssembly 2</a>

![s21305406062025](https://a.okmd.dev/md/684310b863444.png)  
I got this program and then I changed it to C, as usual, with the help of `Perplexity`.

This the code that I received:
```C
#include <stdio.h>
#include <stdlib.h>

int func1(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += 3;
    }
    return sum;
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

With this, I edited the code to get this:
```C
#include <stdio.h>
#include <stdlib.h>

int func1(unsigned int n) {
    unsigned int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += 3;
    }
    return sum;
}

int main() {
    unsigned int input = 4189673334;
    unsigned int result = func1(input);
    printf("Result: %u\n", result);
    
    return 0;
}
```

With this, I directly got my output:  
`3979085410`

After this, I just converted it to hex to get the output.

### Answer:
```
picoCTF{ED2C0662}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=3979085410"> Decimal to Hex Converter</a>
- <a href="https://www.perplexity.ai/">Perplexity</a>
- <a href="https://www.programiz.com/c-programming/online-compiler/">Online C</a>
- <a href="https://stackoverflow.com/questions/32344810/unsigned-values-in-c">Printing unsigned values</a>