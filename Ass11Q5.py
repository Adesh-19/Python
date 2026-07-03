
#write a program which accepts one number and check whether it is palindrome or not.

def Palindrom(No):
    result = ""

    for i in str(No):
        result = i + result
    return result


def main():
    No1 = int(input("Enter the number:"))

    Ret = Palindrom(No1)
    
    if int(Ret) == No1:
        print("the number is palindrome")
    else:
        print("number is not palindrome")

if __name__ == "__main__":
    main()        