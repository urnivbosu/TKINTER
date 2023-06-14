from tkinter import*
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("500x500+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()#for setting the icon(and uploading the icon)
#root.resizable(False,False)#for disabling the full size button
#PACK------------------------
# lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',30,'bold')) #text to be print
# lbl1.pack(side=LEFT)  #top,left,right, bottom method

# lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',30,'bold')) #text to be print
# lbl1.pack(side=RIGHT)

# lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',30,'bold')) #text to be print
# lbl1.pack(side=TOP)

# lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',30,'bold')) #text to be print
# lbl1.pack(side=BOTTOM)

#GRID-------------------------------
# lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',15,'bold')) #text to be print
# lbl1.grid(row=0,column=0)

# lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',15,'bold')) #text to be print
# lbl1.grid(row=0,column=1)

#PLACE
lbl1=Label(root,text="URNIV_BOSU",font=('times new roman',30,'bold')) #text to be print
lbl1.place(x=100,y=100)




root.mainloop() #stay in the window (window will appear for infinite time)