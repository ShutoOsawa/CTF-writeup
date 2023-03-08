
def main():
    print("main")
    a = 26513
    b = 32321
    while True:
        a,b = gcd(a,b)
        if b == 0:
            print(a,b)
            break

def gcd(a,b):
    if a <= b:
        n1,n2 = a,b
    else:
        n1,n2 = b,a
    r = n2 % n1
    return n1,r

if __name__ == '__main__':
    main()