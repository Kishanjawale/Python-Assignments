#write a program to accept one number from user and return its factorial

from errno import WSAESHUTDOWN


#Fact function:
#This function accept one integer as parameter and return 
#its factorial

def Fact(ivalue):
    icnt=1
    ifact=1
    while icnt <= ivalue:
        ifact=icnt*ifact
        icnt=icnt+1
    return ifact 


#Main Function
def main():
    iValue=0
    iRet=0

    iValue=int(input("Enter the Number:"))
    iRet=Fact(iValue)

    print("Factorial:",iRet)

if __name__ == "__main__":
    main()
