# Implemention of homomorphic addition using RSA

## What is Homorphic Encryption:
Homomorphic encryption is a form of encryption that allows computations to be performed on encrypted data without first having to decrypt it. The resulting computations are left in an encrypted form which, when decrypted, result in an output that is identical to that produced had the operations been performed on the unencrypted data.

## What is RSA:
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest widely used for secure data transmission. In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret.

## How does RSA work:
A basic principle behind RSA is the observation that it is practical to find three very large positive integers e, d, and n, such that for all integers m `(0 ≤ m < n)`, both ``(m^e)^d`` and m have the same remainder when divided by n (they are congruent modulo n).


## Initial Statement:
Implementing homomorphic addition using RSA can be a bit tricky since RSA is inherently multiplicative rather than additive.

## Here's what we can do:
We will use Pailler homomorphic encryption to perform an add and subtract using encrypted values. These homomorphic values will be protected with an RSA public key, and decrypted by a private key. In this case we will generate some time samples, and then determine if the time difference between samples is less than 10 seconds using homomorphic encryption. For this we will use a subtract method. The values for the differences will contain a number of contacts. We will use the homomorphic add to total these up.<br>
<b>C code:</b>
```C[]
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <openssl/err.h>
#include <paillier.h>
#include <time.h>

#define TIME_THRESHOLD 10 // seconds

// Initialize RSA key
RSA* initialize_rsa() {
    RSA* rsa = RSA_generate_key(2048, RSA_F4, NULL, NULL);
    if (rsa == NULL) {
        fprintf(stderr, "RSA key generation failed.\n");
        exit(1);
    }
    return rsa;
}

// Homomorphic addition for Paillier encryption
paillier_ciphertext_t* homomorphic_add(paillier_pubkey_t* pub, paillier_ciphertext_t* c1, paillier_ciphertext_t* c2) {
    paillier_ciphertext_t* sum = paillier_create_enc_zero();
    paillier_mul(pub, sum, c1, c2); // Homomorphic addition in Paillier
    return sum;
}

// Homomorphic subtraction for Paillier encryption (add negative)
paillier_ciphertext_t* homomorphic_subtract(paillier_pubkey_t* pub, paillier_ciphertext_t* c1, mpz_t val) {
    mpz_neg(val, val); // Negate the plaintext value
    paillier_ciphertext_t* encrypted_val = paillier_enc(pub, paillier_create_enc_zero(), paillier_create_plaintext(val), paillier_get_rand_devurandom);
    paillier_ciphertext_t* difference = paillier_create_enc_zero();
    paillier_mul(pub, difference, c1, encrypted_val);
    return difference;
}

// Function to perform homomorphic time difference check
void check_time_difference(paillier_pubkey_t* pub, paillier_prvkey_t* prv, time_t t1, time_t t2) {
    printf("\nTimestamp 1: %ld\n", t1);
    printf("Timestamp 2: %ld\n", t2);

    time_t diff = abs(t2 - t1);
    printf("Time difference: %ld seconds\n", diff);

    paillier_plaintext_t* diff_plain = paillier_plaintext_from_ui(diff);
    paillier_ciphertext_t* encrypted_diff = paillier_enc(pub, paillier_create_enc_zero(), diff_plain, paillier_get_rand_devurandom);

    paillier_plaintext_t* threshold_plain = paillier_plaintext_from_ui(TIME_THRESHOLD);
    paillier_ciphertext_t* threshold_enc = paillier_enc(pub, paillier_create_enc_zero(), threshold_plain, paillier_get_rand_devurandom);

    paillier_ciphertext_t* encrypted_check = homomorphic_subtract(pub, encrypted_diff, threshold_plain->m);

    paillier_plaintext_t* check_result = paillier_dec(prv, pub, encrypted_check);
    long check_value = mpz_get_ui(check_result->m);
    if (check_value > 0) {
        printf("Time difference is less than 10 seconds.\n");
    } else {
        printf("Time difference is 10 seconds or more.\n");
    }

    paillier_freeciphertext(encrypted_diff);
    paillier_freeciphertext(threshold_enc);
    paillier_freeciphertext(encrypted_check);
    paillier_freeplaintext(diff_plain);
    paillier_freeplaintext(threshold_plain);
    paillier_freeplaintext(check_result);
}
```
```
int main() {
    paillier_pubkey_t* pub;
    paillier_prvkey_t* prv;
    paillier_keygen(128, &pub, &prv, paillier_get_rand_devurandom);
    RSA* rsa = initialize_rsa();

    // Test Case 1
    time_t t1 = 1699805401;
    time_t t2 = 1699805405;
    check_time_difference(pub, prv, t1, t2);

    // Test Case 2
    t1 = 1699805401;
    t2 = 1699805423;
    check_time_difference(pub, prv, t1, t2);

    // Test Case 3
    t1 = 1699805401;
    t2 = 1699805408;
    check_time_difference(pub, prv, t1, t2);

    paillier_freepubkey(pub);
    paillier_freeprvkey(prv);
    RSA_free(rsa);

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

