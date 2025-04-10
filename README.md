# simplesteganography
A very basic steganography program I wrote in Python for fun :) 

Uses LSB (Least-Significant-Bits) to encode your password into an image. 

A very small extraction script is also in stego.py, I wrote it just to confirm if the encoding had happened properly. 

If you have no need for extraction, use the second file (stego_hash.py). This file is almost the same. but encrypts your password to SHA256 before translating it to binary. This makes it almost impossible for a third party to gain access to your password by reverse engineering. 

