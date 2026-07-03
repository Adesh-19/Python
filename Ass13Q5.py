
#Write a program which accept marks and print grade.

def Grade(No1):
    if No1 >= 75:
        return "Distinction"
    elif No1 >= 60 and No1 <= 75:
        return "First class"
    elif No1 >= 50 and No1 <= 60:
        return "Second Class"
    else:
        return "Fail"
    



def main():
    Marks = int(input("Enter the marks:"))

    Ret = Grade(Marks)
    print("Grade:",Ret)


if __name__ == "__main__":
    main()