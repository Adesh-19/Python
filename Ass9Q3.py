#Write a program which accept one number and print square of that number.

def Square(No):
    return No * No



def main():
    A = int(input("Enter the Number:"))

    Ret = Square(A)
    print("Square of the number is:",Ret)
    

if __name__ == "__main__":
    main()