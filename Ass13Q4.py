
#write a program which accept one number and prints the binary equivalent.


def Binary(No1):
    result = ""

    while No1 > 0:
        rem = No1 % 2
        result = str(rem) + result
        No1 = No1 // 2

    return result





def main():
    No = int(input("Enter the number:"))

    Ret = Binary(No)

    if No == 0:
        print("the binary is 0")
    else:
        print("The binary euivalent is:",Ret)


if __name__ == "__main__":
    main()