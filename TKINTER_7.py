#check boxes
from tkinter import*
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x700+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

def check_get_value():
    print(check_var.get()) 

# check_var=IntVar()
check_var=StringVar()
# check_btn=Checkbutton(root,variable=check_var,onvalue=1,offvalue=0,text='Agree your terms and conditions',font=('arial',20,'bold'))
check_btn=Checkbutton(root,variable=check_var,onvalue='ON',offvalue='OFF',text='Agree your terms and conditions',font=('arial',20,'bold'))
check_btn.place(x=50,y=50)
check_var.set('0')

btn=Button(root,text="Click me",font=('times new roman',30,'bold'),fg='gold',bg='black',command=check_get_value)
btn.place(x=50,y=100)

root.mainloop()