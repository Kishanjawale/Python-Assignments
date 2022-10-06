"""
Write a program which contains one function named as Add()
which accept two parameter as number. And return addition of that
two numbers
"""

#This Function accepts Two integer as parameter
# And return its Addition.

def Add(iNo1,iNo2):
    Addition=iNo1+iNo2
    return Addition


#Main Function.
def main():
    No1=int(input("Enter First Number:"))
    No2= int(input("Enter First Number:"))
    Ret=Add(No1,No2)

    print("Addition =",Ret)

#Starter
if __name__ == "__main__":
    main()