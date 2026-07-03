

##write a program which accept one number and print all even number till that number.


def Odd(No1):
    odd = list()
    
    for i in range(1,No1+1):
        if (i % 2 == 1):
            odd.append(i)

    return odd

def main():
    No = int(input("enter the no:"))

    Ret = Odd(No)
    print("the even no is:",Ret)

if __name__ == "__main__":
    main()