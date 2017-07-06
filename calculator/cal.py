from tkinter import*

def btnClick(number):
    global operator
    operator=operator + str(number)
    input_Text.set(operator)

def clearDisplay():
    global operator
    operator=""
    input_Text.set("")

def actionEqual():
    global operator
    sumup = str(eval(operator))
    input_Text.set(sumup)
    operator = ""

cal = Tk()
cal.title("Python Calculator")
operator = ""
input_Text = StringVar()

text_Display = Entry(cal, font = ('arial', 20, 'bold'), textvariable = input_Text, bd=30, insertwidth=4,
                     bg='powder blue', fg='black', justify='right').grid(columnspan=4)
#======================== Button - first Row ==============================
btn7 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(7), fg='black', text='7').grid(row=1,column=0)
btn8 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(8), fg='black', text='8').grid(row=1,column=1)
btn9 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(9), fg='black', text='9').grid(row=1,column=2)
btnSum = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', fg='black', text='+', command=lambda:btnClick('+')).grid(row=1,column=3)

#======================== Button - Second Row ==============================
btn4 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(4), fg='black', text='4').grid(row=2,column=0)
btn5 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(5), fg='black', text='5').grid(row=2,column=1)
btn6 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(6), fg='black', text='6').grid(row=2,column=2)
btnSub = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', fg='black', command=lambda:btnClick('-'), text='-').grid(row=2,column=3)

#======================== Button - Third Row ==============================
btn1 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(1), fg='black', text='1').grid(row=3,column=0)
btn2 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(2), fg='black', text='2').grid(row=3,column=1)
btn3 = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick(3), fg='black', text='3').grid(row=3,column=2)
btnMult = Button(cal, font = ('arial', 20, 'bold'), padx = 16, bd=7, bg='powder blue', command=lambda:btnClick('*'), fg='black', text='*').grid(row=3,column=3)

#======================== Button - Fourth Row ==============================
btn0 = Button(cal, font = ('arial', 20, 'bold'), padx = 16,pady = 16, bd=7, bg='powder blue', command=lambda:btnClick(0), fg='black', text='0').grid(row=4,column=0)
btnC = Button(cal, font = ('arial', 20, 'bold'), padx = 16, pady = 16, bd=7, bg='powder blue', fg='black', command=clearDisplay, text='C').grid(row=4,column=1)
btneq = Button(cal, font = ('arial', 20, 'bold'), padx = 16, pady = 16, bd=7, bg='powder blue', fg='black', text='=', command=actionEqual).grid(row=4,column=2)
btndiv = Button(cal, font = ('arial', 20, 'bold'), padx = 16, pady = 16, bd=7, bg='powder blue', command=lambda:btnClick('/'), fg='black', text='/').grid(row=4,column=3)

cal.mainloop()

