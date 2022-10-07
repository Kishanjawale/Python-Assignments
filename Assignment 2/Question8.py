#write a program  which accpet one number and display below pattern
"""
input: 5
output:

1
1   2
1   2   3
1   2   3   4
1   2   3   4   5

""" 
#This Function Print the Pattern  
from socket import IPV6_LEAVE_GROUP


def PrintPattern(ival):
    icnt=0
    jcnt=0

    for icnt in range(1,ival+2,1):
        for jcnt in range (1,ival+1,1):
            if jcnt < icnt:
                print(jcnt,"\t",end="")
        print(" ")

#main function
def main():
    ivalue=int(input("Enter the Number:"))
    PrintPattern(ivalue)

#starter
if __name__== "__main__":
    main()