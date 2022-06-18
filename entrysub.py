from tkinter import *
window=Tk()
window.geometry("1350x750")
window.title("GRM Infotech")

def getdata():
    data=txtName.get()
    lab=Label(window,text=data,font=("times",15,"bold"),fg="green")
    lab.pack(fill=X)

txtName=Entry(window,width=30,font=("times",20),selectbackground="black",selectforeground="yellow")
txtName.pack()

btn=Button(window,text="Submit",font=("times",20),width=10,padx=30,pady=10,bg="green",fg="white",command=getdata)
btn.pack()

window.mainloop()
    
