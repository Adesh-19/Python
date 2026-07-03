
##write a program which accept one number and print all even number till that number.


def Even(No1):
    even = list()

    for i in range(1,No1+1):
        if (i % 2 == 0):
            even.append(i)

    return even

def main():
    No = int(input("enter the no:"))

    Ret = Even(No)
    print("the even no is:",Ret)

if __name__ == "__main__":
    main()