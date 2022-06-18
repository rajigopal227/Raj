from tkinter import *
from tkinter import ttk

window=Tk()
window.geometry("1350x750")
window.title("GRM")

def Comboclick(event):
    data=cb.get()
    messagebox.showinfo("Message",data)

lab=Label(window,text="Combo Box",bg="#2c3e50",fg="white",padx=30,pady=10,font=("times",50,"bold"))
lab.pack(fill=X)

cb=ttk.Combobox(window,width=30)
cb['values']=("---------Select----------","C","C++","Python","Java")
cb.current(0)
cb.bind("<<Combobox Selected>>",Comboclick)
cb.pack(pady=30)

sub=Button(window,text="Submit")
sub.pack(pady=30)

window.mainloop()
