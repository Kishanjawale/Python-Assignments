from sys import *

#Addition Function
def Addition(iNo1,iNo2):
    Add=int(iNo1)+int(iNo2)
    return Add

#Main Function
def main():
    if (len(argv)==2):
        if(argv[1]== "--U"):
            print("Use the Application as :")
            print("Python Name_of_Application First_number Second_Number")
            exit()

        if (argv[1] == "--H"):
            print("Help: This Application is used to perform addition of 2 numbers")
            exit()

    #If the number of  command line arguments  are not 3 then exit
    if(len(argv) !=3 ):
        print("Invalid Number of Arguments..")
        print("Please user --U flag to get usage.")
        exit()

    Ret=Addition(argv[1],argv[2])

    print("Addition:",Ret)

    print("Thank You For Using Our Application")
    print("Marvellous Infosystem Student Kishan Jawale")

#Starter
if __name__=="__main__":
    main()