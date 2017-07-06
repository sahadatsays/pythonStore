from tkinter import *

root = Tk()
root.title("Python GUI Basic")
topFrame = Frame(root)
btn = Button(root, text="Submit", bd=10)
btn.pack
topFrame.pack()
root.mainloop()