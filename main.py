# will combine gclib and carriage classes into single executable
from tkinter import *

root = Tk()

a = 2820.0
b = 500.0

if a > b:
    print("Yup")
else:
    print("Nope")

value = IntVar()
Spinbox(root, from_=0, to=5000, textvariable=value).pack()
