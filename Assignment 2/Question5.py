#write a program  which accpet one number  from user
#and check whether number is prime or not.

#CheckPrime function

def CheckPrime(iNo):
    iCnt=1
    flag=0
    No2=iNo // 2
    for iCnt in range(2,No2):
        if iNo % iCnt == 0:
            flag=1
       
    if flag==1:
        return False
    else:
        return True

#Main Function.
def main():
    bRet=False
    iNo=int(input("Enter the number:"))
    bRet = CheckPrime(iNo)

    if bRet ==True :
        print("Number is Prime.")
    else:
        print("Number is not Prime")


#Starter.
if __name__ == "__main__":
    main()