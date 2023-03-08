#plain hex ful 48656c6c6f2c20746869732069732061 207075626c6963206d6573736167652e 2054686973206d65737361676520636f 6e7461696e73206e6f20666c6167732e
#encrypted ful de49b7bb8e3c5e9ed51905b6de326b39 b102c7a6f0e09e92fe398c75d032b411 89b11f873c6cd8cdb65a276f2e48761f 6372df0a109fd29842a999f4cc4be164
import sys,os
from Crypto.Cipher import AES
from settings import *

def main():
    iv1 = "4ee04f8303c0146d82e0bbe376f44e10"
    p1 = "48656c6c6f2c20746869732069732061"
    p2 = "207075626c6963206d6573736167652e"

    c1 = "de49b7bb8e3c5e9ed51905b6de326b39"
    c2 = "b102c7a6f0e09e92fe398c75d032b411"
    c3 = "89b11f873c6cd8cdb65a276f2e48761f"

    key = xor(decryption(bytes.fromhex(c1),bytes.fromhex(iv1)).hex(),p1)
    print("key = ",key)

    #c1x = encryption(bytes.fromhex(xor(c1,p1)),bytes.fromhex(key))
    c1x = encryption("Hello, this is a public message. This message contains no flags.",bytes.fromhex(key))
    print("c1x = ", c1x.hex())

    p2x = xor(xor(c2,key),c1)
    print("p2 = ",p2x)

    p3x = xor(xor(c3,key), c2)
    print("p3 = ",p3x)


def xor(a,b):
    result = int(a, 16) ^ int(b, 16)  # convert to integers and xor them together
    return '{:x}'.format(result)

def padding(text):
    b = BYTE_NB - (len(text) % BYTE_NB)
    return text + chr(b)*b # PKCS7 padding


def encryption(plain,key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded = padding(plain).encode()
    encrypted = cipher.encrypt(padded)
    return encrypted

def decryption(encrypted,key):
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted = cipher.decrypt(encrypted)
    return decrypted

if __name__ == "__main__":
    main()
    #print(padding("Hello, this is a public message. This message contains no flags.").encode())