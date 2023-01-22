from Crypto.Util.number import getPrime, bytes_to_long
import random

flag1 = b"kctf{*****"
flag2 = b"******}"

p, q = getPrime(512), getPrime(512)
n = p * q
e = 0x10001
phi = (p - 1) * (q - 1) 
m = bytes_to_long(flag1)
ct = pow(m, e, n)
print("p: {}\n".format(p))
print("q: {}\n".format(q))
print("ct :",ct)

primes = [p, q]

# prepare 100 prime numbers in addition to p and q
for _ in range(98):
    primes.append(getPrime(512))

# randomize the order of prime numbers
random.shuffle(primes)




primes2 = []

#preparing 16 128bit prime number list
while True:
    if len(primes2) == 16:
        break
    # 128 bit prime number
    p = getPrime(128)
    if p not in primes2:
        primes2.append(p)

# choose number from the prime list randomly and multiply them.
# if n2 exceeds 1024 bits then break
while True:
    n2 = 1
    count = 0
    for p in primes2:
        r = random.randint(0, 1)
        if r:
            n2 *= p
            count += 1
    if n2.bit_length() > 1024:
        print(count)
        break

m2 = bytes_to_long(flag2)
ct2 = pow(m2, e, n2)

#in infos, first two lines are encrypted texts
# the rest are prime numbers.
# do we need to try all the combinations of primes?
print("ct",ct)
with open("infos.txt", 'w') as f:
    f.write('{}\n'.format(ct))
    f.write('{}\n'.format(ct2))

    for p in primes:
        f.write(str(p) + " ")
    f.write("\n")
    
    for p in primes2:
        f.write(str(p) + " ")


    