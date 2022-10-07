
#write a program to accept one number from user 
#and Retun number of digit in that number

#This function accept one integer as parameter and 
# return number of  digit in that numbe

#CountDigit Function
from itertools import count


def CountDigit(ivalue):
    
    Counter1=0
    while ivalue > 0:
        iDig=ivalue % 10
        ivalue=ivalue // 10
        Counter1 = Counter1 + 1 
    
    return Counter1

#Main Function
def main():
    iValue=0
    iRet=0

    iValue=int(input("Enter the Number:"))
    iRet=CountDigit(iValue)

    print("Number of Digits:",iRet)

if __name__ == "__main__":
    main()
