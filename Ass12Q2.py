
#write a program which accept one number and print its factors.

def Factor(No):
    fact = list()

    for i in range(1,No+1):
        if No % i == 0:
            fact.append(i)
    return fact

def main():
    No1 = int(input("enter the number:"))

    Ret = Factor(No1)
    print("Factors:",Ret)



if __name__ == "__main__":
    main()