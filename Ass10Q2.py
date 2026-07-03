
#write a program which accept one number and print sum of first N natural numbers.


def Sum(No1):
    sum = 0

    for i in range(No1 + 1):
        sum = sum + i
    return sum


def main():
    No = int(input("Enter any Natural No:"))

    Ret = Sum(No)
    print("Sum of first N natural No is:",Ret)


if __name__ == "__main__":
    main()