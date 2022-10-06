
"""
Write a program which accept number from user and
print that number of  " * " on screen
"""


#PrintStar Function.
def PrintStars(iNo):
     i=0
     for i in range (i,iNo,1):
         print("*\t",end='')


#Main Function.
def main():
    No=int(input("Enter The Number:"))
    PrintStars(No)


#Starter
if __name__ == "__main__":
    main()