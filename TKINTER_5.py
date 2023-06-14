#creating my onw page with one enter bloack and one address block
from tkinter import*
root=Tk()
root.title("My first GUI") 
root.geometry("500x500+0+0") 
root.wm_iconbitmap()
#root.resizable(False,False)


def click():
    text1="Address: "+text_box.get('1.0',END)# Inputing the string for the textbox
    lbl.config(text=str(text1))  

def click1():
    text2="Name: "+entry.get()# Inputing the string for the textbox
    lbl1.config(text=str(text2)) 

#variables
name_var=StringVar()

entry=Entry(root,textvariable=name_var,width=50,font=("arial,15"),bg='red')
entry.place(x=10,y=10,relwidth=0.5)

text_box=Text(root,font=('arial',20))  #declaring a textbox
text_box.place(x=10,y=150,relwidth=0.5,relheight=0.5)#size of textbox
#making the dimensions of the text box


Mybutton=Button(root,text="Click me for address",font=('times new roman',15,'bold'),fg='gold',bg='black',command=click)
#size of click box
Mybutton.place(x=10,y=600) 

Mybutton1=Button(root,text="Click me for name ",font=('times new roman',15,'bold'),fg='gold',bg='black',command=click1)
#size of click box
Mybutton1.place(x=10,y=50)

lbl=Label(root,text="",font=('arial',15)) 
lbl.place(x=10,y=650)# for the text under the click box

lbl1=Label(root,text="",font=('arial',15)) 
lbl1.place(x=10,y=100)# for the text under the click box


root.mainloop()