
def main():
    print("main")
    a = 26513
    b = 32321
    d,x,y=extended_gcd(a,b)
    print(d,x,y)

def extended_gcd(a,b):
    if b:
        d,y,x = extended_gcd(b,a%b)
        y = y - (a//b)*x
        return d,x,y
    return a,1,0

if __name__ == '__main__':
    main()