#listbox
from tkinter import*
from tkinter import ttk
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x700+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

def show_data():
    cursor=listbox1.curselection()
    #print(cursor)
    for item in cursor:
        print(listbox1.get(item))

    #print(listbox1.get())
    listbox1.delete(cursor)

course=['python','django','java','Tkinter','html']

listbox1=Listbox(root,font=("arial",15,"bold"))
listbox1.place(x=100,y=50)

for i in course:
    listbox1.insert(END,i)

#button
Btn=Button(root,text='SHOW DATA',font=('arial',15,'bold'),bg='black',fg='gold',command=show_data)
Btn.place(x=170,y=330)

root.mainloop()