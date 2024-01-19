from tkinter import *
signup=Tk()
signup.title("Registration Form")
signup.iconbitmap("D:\\python\\logo.ico")
signup.config(bg="sky blue")


lbl0=Label(signup, text="Registration Form", width=40, font=("bold",20))
lbl0.grid(row=0, column=1)

lbl1 = Label(signup, text="Name", width=0, font=("bold", 15))
lbl1.grid(row=10, column=0)
box1 = Entry(signup, width=80)
box1.grid(row=10, column=1) 

lbl2 = Label(signup, text="Age", width=0, font=("bold", 15))
lbl2.grid(row=20, column=0)
box2 = Entry(signup, width=80)
box2.grid(row=20, column=1) 


lbl3 = Label(signup, text="Address", width=0, font=("bold", 15))
lbl3.grid(row=30, column=0)
box3 = Entry(signup, width=80)
box3.grid(row=30, column=1) 

lbl4 = Label(signup, text="Email", width=0, font=("bold", 15))
lbl4.grid(row=40, column=0)
box4 = Entry(signup, width=80)
box4.grid(row=40, column=1) 

lbl5 = Label(signup, text="Password", width=0, font=("bold", 15))
lbl5.grid(row=50, column=0)
box5 = Entry(signup, width=80)
box5.grid(row=50, column=1) 

lbl6= Label(signup, text="Conform password", width=0, font=("bold", 15))
lbl6.grid(row=60, column=0)
box6 = Entry(signup, width=80)
box6.grid(row=60, column=1) 

Button(signup, text="Submit", width=20, bg="sky blue", fg="White").grid(row=80, column=1)

signup.mainloop()