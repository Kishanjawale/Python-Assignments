
"""
Write a program  which display
first 10 even numbers on screen
"""

#PrintEven Function :
    # it prints first 10 even numbers on console

def PrintEven():
      icnt=0
      i=1
      while(icnt<10):
          if(i%2 == 0):
              icnt=icnt+1
              print(i,"\t",end="")
          i=i+1

#Main Function.
def main():
    PrintEven()

#Starter
if __name__ == "__main__":
    main()