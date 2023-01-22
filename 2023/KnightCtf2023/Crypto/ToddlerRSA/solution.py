from Crypto.Util.number import getPrime, bytes_to_long,long_to_bytes
from itertools import combinations

def main():
    # flag1 = b"kctf{*****"
    # m = bytes_to_long(flag1)
    ct,ct2,pq,pq2 = load_flag_info()
    comb = get_combination_list(pq,2)
    decrypt_each(comb,ct)

    comb2 = get_combination_list(pq2,9)
    decrypt_each2(comb2,ct2)

def get_combination_list(lst,num):
    comb = set(list(combinations(lst, num)))
    return comb

def decrypt_each(comb,ct):
    for item in comb:
        flag1 = decrypt1(item[0],item[1], ct)
        if b"KCTF" in flag1:
            print(flag1)
            break

def decrypt_each2(comb,ct):
    for item in comb:
        flag2 = decrypt2(item,ct)
        if len(flag2) < 100:
            print(flag2)

def decrypt1(p,q,ct):
    n = p*q
    phi = (p-1)*(q-1)
    e = 0x10001
    d = modinv(e,phi)
    m = pow(ct, d, n)
    return long_to_bytes(m)

def decrypt2(lst,ct):
    n = 1
    phi = 1
    for item in lst:
        n *= item
        phi *= (item-1)
    e = 0x10001
    d = modinv(e,phi)
    m = pow(ct,d,n)
    return long_to_bytes(m)

#https://tex2e.github.io/blog/crypto/modular-mul-inverse
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def load_flag_info():
    with open("flag_info.txt", 'r') as f:
        ct = int(f.readline())
        ct2 = int(f.readline())
        pq_raw = f.readline()
        pq_raw2 = f.readline()

    pq = list(map(int,pq_raw.split()))
    pq2 = list(map(int,pq_raw2.split()))
    return ct,ct2,pq,pq2

if __name__ == '__main__':
    main()
