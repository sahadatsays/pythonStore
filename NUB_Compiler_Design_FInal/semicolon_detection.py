count = 0
while count < 3:
    user_input = input("Enter Your Input : ")

    user_input = list(user_input)

    if user_input[-1] == ';':
        print("\nOutput : Semecolon Found, at last Here! \n")
    else:
        print("\nOutput : Semecolon Not Found Here ! \n")
count = count+1