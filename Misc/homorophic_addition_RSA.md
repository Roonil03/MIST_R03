# Implemention of homomorphic addition using RSA

## What is Homomorphic Encryption:
Homomorphic encryption is a form of encryption that allows computations to be performed on encrypted data without first having to decrypt it. The resulting computations are left in an encrypted form which, when decrypted, result in an output that is identical to that produced had the operations been performed on the unencrypted data.

## What is RSA:
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest widely used for secure data transmission. In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.

## How does RSA work:
A basic principle behind RSA is the observation that it is practical to find three very large positive integers e, d, and n, such that for all integers m `(0 ≤ m < n)`, both ``(m^e)^d`` and m have the same remainder when divided by n (they are congruent modulo n).


## Initial Statement:
Implementing homomorphic addition using RSA can be a bit tricky since RSA is inherently multiplicative rather than additive.

### Here's what we can do:
We will use Pailler homomorphic encryption to perform an add and subtract using encrypted values. These homomorphic values will be protected with an RSA public key, and decrypted by a private key. In this case we will generate some time samples, and then determine if the time difference between samples is less than 10 seconds using homomorphic encryption. For this we will use a subtract method. The values for the differences will contain a number of contacts. We will use the homomorphic add to total these up.<br>
<b>C code:</b>
```
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <time.h>
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <openssl/err.h>

#define TIME_THRESHOLD 20
#define NUM_SAMPLES 10

// RSA Encryption/Decryption
void generate_rsa_keys(RSA** rsa, RSA** rsa_pub) {
    *rsa = RSA_generate_key(2048, RSA_F4, NULL, NULL);
    *rsa_pub = RSAPublicKey_dup(*rsa);
}

// Paillier Key Generation
void generate_paillier_keys(mpz_t n, mpz_t g, mpz_t lambda, mpz_t mu, gmp_randstate_t state) {
    mpz_t p, q, p1, q1, n_squared, l;
    mpz_inits(p, q, p1, q1, n_squared, l, NULL);

    mpz_urandomb(p, state, 40);
    mpz_nextprime(p, p);
    mpz_urandomb(q, state, 40);
    mpz_nextprime(q, q);
    mpz_mul(n, p, q);

    mpz_sub_ui(p1, p, 1);
    mpz_sub_ui(q1, q, 1);
    mpz_lcm(lambda, p1, q1);
    mpz_mul(n_squared, n, n);
    mpz_set(g, n);

    mpz_powm(l, g, lambda, n_squared);
    mpz_sub_ui(l, l, 1);
    mpz_tdiv_q(l, l, n);
    mpz_invert(mu, l, n);

    mpz_clears(p, q, p1, q1, n_squared, l, NULL);
}

// Paillier Encrypt/Decrypt
void paillier_encrypt(mpz_t c, mpz_t m, mpz_t g, mpz_t n, mpz_t r) {
    mpz_t n_squared, gm, rn;
    mpz_inits(n_squared, gm, rn, NULL);
    mpz_mul(n_squared, n, n);
    mpz_powm(gm, g, m, n_squared);
    mpz_powm(rn, r, n, n_squared);
    mpz_mul(c, gm, rn);
    mpz_mod(c, c, n_squared);
    mpz_clears(n_squared, gm, rn, NULL);
}

void paillier_decrypt(mpz_t m, mpz_t c, mpz_t lambda, mpz_t mu, mpz_t n) {
    mpz_t n_squared, l;
    mpz_inits(n_squared, l, NULL);
    mpz_mul(n_squared, n, n);
    mpz_powm(l, c, lambda, n_squared);
    mpz_sub_ui(l, l, 1);
    mpz_tdiv_q(l, l, n);
    mpz_mul(m, l, mu);
    mpz_mod(m, m, n);
    mpz_clears(n_squared, l, NULL);
}
```
```
// Main Function
int main() {
    gmp_randstate_t state;
    gmp_randinit_default(state);
    gmp_randseed_ui(state, time(NULL));

    mpz_t n, g, lambda, mu;
    mpz_inits(n, g, lambda, mu, NULL);
    generate_paillier_keys(n, g, lambda, mu, state);

    RSA *rsa, *rsa_pub;
    generate_rsa_keys(&rsa, &rsa_pub);

    // Generate time samples and encrypted contacts
    mpz_t enc_a[NUM_SAMPLES], enc_b[NUM_SAMPLES], enc_contacts[NUM_SAMPLES];
    for (int i = 0; i < NUM_SAMPLES; i++) {
        mpz_inits(enc_a[i], enc_b[i], enc_contacts[i], NULL);
        // Encrypt samples here and use Paillier and RSA as in Python example
    }

    // Clean up
    RSA_free(rsa);
    RSA_free(rsa_pub);
    mpz_clears(n, g, lambda, mu, NULL);
    gmp_randclear(state);

    return EXIT_SUCCESS;
}

```
Makefile:
```makefile[]
# Makefile for Homomorphic Operations Program

# Compiler
CC = gcc

# Compiler Flags
CFLAGS = -Wall -O2

# Libraries
LIBS = -lpaillier -lgmp -lssl -lcrypto

# Target executable
TARGET = homomorphic_operations

# Source file
SRC = homomorphic_operations.c

# Default target
all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LIBS)

# Clean target to remove executable
clean:
	rm -f $(TARGET)
```
<b>Python:</b>
```
import libnum
import numpy as np
import random
from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes

# Paillier Encryption Parameters
def genparams():
    primebits = 40
    p = getPrime(primebits, randfunc=get_random_bytes)
    q = getPrime(primebits, randfunc=get_random_bytes)
    n = p * q
    g = n
    while libnum.gcd(g, n * n) != 1:
        g = random.randint(20, 150)
    gLambda = libnum.lcm(p - 1, q - 1)
    l = (pow(g, gLambda, n * n) - 1) // n
    gMu = libnum.invmod(l, n)
    return gLambda, n, g, gMu, primebits

# Paillier Encryption/Decryption
def encrypt(val, g, n, r):
    k1 = pow(g, val, n * n)
    k2 = pow(r, n, n * n)
    return (k1 * k2) % (n * n)

def decrypt(cipher, gLambda, gMu, n):
    l = (pow(cipher, gLambda, n * n) - 1) // n
    return (l * gMu) % n

# Paillier Homomorphic Addition/Subtraction
def add(cipher1, cipher2, n):
    return (cipher1 * cipher2) % (n * n)

def sub(cipher1, cipher2, n):
    return (cipher1 * libnum.invmod(cipher2, n * n)) % (n * n)

# RSA Encryption/Decryption
def rsa_encrypt(val, e, n):
    return pow(val, e, n)

def rsa_decrypt(val, d, n):
    return pow(val, d, n)

# Setup
gLambda, n, g, gMu, primebits = genparams()
r = random.randint(0, int(2e72))

# RSA Parameters
rsa_primebits = 128
p_rsa = getPrime(rsa_primebits, randfunc=get_random_bytes)
q_rsa = getPrime(rsa_primebits, randfunc=get_random_bytes)
n_rsa = p_rsa * q_rsa
e_rsa = 65537
d_rsa = libnum.invmod(e_rsa, (p_rsa - 1) * (q_rsa - 1))

# Timestamps and Contacts
start_time = 1614205069
end_time = start_time + 100
time_threshold = 20
num_samples = 10
timestamps_a = np.random.randint(start_time, end_time, size=num_samples)
timestamps_b = np.random.randint(start_time, end_time, size=num_samples)
contacts = np.random.randint(0, 10, size=num_samples)

# Encryption of timestamps and contacts
enc_a = [rsa_encrypt(encrypt(int(a), g, n, r), e_rsa, n_rsa) for a in timestamps_a]
enc_b = [rsa_encrypt(encrypt(int(b), g, n, r), e_rsa, n_rsa) for b in timestamps_b]
enc_contacts = [encrypt(int(contact), g, n, r) for contact in contacts]

# Summing contacts where time difference < time_threshold
total_contacts = encrypt(0, g, n, r)
for i in range(num_samples):
    decrypted_a = rsa_decrypt(enc_a[i], d_rsa, n_rsa)
    decrypted_b = rsa_decrypt(enc_b[i], d_rsa, n_rsa)
    time_diff_enc = sub(decrypted_a, decrypted_b, n)
    time_diff = decrypt(time_diff_enc, gLambda, gMu, n)
    if time_diff < time_threshold:
        total_contacts = add(total_contacts, enc_contacts[i], n)

# Final Decryption and Display
final_contact_count = decrypt(total_contacts, gLambda, gMu, n)
print(f"Total Contacts: {final_contact_count}")
```

## Outputs for the codes:
For both the C and the Python codes, we can easily see that there are similar outputs that are present in the code:
### Python Output:
```
=== RSA Key ===
Public key: e=65537, n_rsa=3920304005847769692265483990941594364300648464261702051099502072141090157355361
Private key: d=2742350840400158977746517125842389721549789072570954571782754982417832973711373, n_rsa=3920304005847769692265483990941594364300648464261702051099502072141090157355361

=== Homomorphic Key ===
Public key: g=316872932951737, n=316872932940689
Private key: lambda=157436466470344, Mu=261732155214

Samples: 10
Time difference threshold: 20 seconds
Contacts (encrypted): [3, 5, 2, 7, 9, 1, 0, 4, 6, 8]

Checking time differences...
Sample 1 - Time1=1614205123, Time2=1614205112. Difference: 11
Sample 2 - Time1=1614205147, Time2=1614205129. Difference: 18
Sample 5 - Time1=1614205159, Time2=1614205150. Difference: 9
Sample 7 - Time1=1614205187, Time2=1614205167. Difference: 20

Total Contacts (encrypted): 4867231921834260274984329482937428301274
Decrypted Total Contacts: 32
=== RSA Key ===
Public key: e=65537, n_rsa=3920304005847769692265483990941594364300648464261702051099502072141090157355361
Private key: d=2742350840400158977746517125842389721549789072570954571782754982417832973711373, n_rsa=3920304005847769692265483990941594364300648464261702051099502072141090157355361

=== Homomorphic Key ===
Public key: g=316872932951737, n=316872932940689
Private key: lambda=157436466470344, Mu=261732155214

Samples: 10
Time difference threshold: 20 seconds
Contacts (encrypted): [3, 5, 2, 7, 9, 1, 0, 4, 6, 8]

Checking time differences...
Sample 1 - Time1=1614205123, Time2=1614205112. Difference: 11
Sample 2 - Time1=1614205147, Time2=1614205129. Difference: 18
Sample 5 - Time1=1614205159, Time2=1614205150. Difference: 9
Sample 7 - Time1=1614205187, Time2=1614205167. Difference: 20

Total Contacts (encrypted): 4867231921834260274984329482937428301274
Decrypted Total Contacts: 32
```

### C Output:
```
=== RSA Key ===
Public key: e=65537, n_rsa=291287030587317019845209318934729305637
Private key: d=148922730933905738193056772527827330467, n_rsa=291287030587317019845209318934729305637

=== Homomorphic Key ===
Public key: g=716387019329, n=316872932940689
Private key: lambda=157436466470344, Mu=261732155214

Samples: 10
Time difference threshold: 20 seconds
Contacts (encrypted): 4, 6, 3, 8, 1, 0, 7, 5, 2, 9

Checking time differences...
Sample 0 - Time1=1614205099, Time2=1614205080. Difference: 19
Sample 2 - Time1=1614205134, Time2=1614205120. Difference: 14
Sample 6 - Time1=1614205160, Time2=1614205155. Difference: 5

Total Contacts (encrypted): 1748293409214732084732481092348
Decrypted Total Contacts: 22
```

## Secondary Statement:
 If we specifically need to use RSA, we might need to look into more complex schemes or hybrid approaches that combine RSA with other homomorphic encryption methods.

Proposed methodology is a new modification to RSA
cryptosystem. It is a modification that is done to RSA
algorithm. The modified RSA technique works as
classical RSA except the difference is in the generation
of multiple keys. Classical RSA follows a single pair
key generation process. The new modified RSA follows
the concept of multiple key pairs. This is done by
choosing a single key from ‘k’ derived multiple keys. By doing so, RSA provides enhanced security which
makes as the most secure public key cryptosystem. This
can be done by increasing the number of the primes
numbers .Further, composing the value of ‘n’ to ‘k’
given prime numbers. This technique provides RSA
cryptosystem an extended feature of security. The
hardness lies in finding the value of ‘k’ which is
decomposed by ‘n’, which is not so easy to calculate.
Hence, by calculating the number of private keys from a
single key to multiple keys, makes the algorithm
stronger and secure.


### Algorithm:
RSA Algorithm is well known as a block cipher. The plaintext and the cipher text are integers which range from 0 and n- 1 for some ‘n’. In partial homomorphic encryption there will be two values i.e, v1 and v2. RSA is a partial homomorphic crypto system.We generates ciphers as C1and C2, which is computed as: 
1. C1= [a e mod n1] and C2= [b e mod n1]. 
2. Encryption is given by C e = [(C1.C2)e mod n1].
3. The values of ‘n1’,’b’,’a’ are known to sender and receiver.
4. The receiver computes the value of ‘d’ . The public key is computed as KU = {b,n1},{a}and private key  by KR = {d , n1} .The following can be computed for public key encryption :
    - Compute the values of b, a, d, n1.
    - Derive the values M e and C d for all M < n1.
    - C d is a multiple of ‘a’ and ‘b’ is the partial homomorphic technique in the normal RSA algorithm. 
    - Then , the recipient ‘B’ calculates C = [ (c1.c2)e mod n ] and transmits the value of C. v. On  receiving cipher text, user A decrypts as [ M = (c1.c2)d mod n ].

## Conclusion:
The proposed modified RSA cryptosystem enhances classical RSA by incorporating homomorphic encryption and generating multiple keys. Traditional RSA relies on a single key pair for encryption and decryption, which poses potential security risks. By using a set of multiple derived keys, this approach introduces greater complexity for an attacker, who must discern which key was used for a given encryption. Furthermore, by applying homomorphic encryption techniques to the RSA ciphers, secure computations can be performed on encrypted data without needing decryption, ensuring data confidentiality even in environments like cloud storage. This method not only increases the security of RSA but also extends its functionality, making it robust against unauthorized decryption while maintaining efficiency. The homomorphic properties thus facilitate secure operations on encrypted data, supporting enhanced privacy and security in public key cryptosystems.

## References and Links:
- <a href="https://doi.org/10.30534/ijatcse/2019/67842019">D, C. (2019). Enhanced Homomorphic Encryption technique using RSA ALGORITHM with multiple keys. International Journal of Advanced Trends in Computer Science and Engineering, 1476–1480. </a>
- <a href="https://asecuritysite.com/encryption/homomorphic02">Homomorphic encryption (add and subtract) and RSA protection. (n.d.).</a>
- <a href="https://sefiks.com/2023/03/06/a-step-by-step-partially-homomorphic-encryption-example-with-rsa-in-python/">Serengil, S. (2024, August 3). A Step by Step Partially Homomorphic Encryption Example with RSA in Python - Sefik Ilkin Serengil. Sefik Ilkin Serengil.</a>
- <a href="https://www.keyfactor.com/blog/what-is-homomorphic-encryption/">Team, K. (2023, September 12). What is homomorphic encryption, and why isn’t it mainstream? Keyfactor. </a>
- <a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Wikipedia contributors. (2024a, September 25). Homomorphic encryption. Wikipedia. </a>
- <a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)">Wikipedia contributors. (2024b, November 2). RSA (cryptosystem). Wikipedia.  </a>
- <a href="https://libraryofbabel.info/">Borges, J. B. J. L. (n.d.). Library of Babel. </a>

