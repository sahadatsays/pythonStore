import sys

def addNumber(fnum, lnum):
    return fnum+lnum

# print("Enter Your First Number : ")
# firstNumber = sys.stdin.readline()
# print("Enter Your Second Number : ")
# secondNumber = sys.stdin.readline()

try:
    x = int(input("Enter F number : "))
    y = int(input("Enter S Number : "))
    print("Your Output is : ", addNumber(x, y))
except:
    print("Input not valid! ")



# print("Enter Your name : ")
# name = sys.stdin.readline()
# print("Welcome to ",name)
# print('\n'*5)

# addNumber(30, 30)
