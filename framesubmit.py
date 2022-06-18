from tkinter import *
window=Tk()
window.title("Frame")
window.geometry("800x400")

frame=Frame(window,highlightbackground="black",highlightthicknes=2,padx=20,pady=20)
frame.grid(row=0,column=0,padx=50,pady=50)

title=Label(frame,text="REGISTRATION",font=("times",15,"bold"),fg="green")
title.grid(columnspan=2)

name=Label(frame,text="Name",font=("times",15,"bold"),pady=10)
name.grid(row=1,column=0)

txtname=Entry(frame,font=("times",15,"bold"))
txtname.grid(row=1,column=1)

mail=Label(frame,text="Mail",font=("times",15,"bold"),pady=10)
mail.grid(row=2,column=0)

txtmail=Entry(frame,font=("times",15,"bold"))
txtmail.grid(row=2,column=1)

add=Label(frame,text="Address",font=("times",15,"bold"),pady=10)
add.grid(row=3,column=0)

txtadd=Entry(frame,font=("times",15,"bold"))
txtadd.grid(row=3,column=1)

sub=Button(frame,text="Submit",bg="green",fg="white",width=5,padx=20,pady=5,font=("times",15,"bold"))
sub.grid(row=4,column=1,sticky=N)

clr=Button(frame,text="Clear",bg="green",fg="white",width=5,padx=20,pady=5,font=("times",15,"bold"))
clr.grid(row=4,column=2,sticky=E)

window.mainloop()
