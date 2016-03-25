# CryptoAlgorithmChallenge
A Simple Encryption Algorithm

## Description
This repository contains a simple block encryption algorithm in the
file named `cac.py`. It is a Python script that provides some basic
functions for block operations and a demonstration of the tool.

The current algorithm is very simple and may have some problems here
and there. Your task is to improve it!

This code is a very bad symmetric key cryptographic algorithm. It should
never be used for anything other than experimentation and fun. A good
rule of thumb is: **NEVER WRITE YOUR OWN CRYPTO**. This repository has
been created for educational purposes. You can fork it and play with it
and compare your solution to others' to determine the best algorithm in
terms of performance and security.

## How it works
The code is very simple and the tutorial has a lot of messages that are
very descriptive. You can run this script and see that for yourself.
The algorithm followed is also very simple. It uses a property of XOR
to be reversible yet need a key for this. Each time you run this, a random
128-bit key is generated.

Now go and play with it! Here are a few questions for you to answer:

* What happens if you increase the rounds to 5? What about 6? 7? 8?
* Do you see a problem with the second round of decryption?
* How can you solve this problem? Change the algorithm and write the code!
