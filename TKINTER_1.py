

from tkinter import*
root=Tk()#making the tool kit
root.title("My first GUI") #title of the window
root.geometry("1530x800+0+0") #size of the window(width, height, xaxis, yxais)
root.wm_iconbitmap()#for setting the icon
root.resizable(False,False)#for disabling the full size button
root.mainloop() #stay in the window (window will appear for infinite time)
