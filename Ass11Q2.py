
#write a program which accepts one number
#and print count of digits in that number.

def Digits(No1):
    Count = 0

    for i in str(No1):
        Count = Count + 1
    return Count

def main():
    No = int(input("Enter the number:"))

    Ret = Digits(No)
    print("the count is:",Ret)

if __name__ == "__main__":
    main()    