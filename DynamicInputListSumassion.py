
def Sumassion(Data):
    Sum = 0
    for no in Data:
        Sum = Sum + no
    return Sum

def main():
   Size  = 0
   Arr = list()
   print("Enter the no of elements : ")
   Size = int(input())

   print("Enter the elementes")
   for i in range(Size):
       no = int(input())
       Arr.append(no)

   Ret = Sumassion(Arr)
   print("Sumassion is ret:",Ret)
    

if __name__ == "__main__":
    main()    

    