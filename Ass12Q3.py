
#write a program which accept two numbers and print add,sub,mul and div.

def Calc(No1,No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mul = No1 * No2
    Div = No1 + No2
    return Add,Sub,Mul,Div

def main():
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))

    Ret1,Ret2,Ret3,Ret4 = Calc(a,b)
    print("addition is",Ret1)
   
    print("Sub is",Ret2)
    
    print("multi is",Ret3)
    
    print("div is",Ret4)

if __name__ == "__main__":
    main()

