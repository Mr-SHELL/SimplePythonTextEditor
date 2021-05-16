#messagbox pump out.
import tkinter
import tkinter.messagebox
import datetime 
def displaydate():
    now = datetime.datetime.now()
    disp = 'Today date is: {}'.format(now)
    tkinter.messagebox.showinfo("Information", disp)
root = tkinter.Tk()
root.title('Pop up MessageBox')
butn = tkinter.Button(root, text="Display Dat", padx=7, pady=7, width=12,
command=displaydate)
butn.pack(pady=11)
root.geometry('400x400+400+350')
root.mainloop()