# message box
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x700+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()


def message():
    messagebox.showinfo('Success','Successfully Submitted')

def message1():
    messagebox.showerror('Error','enter valid details')

def message2():
    messagebox.showwarning('Warning','This is last warning')

#button
Btn=Button(root,text='BUTTON 1',font=('arial',15,'bold'),bg='black',fg='gold',command=message)
Btn.place(x=50,y=100)

Btn1=Button(root,text='BUTTON 2',font=('arial',15,'bold'),bg='black',fg='gold',command=message1)
Btn1.place(x=200,y=100)

Btn2=Button(root,text='BUTTON 3',font=('arial',15,'bold'),bg='black',fg='gold',command=message2)
Btn2.place(x=350,y=100)

root.mainloop()