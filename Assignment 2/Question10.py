
#write a program to accept one number from user 
#and Retun addition of its Digits

#This function accept one integer as parameter and 
# return Addition of its factors 

#AddDigit Function
def AddDigit(ivalue):

    iAddDigi=0
    while ivalue > 0:
        iDig=ivalue % 10
        ivalue=ivalue // 10
        iAddDigi=iDig+iAddDigi
    
    return iAddDigi

#Main Function
def main():
    iValue=0
    iRet=0

    iValue=int(input("Enter the Number:"))
    iRet=AddDigit(iValue)

    print("Addition of Digits:",iRet)

if __name__ == "__main__":
    main()
