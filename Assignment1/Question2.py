"""
Write a program which contains one function named as ChkNum()
which accept one parameter as number.if number is even then it
should display "Even Number" otherwise Display "Odd number"
on console
"""

#This Function accepts one integer as parameter
# And return true if number is even
#And return false if Number is odd
def ChkNum(iNo):
    if iNo % 2 == 0:
        return True
    else:
        return  False


#Main Function.
def main():
    No=int(input("Enter The Number:"))
    Ret=ChkNum(No)
    if Ret == True:
        print("Number is Even.")
    else:
        print("Number is Odd")

#Starter
if __name__ == "__main__":
    main()