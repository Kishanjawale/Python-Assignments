
"""
Write a program which accept the name of user and display
length of its name.
"""

#PrintLength function
def PrintLength(str):
    print(len(str))

#Main Function.
def main():
    name = input("Enter Your Name:")
    PrintLength(name)

#Starter
if __name__ == "__main__":
    main()