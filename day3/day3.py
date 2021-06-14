from tkinter import *
from tkinter import ttk


window=Tk()
window.title("Employee Registration Form")
window.geometry('500x500')
window.configure(background="olive drab");


Form=Label(window,text="Employee Registration Form",font=("bold",15)).grid(row=0,column=1)
Employeename=Label(window ,text= "Employee name",width=20).grid(row=1,column =0)
Employeeid=Label(window ,text= "Employee id",width=20).grid(row=2,column =0)
Email=Label(window ,text= "Email",width=20).grid(row=3,column =0)
Mobile=Label(window ,text= "phone number",width=20).grid(row=4,column =0)
Address=Label(window , text="Address",width=20).grid(row=5,column=0)
City=Label(window,text="City",width=20).grid(row=6,column=0)
Country=Label(window,text="Country",width=20).grid(row=7,column=0)
Gender=Label(window,text="Gender",width=20).grid(row=8,column=0)
var = IntVar()
Radiobutton(window, text="Male",padx = 30, variable=var, value=1).grid(row = 8,column = 1)
Radiobutton(window, text="Female",padx = 20, variable=var, value=2).grid(row = 8,column = 2)

Employeename1=Entry(window,width=30).grid(row =1, column =1)
Employeeid1 =  Entry(window,width=30).grid(row=2,column=1)
Email1=Entry(window,width=30).grid(row=3,column=1)
mobile1=Entry(window,width=30).grid(row=4,column=1)
Address1=Entry(window,width=30).grid(row=5,column=1)
City1=Entry(window,width=30).grid(row=6,column=1)
Country1=Entry(window,width=30).grid(row=7,column=1)



def clicked():
   res="welcome"
   



Button(window,text="Register",command=clicked).grid(row=14,column=1)


window.mainloop()

