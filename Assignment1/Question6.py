"""
Write a program which accepts the number from user
and check whether that number
is positve or negative or zero
"""

#This Function accepts one integer as parameter
#return 1 if number is positive
#return -1 if number is negative

def ChkNum(iNo):
    if iNo > 0 :
        return 1
    if iNo < 0 :
        return -1

#Main Function.
def main():
    No=int(input("Enter The Number:"))
    Ret=ChkNum(No)

    if Ret == 1:
        print("Positive Number")
    elif Ret == -1:
        print("Negative Number")
    else:
        print("Zero")

#Starter
if __name__ == "__main__":
    main()