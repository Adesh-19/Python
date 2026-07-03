
#write a program which accepts one character and checks whether it is vowel or consonent.


def Vowel(char):
    if char == "a" or char == "e" or char== "i" or char== "o" or char == "u":
        return True
    elif char == "A" or char == "E" or char== "I" or char== "O" or char == "U":
        return True
    else:
        return False
    
def main():
    str = input("Enter the character:")

    Ret = Vowel(str)

    if Ret == True:
        print("Vowel")
    else:
        print("Consonenet")

if __name__=="__main__":
    main()