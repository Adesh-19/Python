
#write a program which accepts one number and 
# checks whether it is divisible by 3 and 5.

def Divisible(No):
    if No % 3 == 0 and No % 5 == 0:
        return True
    else:
        return False

def main():
    Num = int(input("Enter the Number:"))

    Ret = Divisible(Num)

    if Ret == True:
        print(Num,"is Divisible by 3 and 5")
    else:
        print(Num,"is Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()