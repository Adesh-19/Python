
#write a program which accept one number and print factorial of number.

def Fact(No1):
    fact = 1

    for i in range(1,No1+1):
        fact = fact * i
    return fact    


def main():
    No = int(input("Enter the no:"))

    Ret = Fact(No)
    print("Factorial is:",Ret)


if __name__ == "__main__":
    main()