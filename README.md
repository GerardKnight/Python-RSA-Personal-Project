RSA encryption as a personal project. The main function is in rsa.py, so run that.

Instruction for use~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To encrypt a message:
1. Insert the public key of the person you wish to send the message to, using option 4.
2. Write the message. The result will look like an array of large integers, like [1234567890,0987654321]. Send this to the person.

To decrypt a message.
1. Generate or insert a public and private key, using options 1 or 2.
2. Send your public key to anyone you wish to receive messages from.
3. They will send an encrypted message, similar to the one seen above.
4. Select option 7 and type in the message they sent. It will then be decrypted and printed.

You can print your keys using option 3 and theirs using option 5. You will need to do this to share your key. You can also use these options to save the keys for later use. Do not share the private key.

Explainers for the code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A full explainer for the mathematics behind the RSA algorithm can be found at its Wikipedia page: https://en.wikipedia.org/wiki/RSA_cryptosystem

It relies heavily on complex modular arithmetic. Included in rsa_primes.py is a fast modular exponentiation function, which can perform these operation relatively fast. This is necessary to use large numbers for the keys.

The public key consists of the product of two very large prime numbers. To find a large prime number, we guess a large number and check if it is prime using the Miller-Rabin primality test. This test is fast, scales well for large numbers. While theoretically it returns false-positives, the odds are extremely low.
The private key is more complex to explain. It is represented by d in the Wikipedia page.

e is always 2^31-1, as using a single value reduces the complexity of the code and does not alter its performance.

Please find also these explainers of the Miller-Rabin primality test:
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
https://www.youtube.com/watch?v=tBzaMfV94uA
