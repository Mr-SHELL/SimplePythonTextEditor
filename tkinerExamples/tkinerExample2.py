#Use pack() method
import tkinter
from tkinter import *
parent = Tk()
blbtn= Button(parent, text = "Blue", fg = "Blue")
blbtn.pack( side = TOP)
Brbtn = Button(parent, text = "Brown", fg = "Brown")
Brbtn.pack( side = LEFT)
Aqbtn = Button(parent, text = "Aqua", fg = "Aqua")
Aqbtn .pack( side = BOTTOM )
orgbtn = Button(parent, text = "Orange", fg = "Orange")
orgbtn.pack( side = RIGHT)
parent.mainloop()
#在这里，pack（）方法用于以良好的格式组织按钮。
# 它指定要放置在窗口上的一侧。