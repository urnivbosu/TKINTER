#Radio buttons

from tkinter import*
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("500x500+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

gender=StringVar()

def gender_get():
    print(gender.get())
    

male=Radiobutton(root,variable=gender,value='male',text='Male')
male.place(x=50,y=50)
gender.set('Male')

female=Radiobutton(root,variable=gender,value='female',text='female')
female.place(x=200,y=50)

butt=Button(root,text="Click me",font=('times new roman',30,'bold'),fg='gold',bg='black',command=gender_get)
butt.place(x=125,y=100)

root.mainloop()