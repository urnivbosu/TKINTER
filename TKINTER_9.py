#Student entry form
from tkinter import*
from tkinter import ttk
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("700x800+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()

#function declaration
def show_data():
    if check_var.get()=='ON':
        get_data=f'Name:{name_var.get()}\nEmail:{email_var.get()}\nGender:{gender_var.get()}'
        my_data.config(text=get_data,font=('arial',15,'bold'))
    else:
        my_data.config(text='Please accept our Terms and Conditions.')
#TITLE
title_name=Label(root,text="STUDENT ENTRY FORM",font=('arial',30,'bold'),bg='yellow',fg='blue')
title_name.pack(side=TOP)

#FRAME
main_frame=Frame(root,bd=5,relief=RIDGE)
main_frame.place(x=20,y=70,width=650,height=650)

#LABELS
name=Label(main_frame,text='STUDENT NAME :',font=('arial',15,'bold'))
name.grid(row=0,column=0,padx=10,pady=10,sticky=W)

email=Label(main_frame,text='STUDENT EMAIL :',font=('arial',15,'bold'))
email.grid(row=1,column=0,padx=10,pady=10,sticky=W)

gender=Label(main_frame,text='GENDER :',font=('arial',15,'bold'))
gender.grid(row=2,column=0,padx=10,pady=10,sticky=W)

#variables
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
check_var=StringVar()

#ENTRY FIELDS
name_entry=Entry(main_frame,textvariable=name_var,font=('arial',15,'bold'),width=20,highlightthickness=2)
name_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

email_entry=Entry(main_frame,textvariable=email_var,font=('arial',15,'bold'),width=20,highlightthickness=2)
email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

#RADIOBUTTON
male=Radiobutton(main_frame,variable=gender_var,text='MALE',value='Male',font=('arial',15,'bold'))
male.grid(row=2,column=1,padx=10,pady=10,sticky=W)
gender_var.set('male')

female=Radiobutton(main_frame,variable=gender_var,text='FEMALE',value='Female',font=('arial',15,'bold'))
female.grid(row=3,column=1,padx=10,pady=10,sticky=W)

#checkbutton
check_btn=Checkbutton(main_frame,variable=check_var,onvalue='ON',offvalue='OFF',text='Agree our Terms and Condition',font=('arial',15,'bold'))
check_btn.grid(row=4,column=1,padx=10,pady=10,sticky=W)
check_var.set('OFF')

#Button
Btn=Button(main_frame,text='SHOW DATA',font=('arial',15,'bold'),bg='black',fg='gold',command=show_data)
Btn.grid(row=5,column=1,padx=10,pady=10,sticky=W)

my_data=Label(main_frame,text='',font=('arial',15,'bold'))
my_data.grid(row=6,column=1,padx=10,pady=10,sticky=W)


root.mainloop()