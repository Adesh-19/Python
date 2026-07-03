
#write a program which accepts one number and checks whether it is prime or not.

def prime(No):
    if No <= 1:
        return False
    for i in range(2,No):
        if No%i == 0:
            return False
    return True
    
def main():
    No1 = int(input("Enter the num:"))

    Ret = prime(No1)

    if Ret == True:
        print("prime number is:",No1)
    else:
        print("number is not prime",No1)    


if __name__ == "__main__":
    main()        
