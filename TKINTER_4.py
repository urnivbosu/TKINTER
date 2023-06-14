#text box so that we can put enter (nextline) int the text box
from tkinter import*
root=Tk()
root.title("My first GUI") 
root.geometry("500x500+0+0") 
root.wm_iconbitmap()
#root.resizable(False,False)


def click():
    text1="Address: "+text_box.get('1.0',END)# Inputing the string for the textbox
    lbl.config(text=str(text1))  

#variables
#name_var=StringVar()

# entry=Entry(root,textvariable=name_var,width=50,font=("arial,15"),bg='red')
# entry.place(x=0,y=10,relwidth=1)

text_box=Text(root,font=('arial',20))  #declaring a textbox
text_box.place(x=0,y=70,relwidth=0.50,relheight=0.35)#size of textbox
#making the dimensions of the text box


Mybutton=Button(root,text="Click me",font=('times new roman',30,'bold'),fg='gold',bg='black',command=click)
#size of click box
Mybutton.place(x=200,y=300)   

lbl=Label(root,text="",font=('arial',15)) 
lbl.place(x=200,y=400)# for the text under the click box



root.mainloop()