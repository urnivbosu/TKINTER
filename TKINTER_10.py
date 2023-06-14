#combobox
from tkinter import*
from tkinter import ttk
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x800+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

#function
def show_data():
    print(mycombo.get())

#combobox
mycombo=ttk.Combobox(root,justify='center',font=('arial',15,),width=25,state='readonly')
mycombo['value']=('Python','Java','Javascript','HTML')
mycombo.set('Select Option')
mycombo.place(x=100,y=50)

#button
Btn=Button(root,text='SHOW DATA',font=('arial',15,'bold'),bg='black',fg='gold',command=show_data)
Btn.place(x=170,y=200)

root.mainloop()