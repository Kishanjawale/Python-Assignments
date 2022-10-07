#importing MarvellousArithmatic Module 
import MarvellousArithmatic as Arith


#Main Function
def main():
    iValue1= int(input("Enter First Number:"))
    iValue2=int(input("Enter Second NUmber:"))

    iAddRet=Arith.Addition(iValue1,iValue2)
    iSubRet=Arith.Substraction(iValue1,iValue2)
    iMultRet=Arith.Multiplication(iValue1,iValue2)
    iDivRet=Arith.Division(iValue1,iValue2)

    print("Addition=",iAddRet)
    print("Substraction=",iSubRet)
    print("Multiplication=",iMultRet)
    print("Division=",iDivRet)

#Starter
if __name__== "__main__":
    main()
