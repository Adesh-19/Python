
#write a program which accepet one number and print multiplication table of that number.

def Table(No1):
    table = []

    for no in range(1,11):
        w = no * No1 
        table.append(w)
    
    return table






def main():
    No = int(input("Enter the No:"))

    Ret = Table(No)
    print("The table is:",Ret)


if __name__ == "__main__":
    main()