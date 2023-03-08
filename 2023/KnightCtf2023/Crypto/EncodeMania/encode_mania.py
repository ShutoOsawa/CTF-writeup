import base64
from random import randint

flag = "kctf{************}"

def encrypt(s, option):
    if option == 0:
        ret = base64.b64encode(s)
    elif option == 1:
        ret = base64.b32encode(s)
    elif option == 2:
        ret = base64.b16encode(s)
    else:
        ret = base64.b85encode(s)

    return ret

def decrypt(s, option):
    if option == 0:
        ret = base64.b64decode(s)
    elif option == 1:
        ret = base64.b32decode(s)
    elif option == 2:
        ret = base64.b16decode(s)
    else:
        ret = base64.b85decode(s)

    return ret

encrypted_flag = flag.encode('utf-8')

encrypted_flag = encrypt(encrypted_flag,0)
decrypted_flag = decrypt(encrypted_flag,0)
print(decrypted_flag.decode)

# for _ in range(12):
#     option = randint(0, 3)
#     encrypted_flag = encrypt(encrypted_flag, option)

# with open("flag.txt", 'w') as f:
#     f.write(encrypted_flag.decode())
