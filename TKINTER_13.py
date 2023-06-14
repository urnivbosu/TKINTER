# menu bars
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x700+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

def student_data():
    messagebox.showinfo("Success","File created")
def student_data1():
    messagebox.showinfo("Success","Window created")
def student_data2():
    messagebox.showinfo("Success","view created")



MyMenu=Menu(root)
StudentMenu=Menu(MyMenu,tearoff=0)
StudentMenu.add_command(label="New File",command=student_data)
StudentMenu.add_command(label="New Window",command=student_data1)
StudentMenu.add_command(label="New view",command=student_data2)
MyMenu.add_cascade(label="File",menu=StudentMenu)

root.config(menu=MyMenu)

root.mainloop()