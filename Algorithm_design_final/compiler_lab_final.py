input_file = open("input.txt","r")
#convertion string
input_string = input_file.read()
char_string = list(input_string)
input_str = input_string.split()
input_str_by_coma = input_string.split(',')

get_keyword = ['if', 'else', 'printf', 'while', 'for']
get_variable = ['a', 'b', 'c', 'x', 'y', 'z']
get_brackets =list("(){}")

output_keyword = []

for ist in input_str:
    for get_key in get_keyword:
        output = ist.find(get_key)
        if output==0:
            output_keyword.append(get_key)

#output print
print("Keywrods : ", end="")
for x in output_keyword:
    print("%s"%x, end=", ")
print("\n"*1)
print("Number has ", end=": ")
number = [int(num) for num in list(input_string) if num.isdigit()]
for h in number:
    print(h, end=", ")
print("\n"*1)
print("Brackets has ", end=": ")

for br in char_string:
    for get_br in get_brackets:
        if br == get_br:
            print(get_br, end=',')
print("\n"*1)


outputvar = []
outPutString = []
index = []
count = 0


for v in input_str_by_coma:
    for get_v in get_variable:
        if v==get_v:
            outputvar.append(v)

print("Variable has : ", end='')
for var in outputvar:
    print(var, end=',')
# print(index)

# print(outPutString)
# print(count)

input_file.close()