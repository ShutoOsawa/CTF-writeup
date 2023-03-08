import base64
from random import randint
from itertools import product

def main():
    with open("flag.txt", 'r') as f:
        flag = f.readline()
    print(flag)
    patterns = get_combination_list()
    encoded_flag = flag.encode('utf-8')

    for pattern in patterns:
        for i in range(len(pattern)):
            print(pattern[i])
            encoded_flag = decrypt(encoded_flag,pattern[i])
        decrypted_flag = encoded_flag.decode()
        print(decrypted_flag)

def get_combination_list():
    patterns = list(product(range(4), repeat=12))
    return patterns

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

if __name__ == '__main__':
    main()