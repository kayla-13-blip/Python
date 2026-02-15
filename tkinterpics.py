from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning('Alert', 'Stop! Virus Found.')
Button = Button(root, text="Scan for virus", command=msg)   
Button.place(x=40, y=80)
root.mainloop()
