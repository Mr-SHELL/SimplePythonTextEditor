#在GUI窗口上使用Label窗口小部件。
import tkinter as tk
window = tk.Tk()
frame = tk.Frame(master=window, width=1000, height=1000)
frame.pack()
lab1 = tk.Label(master=frame, text="Points at (50, 59)", bg="Aqua")
lab1.place(x=50, y=59)
lab2 = tk.Label(master=frame, text="Points at (665, 665)", bg="Pink")
lab2.place(x=665, y=665)
window.mainloop()

#在这里，代码产生了这样的窗口。我们已经导入了一个Tkinter包，并定义了一个窗口。
#接下来，定义标签以在窗口上显示带有点的输出。每个标签都给出了比例尺点。
#最后，执行mainloop来触摸事件。