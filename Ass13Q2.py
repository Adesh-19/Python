
#Write a program which accept radius of circle and print area of circle.

def Area(No):
    PI = 3.14

    Ans = PI * No * No

    return Ans

def main():
    Radius = int(input("Enter the radius:"))

    Ret = Area(Radius)
    print("Area of the circle:",Ret)


if __name__ == "__main__":
    main()