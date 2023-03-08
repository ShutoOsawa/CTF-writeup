#!/usr/bin/env python3
#
# Polymero
#

# Imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Local imports
with open('flag.txt', 'rb') as f:
    FLAG = f.read()
    f.close()

# Header
HDR = r"""|
|
|       __ _       ___ ____ ______ __ __ ____   ___  ____  __ __  ___  ____  ____  ____
|      /  ] |     /  _]    |      |  |  |    \ /   \|    \|  |  |/   \|    \|    |/    |
|     /  /| |    /  [_ |  ||      |  |  |  D  )     |  o  )  |  |     |  o  )|  ||  o  |
|    /  / | |___/    _]|  ||_|  |_|  _  |    /|  O  |   _/|  _  |  O  |     ||  ||     |
|   /   \_|     |   [_ |  |  |  | |  |  |    \|     |  |  |  |  |     |  O  ||  ||  _  |
|   \     |     |     ||  |  |  | |  |  |  .  \     |  |  |  |  |     |     ||  ||  |  |
|    \____|_____|_____|____| |__| |__|__|__|\_|\___/|__|  |__|__|\___/|_____|____|__|__|
|
|"""


# Server encryption function
def encrypt(msg, key):
    print(key)
    #多分最後のブロックにしか使われない？16以下なら16にする
    pad_msg = pad(msg, 16)

    blocks = [os.urandom(16)] + [pad_msg[i:i+16] for i in range(0,len(pad_msg),16)]
  #  print("blocks: ",blocks)

    #
    itm = [blocks[0]]
    for i in range(len(blocks) - 1):
       # print("i: ",i)
        tmp = AES.new(key, AES.MODE_ECB).encrypt(blocks[i+1])
        itm += [bytes(j^k for j,k in zip(tmp, blocks[i]))]


    #print("itm: ",itm)

    cip = [blocks[0]]
    for i in range(len(blocks) - 1):
       # print("itm -(i+1):",itm[-(i+1)])
       # print("itm -i:", itm[-i])
        tmp = AES.new(key, AES.MODE_ECB).decrypt(itm[-(i+1)])
        cip += [bytes(j ^ k for j, k in zip(tmp, itm[-i]))]


    #print("cip: ", cip)
    return b"".join(cip[::-1])

def xor(first,second):
    return bytes(j ^ k for j, k in zip(first, second))

# this one works for a short message
# def decrypted(flag,key):
#     blocks = [flag[i:i + 16] for i in range(0, len(flag), 16)]
#     print("blocks: ",blocks)
#     cip = blocks[::-1]
#     print("cip: ",cip)
#     iv = cip[0]
#     print("iv: ",iv)
#     dec_cip = AES.new(key, AES.MODE_ECB)
#     enc_cip = AES.new(key,AES.MODE_ECB)
#     cip_iv = xor(cip[1],iv)
#     cip_iv_iv = xor(enc_cip.encrypt(cip_iv),iv)
#     msg0 = dec_cip.decrypt(cip_iv_iv)
#     print("message: ",msg0)

def decrypted(flag,key):
    blocks = [flag[i:i + 16] for i in range(0, len(flag), 16)]
    cip = blocks[::-1]
    test_sum(cip,key)
    enc_tmp = create_temp(cip,key)
    decrypt_message(enc_tmp,cip,key)

def create_temp(cip,key):
    enc_tmp = [cip[0]]
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(len(cip) - 1):
        enc_tmp.append(cipher.encrypt(xor(enc_tmp[i], cip[i + 1])))
    return enc_tmp


def decrypt_message(enc_tmp,cip,key):
    decipher = AES.new(key, AES.MODE_ECB)
    msg = [cip[0]]
    for i in range(len(cip)-1,0,-1):
        msg.append(decipher.decrypt(xor(enc_tmp[i],msg[-1])))
    print(msg)

def test_sum(cip,key):
    cipher = AES.new(key, AES.MODE_ECB)
    pre_xored = xor(cip[0],cip[1])
    enc1 = cipher.encrypt(pre_xored)
    print("before",enc1)
    for i in range(9):
        enc1 = cipher.encrypt(enc1)
    print("after ", enc1)

    enc2 = cipher.encrypt(cip[0])
    enc3 = cipher.encrypt(cip[1])
    post_xored = xor(enc2,enc3)


    print("post",post_xored)



# Server connection
KEY = os.urandom(32)

print(HDR)
print("|  ~ I trapped the flag using AES encryption and decryption layers, so good luck ~ ^w^")
print(FLAG.hex())
flag = encrypt(FLAG, KEY)
print(f"|\n|    flag = {flag}")

decrypted(flag,KEY)
# plaintext = bytes.fromhex('6964656b7b52454441435445444142434445464748494a4b4c4d4e4f505152535455565758595a7d')
# provided_flag = 'a383fa5b951886c527644c0308b1fb86dcf48aed2360fcd8a91b63b417a0288d33d48d4ddd50fd2d822ba3e280212cfda2668379cb2a31c6a9a36d172b4513f9a4f4362509a03e3bce5ecd6b0a6f00657be09ad9a4c65a13dac78b1677567089'
# provided_flag = 'd070da8a55e4743da02ae31a9a58b072661b3125271c026051a92af268b0c0c77a3e50b3770afdde96ab98216ed48e89dec3de39ac974897d795e027c73901f4'
# flag_bytes = bytes.fromhex(provided_flag)
# decrypted(flag_bytes,KEY)
#
# print("key:",KEY)

# Server loop
while True:

    try:

        print("|\n|  ~ Want to encrypt something?")
        msg = bytes.fromhex(input("|\n|    > (hex) "))

        enc = encrypt(msg, KEY)
        print(f"|\n|   {enc.hex()}")

    except KeyboardInterrupt:
        print('\n|\n|  ~ Well goodbye then ~\n|')
        break

    except:
        print('|\n|  ~ Erhm... Are you okay?\n|')
