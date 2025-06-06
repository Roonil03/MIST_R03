# <a href="https://play.picoctf.org/practice/challenge/111">ARMssembly 1</a>

![s21285206062025](https://a.okmd.dev/md/6843103e86b02.png)

This challenge again gave us the assembly code that we needed to work with. Starting off with the code, I sent it into `Perplexity`  again to get my code converted into C.

From there onwards, I saw this:
```C
#include <stdio.h>
#include <stdlib.h>

int func(int a) {
    int local1 = 79;
    int local2 = 7;
    int local3 = 3;
    
    int result = local1 << local2;  
    result = result / local3;       
    result = result - a;         
    
    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }
    
    int input = atoi(argv[1]);
    int result = func(input);
    
    if (result == 0) {
        printf("You win!\n");
    } else {
        printf("You Lose :(\n");
    }
    
    return 0;
}
```

Therefore, I edited the code to perform this:
```
printf("%d", result);
```

This would give me the result that would make result 0 and thus giving me the right flag!
This gave me the result:
```
3370
```

I prompt converted it into hex and then submitted the flag.

### Answer:
```
picoCTF{00000D2A}
```

### References and Links:
- <a href="https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=3370"> Decimal to Hex convertor</a>
- <a href="https://www.perplexity.ai"> Perplexity</a>
- <a href="https://www.programiz.com/c-programming/online-compiler"> Online C</a>

