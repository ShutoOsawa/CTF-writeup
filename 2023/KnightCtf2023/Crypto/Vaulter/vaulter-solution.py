import sys
import random


def main():

    byte_data = []
    #file_name = sys.argv[1]
    file_name = "test.txt"
    #num = random.randint(1, 1024)
    num = 100

    with open(file_name, "rb") as f:
        byte_data = f.read()        
        bdh = byte_data.hex()
        print(bdh)
        out = []
        for each in list(bdh):
            out.append(ord(each) ^ num)
        print(out)
        concat = "".join(chr(i) for i in out)

        with open("output.enc.txt", "w") as f:
            f.write(concat)


def decrypt():
    file_name = "output.enc.txt"

    with open(file_name, "rb") as f:
        byte_data = f.read()
        bdh = []
        for s in byte_data:
            bdh.append(s)

        for i in range(50,101):
            out = []
            for each in list(bdh):
                xor = each ^ i
                print(xor)
                out.append(chr(xor))
            lst  = []
            for i in range(0,len(out),2):
                st = ""
                for j in out[i:i+2]:
                    st += str(j)
                lst.append(st)
            print(lst)
            concat = ""
            for st in lst:
                concat += str(st)
            print(concat)





if __name__ == "__main__":
    #main()
    decrypt()