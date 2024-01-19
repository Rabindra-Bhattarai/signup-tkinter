from tkinter import *
from tkinter import messagebox

def on_submit():
    messagebox.showinfo("Success", "You have successfully Signup.")

signup=Tk()

signup.title("Registration Form")
signup.iconbitmap("D:\\python\\logo.ico")
signup.geometry("600x300")

title=Label(signup, text="Sign Up", width=15, font=("bold",20))
title.grid(row=0, column=1)

name=Label(signup,text="Name").grid(row=5, column=0)
e1=Entry(signup).grid(row=5, column=1)

DOB=Label(signup,text="DOB").grid(row=10, column=0)
e1=Entry(signup).grid(row=10, column=1)

Address=Label(signup,text="Address").grid(row=15, column=0)
e1=Entry(signup).grid(row=15, column=1)


Email=Label(signup,text="Email").grid(row=20, column=0)
e1=Entry(signup).grid(row=20, column=1)


Password=Label(signup,text="Password").grid(row=25, column=0)
e1=Entry(signup).grid(row=25, column=1)

Conform_Password=Label(signup,text="Conform Password").grid(row=30, column=0)
e2=Entry(signup).grid(row=30, column=1)


submit=Button(signup, text="Submit", command=on_submit).grid(row=35, column=1)

signup.mainloop()
