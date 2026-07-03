
#write a program which accept one number and print that many numbers in reverse order.

def End(No):
    end =[]

    for i in range(No,0,-1):
        end.append(i)
    return end
    

def main():
    a = int(input("enter "))
    
    Ret = End(a)
    print(Ret)




if __name__ == "__main__":
    main()