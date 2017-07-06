#======== Tips No One=========
        #===bad way====
print("Bad Way !\n")
ex_list = ['Cow', 'Cat', 'Deer', 'Tiger', 'Monkey', 'Dog']
i = 0
for list in ex_list:
    print(i, list)
    i+=1

    #===Good Way===
print("\nGood Way\n")
for i, list in enumerate(ex_list):
    print(i, list)
#==============Tips No 2===========
#====Bad way=====
print("\n\nBad Way for Two Print Daintional List\n")
x_list = [1,2,3,4,5,6,7,8,9,10]
y_list = [4,5,7,1,84,4,38,29,120,3]

for j in range(len(x_list)):
    x= x_list[j]
    y= y_list[j]
    print(x,y)

print("\nGood Way :")
for x,y in zip(x_list, y_list):
    print(x,y)
#===================Tips 3 ==========
#=====Bady way ====
print("\nSwaping System Bad Way")
num = 30
num2 = -40
print("Without Change ")
print("X = ", num, "| Y = ", num2)

# temp = num2
# num2 = num
# num = temp
#
# print("With Change ")
# print("X = ", num, "| Y = ", num2)
#=====Good way ====
print("\nGood Way For Swap")
num,num2 = num2,num
print("With Change ")
print("X = ", num, "| Y = ", num2)
# ===================Tips 4(Dictonarry)==========
# =====Bady way ====
print("\nBad Way Dictonary")
ages = {
    'Sahadat' : 30,
    'Faisal'  : 50,
    'Ismail'  : 60
}
    # if 'Ismail' in ages:
    #     age = ages['Ismail']
    # else:
    #     age = "Unknown"
    # print("Ismail is %s Years Old"% age)
# =====Good way ====
age = ages.get("Ismail", "Unknown")
print("Ismail is %s Years Old" % age)

# ===================Tips 5 ==========
# =====Bady way ====
print("\n"*3)
need = 'd'
hystack = ['a', 'b', 'c']
        # found = False
        # for i in hystack:
        #     if i==need:
        #         found=True
        #         print("Found")
        #         break
        # if not found:
        #     print("Not-Found")
# =====Good way ====
for i in hystack:
    if i==need:
        print("Found")
        break
else:
    print("Not Found")
# ===================Tips 6 ==========
# =====Bady way ====
    #f = open('demo.txt')
    #read = f.read()
    # for line in read.split('\n'):
    #     print(line)
    # f.close()
# =====better way ====
#     for line in f:
#         print(line)
#     f.close()
# =====better way ====
    # with open('Demo.txt') as f:
    #     for line in f:
    #         print(line)
    # f.close()

# ===================Tips 7 ==========
# =====Bady way ====
print("\n"*5)
print("Converting....")
try:
    print(int('8'))
except:
    print("Converting Fail!")
else: #if  no-except
    print("Conversion SuccessFully !")
finally: #always print
    print("Done !")
# =====Good way ====
pythonCurrentVersion = 3
pythonUpdateVersion = 3

msg = "Update available" if pythonCurrentVersion<pythonUpdateVersion else "No Update Available"
print("Now - %s" %msg)
