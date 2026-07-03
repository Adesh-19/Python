

#Write a program which one function name as checkGreator() and 
# that accepet two number and print the generator number


def checkGreator(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2
 


def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter second number:"))
    
    Ret = checkGreator(No1,No2)
    print("The grator Number is:",Ret)


if __name__ == "__main__":
    main()