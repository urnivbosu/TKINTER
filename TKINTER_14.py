#Scroll bar
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x700+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

myframe=Frame(root,bd=3,relief=RIDGE)
myframe.place(x=200,y=50,width=200,height=250)

scroll_x=Scrollbar(myframe,orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM,fill=X)

scroll_y=Scrollbar(myframe,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)



mylist=Listbox(myframe,font=("arial",14,"bold"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
mylist.pack()

scroll_x.config(command=mylist.xview)
scroll_y.config(command=mylist.yview)
for i in range(0,21):
    mylist.insert(END,f'Python Version:{i}')

root.mainloop()


