
#write a program to accept one number from user 
#and Retun addition of its factors


#AddFact function:
#This function accept one integer as parameter and 
# return Addition of its factors 

def AddFact(ivalue):
    icnt=1
    iAddfact=0
    while icnt <= ivalue/2:
        if ivalue % icnt==0:
            iAddfact= iAddfact+icnt
        icnt=icnt+1
    return iAddfact 


#Main Function
def main():
    iValue=0
    iRet=0

    iValue=int(input("Enter the Number:"))
    iRet=AddFact(iValue)

    print("Addition of Factors:",iRet)

if __name__ == "__main__":
    main()
