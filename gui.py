from tkinter import *
from tkinter import messagebox
username_exist=[

]
def signup():
    if username.get()=="" or password.get()=="":
        messagebox.showerror("error","Username and Password should be provided!")
    elif username.get() in username_exist:
        messagebox.showerror("error","The username is already taken!!!")
    elif " " in username.get() or " " in password.get():
        messagebox.showerror("error","Spaces are not allowed in password/Username!!!")
    elif len(password.get())<5:
        messagebox.showerror("error","Password is too short!!!")
    else:
        username_exist.append(username.get())
        messagebox.showinfo("Welcome","you have Signed up successfully.")
main_window=Tk()
main_window.title("SIGNUP")
main_window.resizable(True,True)
heading=Label(main_window,anchor="center",text="SIGNUP",font=("times new roman",40,"bold"),fg="orange")
heading.pack()
Label(main_window,text="First Name").pack()
first_name=Entry(main_window)
first_name.pack()
Label(main_window,text="Last Name").pack()
last_name=Entry(main_window)
last_name.pack()
Label(main_window,text="Username").pack()
username=Entry(main_window)
username.pack()
Label(main_window,text="Password").pack()
password=Entry(main_window)
password.pack()
Label(main_window).pack()
Button(main_window,text="signup",bg="orange",fg="white",width=20,command=signup).pack()
l=Label(main_window)
l.pack()
main_window.mainloop()
