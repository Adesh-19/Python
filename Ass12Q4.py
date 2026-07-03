
#write a program which accept one number and print that many numbers starting from 1.

def Start(No):
    start = []

    for i in range(1,No+1):
        start.append(i)
    return start



def main():
    a = int(input("enter the number:"))

    Ret = Start(a)
    print(Ret)


if __name__ == "__main__":
    main()