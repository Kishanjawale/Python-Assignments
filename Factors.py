
#DisplayFactors  function:used to display factors of entered number
def DisplayFactors(iNo):

    #using for Loop
    icnt = 0
    print("Factors Of ",iNo,":")
    for icnt in range (1 , (iNo // 2)+ 1 , 1):   #  for loop with reduced iterations
        if iNo % icnt == 0 :
            print(icnt)
            
"""        
    #using while loop
    print("Factors Of ", iNo, ":")
    icnt=1
    while(icnt <= int(iNo/2)):
        if iNo % icnt == 0:
            print(icnt)
         icnt=icnt+1
"""

#Main Function
def main():
    print("enter the number:")
    iNo =int(input())
    DisplayFactors(iNo)

#Starter
if __name__ == "__main__":
    main()
