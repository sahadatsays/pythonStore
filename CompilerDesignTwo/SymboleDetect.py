detectSymbole = "!@#$%^&*()"
detectSymbole = list(detectSymbole)
user_input = input("Enter Your Input : ")
user_input_list = list(user_input)
temp = []
for symble in detectSymbole:
    for u_i in user_input_list:
        if u_i == symble:
            temp.append(symble)

number_of_symbole = len(temp)
if(len(temp) > 0):
    print("User input is : ",user_input)
    str_temp = ''.join(str(x) for x in temp)

    print("Number of Symble found : ", number_of_symbole)
    print("Found Symbole is : ", str_temp)
else:
    print("User input is : ",user_input)
    print("Symbole not Found !")