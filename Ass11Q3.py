
#write a program which accepts one number and print sum of digits.

def Sum(No):
    sum = 0

    for i in str(No):
        sum = sum + int(i)

    return sum

def main():
    No1 = int(input("Enter the number:"))

    Ret = Sum(No1)
    print("the sum is:",Ret)

if __name__ == "__main__":
    main()