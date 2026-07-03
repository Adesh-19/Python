
#write a program which accepet length and width of rectangleand print area.

def Area(No1,No2):
    Ans = No1 * No2
    return Ans


def main():
    length = int(input("Enter the length:"))
    width = int(input("Enter the width:"))

    Ret = Area(length,width)
    print("Area of the rerctangle is:",Ret)



if __name__ == "__main__":
    main()