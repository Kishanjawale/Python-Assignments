"""
Write a program which contains a function that accepts
 the number from user
and return true if number is divisible by 5
otherwise return false
"""

#This Function accepts one integer as parameter
#return True if number is Divisible by 5
#Otherwise return false.

def ChkNum(iNo):
    if iNo % 5 == 0 :
        return True
    else:
        False

#Main Function.
def main():
    No=int(input("Enter The Number:"))

    Ret=ChkNum(No)

    if Ret== True:
        print("TRUE")
    else:
        print("False")

#Starter
if __name__ == "__main__":
    main()