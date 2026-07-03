#Write a program which accept one number and print Cube of that number.

def Cube(No):
    return No*No*No

def main():
    Num = int(input("Enter the number:"))

    Ret = Cube(Num)
    print("Cube of the number is:",Ret)

if __name__ == "__main__":
    main()