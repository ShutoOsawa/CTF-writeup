from Crypto.Cipher import AES
import os

def main():
    vect =  b'\xac:ti\xb7F_Ds\xfe\x18\xa7\xc7Up)'

    #1. ivと暗号化された文章を準備
    iv = bytes.fromhex('4ee04f8303c0146d82e0bbe376f44e10')
    encrypted_message = bytes.fromhex('de49b7bb8e3c5e9ed51905b6de326b39b102c7a6f0e09e92fe398c75d032b41189b11f873c6cd8cdb65a276f2e48761f6372df0a109fd29842a999f4cc4be164')
    print("original encrypted",encrypted_message)
    key = decrypt_first(iv,encrypted_message,vect)
    print("key",key)

    print("plain hex",b"Hello, this is a public message. This message contains no flags.".hex())
    decrypt = decryption(encrypted_message,iv,vect)
    plain2 = byte_xor(decrypt, key)
    print("plain2",plain2)

    iv2 = bytes.fromhex('1fe31329e7c15feadbf0e43a0ee2f163')
    encrypted_flag = bytes.fromhex(
        'f6816a603cefb0a0fd8a23a804b921bf489116fcc11d650c6ffb3fc0aae9393409c8f4f24c3d4b72ccea787e84de7dd0')

    flag_before = decryption(encrypted_flag,key,vect)
    flag = byte_xor(encrypted_flag, key)
    print("flag:",flag)

def encryption(plain,key,vect):
    cipher = AES.new(key, AES.MODE_CBC, vect)
    encrypted = cipher.encrypt(plain)
    return encrypted

def decryption(cipher,key,vect):
    decipher = AES.new(key, AES.MODE_CBC, vect)
    decrypted = decipher.decrypt(cipher)
    return decrypted

def decrypt_first(iv,encrypted,vect) -> bytes:
    decipher = AES.new(iv,AES.MODE_CBC,vect)
    #復号
    decrypted_message = decipher.decrypt(encrypted)
    #最初の16バイト分以外は問題なく復号できる
    print("Decrypted CT1 =", decrypted_message)
    #最初の16文字の平文を持ってくる
    plain = b"Hello, this is a"
    #復号かされた最初の16バイト分を持ってくる
    d_iv =  decrypted_message[:16]
    #xorを取れば鍵になる
    key = byte_xor(plain,d_iv)
    return key

def decrypt_second(key,encrypted,vect) -> bytes:
    #cipher二つ目を準備
    decipher = AES.new(key,AES.MODE_CBC,vect)
    #flag暗号文を復号
    decrypted = decipher.decrypt(encrypted)
    return decrypted

def byte_xor(ba1, ba2) -> bytes:
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

if __name__ == "__main__":
    main()