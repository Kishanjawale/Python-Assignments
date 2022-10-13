#This functio accepts one integer as input and return its factorial
def Fact(ivalue):
    icnt=1
    fact=1
    for icnt in range(1,ivalue):
        fact=fact*icnt
    
    return fact

#main Function
def main():
    ivalue=int(input("Enter the number to find Factorial"))
    iRet=Fact(ivalue)
    print("Factorial =",iRet)

    #starter
if __name__=="__main__":
    main()
