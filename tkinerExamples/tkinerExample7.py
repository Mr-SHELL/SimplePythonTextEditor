#use place() method 
from tkinter import *
top = Tk()
top.geometry("300x150")
LoginID = Label(top, text = "LoginID").place(x = 20,y = 40)
email = Label(top, text = "Email").place(x = 20, y = 80)
Phone = Label(top, text = "Phone").place(x = 20, y = 110)
a1 = Entry(top).place(x = 70, y = 40)
a2 = Entry(top).place(x = 70, y = 80)
a3 = Entry(top).place(x = 85, y = 110)
top.mainloop()
