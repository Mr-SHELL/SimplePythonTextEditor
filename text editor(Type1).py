from tkinter import *
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
root.mainloop()


