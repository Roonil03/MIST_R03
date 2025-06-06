# <a href="https://play.picoctf.org/practice/challenge/183">ARMssembly 4</a>

![s21331906062025](https://a.okmd.dev/md/6843114960f13.png)  
Like the previous challenges in this series, the first step I took is converting this assembly code into C so that I can read and understand the code better.
```C
#include <stdio.h>
#include <stdlib.h>

int func8(int a) {
    return a + 2;
}

int func5(int a) {
    return func8(a);
}

int func4(int a) {
    int local = 17;
    func1(local); 
    return a;
}

int func7(int a) {
    return (a > 100) ? a : 7;
}

int func3(int a) {
    return func7(a);
}

int func2(int a) {
    if (a <= 499) {
        return func4(a - 86);
    } else {
        return func5(a + 13);
    }
}

int func1(int a) {
    if (a > 100) {
        return func2(a + 100);
    } else {
        return func3(a);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }
    
    int input = atoi(argv[1]);
    printf("Result: %d\n", func1(input));
    return 0;
}
```

I changed around the code a bit and this is what I landed up with, so that I could get the proper result:
```C
#include <stdio.h>
#include <stdlib.h>

unsigned int func1(unsigned int);

unsigned int func8(unsigned int a) {
    return a + 2;
}

unsigned int func5(unsigned int a) {
    return func8(a);
}

unsigned int func4(unsigned int a) {
    unsigned int local = 17;
    func1(local);  
    return a;
}

unsigned int func7(unsigned int a) {
    return (a > 100) ? a : 7;
}

unsigned int func3(unsigned int a) {
    return func7(a);
}

unsigned int func2(unsigned int a) {
    if (a <= 499) {
        return func4(a - 86);
    } else {
        return func5(a + 13);
    }
}

unsigned int func1(unsigned int a) {
    if (a > 100) {
        return func2(a + 100);
    } else {
        return func3(a);
    }
}

int main() {
    unsigned int input = 2907278761;
    printf("Result: %u\n", func1(input));
    return 0;
}
```

After running the program, this was the answer that we get:  
`2907278876`

and thus, I converted it to hex and got the right answer!

### Answer:
```
picoCTF{AD498E1C}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=2907278876"> Decimal to Hex Converter</a>
- <a href="https://www.perplexity.ai/"> Perplexity</a>
- <a href="https://www.programiz.com/c-programming/online-compiler/"> Online C</a>