#write a program  which accpet one number and display below pattern
"""
input: 5
output:
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
*   *   *   *   *
""" 
#This Function Print the Pattern  
def PrintPattern(ival):
    icnt=0
    jcnt=0

    for icnt in range(ival+1,0,-1):
        for jcnt in range (ival+1,0,-1):
            if jcnt < icnt:
                print("*\t",end="")
    
        
        print(" ")

#main function
def main():
    ivalue=int(input("Enter the Number:"))
    PrintPattern(ivalue)

#starter
if __name__== "__main__":
    main()