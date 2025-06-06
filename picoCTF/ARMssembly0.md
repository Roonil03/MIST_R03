# <a href="https://play.picoctf.org/practice/challenge/160">ARMssembly 0</a>

![s21263606062025](https://a.okmd.dev/md/68430fb60648b.png)  
We are given the `.s` file, so I tried to find compilers which would run the code. After spending through a lot of sites attempting this, I went to `Perplexity` and asked to convert this ARMv8 asm code into C or an easier language for me to understand.

I then used the converted code to run for our function:
```
#include <stdio.h>
#include <stdlib.h>

// Function to return the maximum of two unsigned integers
unsigned int func1(unsigned int a, unsigned int b) {
    return (a > b) ? a : b;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <num1> <num2>\n", argv[0]);
        return 1;
    }

    // Convert arguments to unsigned integers
    unsigned int num1 = strtoul(argv[1], NULL, 10);
    unsigned int num2 = strtoul(argv[2], NULL, 10);

    // Compute and print the result
    printf("Result: %u\n", func1(num1, num2));
    return 0;
}

```

And this was the result:  
`4134207980`

Thus, I converted it into hex and put the answer!

### Answer:
```
picoCTF{F66B01EC}
```

### References and Links:
- <a href="https://stackoverflow.com/questions/10285410/what-are-s-files">S Files</a>
- <a href="https://www.perplexity.ai">Perplexity AI</a>
- <a href="https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=4134207980">Decimal to Hex Convertor</a>