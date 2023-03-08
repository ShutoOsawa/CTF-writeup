from Crypto.Cipher import AES
import os
def main():
    key = os.urandom(16)
    flag = b"flag{REDACTEDXX}"
    assert len(flag) % 16 == 0

    #First
    iv = os.urandom(16)
    iv = bytes.fromhex('4ee04f8303c0146d82e0bbe376f44e10')
    original = b"Hello, this is a public message. This message contains no flags."
    print("Original =",original.hex())

    given_encrypted = bytes.fromhex('de49b7bb8e3c5e9ed51905b6de326b39b102c7a6f0e09e92fe398c75d032b41189b11f873c6cd8cdb65a276f2e48761f6372df0a109fd29842a999f4cc4be164')
    print("CT1 given =", given_encrypted.hex())

    decipher = AES.new(iv,  AES.MODE_CBC, key)
    decrypted_with_key = decipher.decrypt(given_encrypted)
    print("CT1 Dec_with_key =", decrypted_with_key.hex())
    xor_key = xor(decrypted_with_key.hex()[:32],key.hex())
    print("Xor Key =",xor_key)
    xor_iv = xor(decrypted_with_key.hex()[:32], iv.hex())
    print("Xor iv =", xor_iv)



    xor_orig = xor(decrypted_with_key.hex()[:32],original.hex()[:32])
    print("xor original = ",xor_orig)

    key = bytes.fromhex(xor_orig)

    #Second
    #iv = os.urandom(16)
    iv = bytes.fromhex('1fe31329e7c15feadbf0e43a0ee2f163')
    encrypted_flag = 'f6816a603cefb0a0fd8a23a804b921bf489116fcc11d650c6ffb3fc0aae9393409c8f4f24c3d4b72ccea787e84de7dd0'
    encrypted = bytes.fromhex(encrypted_flag[:32])
    #cipher = AES.new(key, AES.MODE_CBC, iv )
    #print("IV2 =", iv.hex())
    #encrypted = cipher.encrypt(flag)
    #print("CT2 =", encrypted.hex())

    decipher = AES.new(key,  AES.MODE_CBC, iv)
    flag_before=decipher.decrypt(encrypted)
    print("CT2 REV =", flag_before)
    xor_flag = xor(iv.hex(),flag_before.hex())
    print(xor_flag)


def xor(a,b):
    print("a ",a)
    print("b ",b)
    result = int(a, 16) ^ int(b, 16)  # convert to integers and xor them together
    return '{:x}'.format(result)

def byte_xor(ba1, ba2) -> bytes:
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


if __name__ == "__main__":
    main()