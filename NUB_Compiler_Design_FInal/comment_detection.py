count = 0
while count < 5:

    user_input = input("Enter User Input : ")
    user_input = list(user_input)
    if (user_input[0]) == '/' and user_input[1]=='/':
        print("Yes, It is Single Line Comment.")
    elif (user_input[0]=='/' and user_input[1]=='*') and (user_input[-1]=='/' and user_input[-2]=='*'):
        print("Yes, It is Multi-line comment.")
    else:
        print("No, It is not a comment !")
count=count+1