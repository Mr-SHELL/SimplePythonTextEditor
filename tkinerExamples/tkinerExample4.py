#Using Check box -mainloop() is executed
from tkinter import *
root = Tk()
root.geometry("400x300")
aa = Label(root, text ='EDUCBA-Online ', font = "60")
aa.pack()
Chckbtn1 = IntVar()
Chckbtn2 = IntVar()
Chckbtn3 = IntVar()
Btn1 = Checkbutton(root, text = "Courses",
variable = Chckbtn1,
onvalue = 2,
offvalue = 0,
height = 3,
width = 12)
Btn2 = Checkbutton(root, text = "Free-Trial",
variable = Chckbtn2,
onvalue = 3,
offvalue = 0,
height = 3,
width = 12)
Btn3 = Checkbutton(root, text = "Paid",
variable = Chckbtn3,
onvalue = 1,
offvalue = 0,
height = 2,
width = 10)
Btn1.pack()
Btn2.pack()
Btn3.pack()
mainloop()

#当我们执行以上代码时，我们会看到一个弹出窗口，其中包含标题，一些标签和按钮单击。
#我们使用了Tk类来创建主窗口，并使用pack（）方法将其放置在父窗口中。
#在这里，使用command关键字指定处理单击事件的功能，这是一个复选框。