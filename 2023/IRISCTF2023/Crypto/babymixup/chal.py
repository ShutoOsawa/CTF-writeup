from Crypto.Cipher import AES
import os

#
# flag = b"flag{REDACTEDXX}"
# assert len(flag) % 16 == 0

key = os.urandom(16)


#iv1

iv1 = bytes.fromhex('4ee04f8303c0146d82e0bbe376f44e10')
iv1 = os.urandom(16)
print(iv1)
print("CT1 =",b"Hello, this is a public message. This message contains no flags.".hex())
cipher = AES.new(iv1,  AES.MODE_CBC, key)
print("CT1 =", cipher.encrypt(b"Hello, this is a public message. This message contains no flags."))

ct1 = bytes.fromhex('de49b7bb8e3c5e9ed51905b6de326b39b102c7a6f0e09e92fe398c75d032b41189b11f873c6cd8cdb65a276f2e48761f6372df0a109fd29842a999f4cc4be164')
print(ct1.hex())
cipher_dec = AES.new(iv1,AES.MODE_CBC,key)
print("\n")
print("decrypted=",cipher_dec.decrypt(ct1))
print("decrypted=",cipher_dec.decrypt(ct1).hex())

# #iv2
iv2 = bytes.fromhex("1fe31329e7c15feadbf0e43a0ee2f163")
ct2 = bytes.fromhex("f6816a603cefb0a0fd8a23a804b921bf489116fcc11d650c6ffb3fc0aae9393409c8f4f24c3d4b72ccea787e84de7dd0")
cipher_dec = AES.new(iv2,AES.MODE_CBC,key)
decrypted = cipher_dec.decrypt(ct2)
print("decrypted=",decrypted)