
#write a program which accept a number and check whether it is perfect or not.


def Perfect(No):
    
    count = 0
    for i in range(1,No):
        if No % i == 0:
            count = count + i
    return count


def main():
    No1 = int(input("enter the number:"))

    Ret = Perfect(No1)
    
    if Ret == No1:
        print(No1,"is perfect no")

    else:
        print(No1,"is not perfect no")





if __name__ == "__main__":
    main()