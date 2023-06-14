#designing
from tkinter import*
from tkinter import ttk
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x700+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

title=Label(root,text='COURSE DETAILS',font=('arial',25,'bold'),bg='white',fg='red',bd=5,relief=RAISED)
# for border of the title, we can use SUNKEN, RAISED, RIDGE
title.place(x=0,y=0,relwidth=1)

# name=Entry(root,font=('times new roman',12,'bold'),highlightthickness=3,bd=2,relief=RIDGE,bg="light yellow",fg='green',show='*')
# name.place(x=0,y=50,relwidth=1)

name=ttk.Entry(root,font=('times new roman',12,'bold'))
name.place(x=0,y=50,relwidth=1)

btn=Button(root,text='Course Details',font=('arial',12,'bold'),bg='green',fg='blue',activebackground='blue',activeforeground='green',bd=3,relief=RIDGE,cursor='hand1')
btn.place(x=300,y=100,relwidth=0.2,width=200)   





root.mainloop()