
#write a program which accepts one number and print reverse of that number.


def Reverse(No):
    result = ""

    for i in str(No):
        result = i + result

    return result    


def main():
    No1 = int(input("Enter the Number:"))

    Ret = Reverse(No1)
    print("Reversed number is:",Ret)


if __name__ == "__main__":
    main()       
