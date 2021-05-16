from tkinter import *
import tkinter.filedialog
root=Tk()
root.title("SimpleTextEditor")
###
#The original artcile use those below codes to import tkinter library:

#import sys
#v=sys.python_version
#if "2.7" in v:
#    from Tkinter import *
#elif "3.3" in v or "3.4" in v:
#    from tkinter import *
#root=Tk("Text Editor")

#But I don't like it, I belive python2 will not be used for the program,so I deleted it.
text=Text(root)
text.grid()
def saveas():
    global text
    t = text.get("1.0","end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation,"w+")
    file1.write(t)
    file1.close()

button=Button(root,text="save",command=saveas)
button.grid()

def FontHelvetica():

    global text
    text.config(font="Helvetica")
def FontCourier():
    global text
    text.config(font="Courier")
font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
helvetica=IntVar() 
courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, 
command=FontHelvetica)

root.mainloop()


