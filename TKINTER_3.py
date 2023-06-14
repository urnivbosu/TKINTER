#creating input field and buttons in TKINTER
from tkinter import*
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("1530x800+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()#for setting the icon
root.resizable(False,False)#for disabling the full size button
#for input field
entry=Entry(root,width=50,font=("arial,15"))#for the input box
entry.pack(padx=20,pady=20)

def click():
    text1="hello kaise ho " + entry.get()#linking with the entry (input box)
    lbl=Label(root,text=text1,font=('arial',15)) #property of the text to be printed
    lbl.pack()#creating the function click which prins something

Mybutton=Button(root,text="Click me",font=('times new roman',30,'bold'),fg='gold',bg='black',command=click)
Mybutton.pack(padx=50,pady=50)#creating the button and linking it with click function
#padx and pady maintains the distance of the button from x axis and y axis

root.mainloop()