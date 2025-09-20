from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Login_Window:
    def __init__(self,root):
        self.root=root
        self. root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Ridham Jasani\Documents\ridmy\Login\sunset.jpg")
        lbbg = Label(self.root,image=self.bg)
        lbbg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\Login\user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg1= Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Arial",21,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text="Username",font=("Arial",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("Arial",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("Arial",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("Arial",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        img2=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\Login\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbimg2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\Login\lock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbimg3.place(x=650,y=393,width=25,height=25)

        lgnbtn = Button(frame,command=self.login,text="Login",font=("Arial",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        lgnbtn.place(x=110,y=300,width=120,height=35)

        regbtn = Button(frame,text="New User Register",font=("Arial",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=15,y=350,width=160)  

        forbtn = Button(frame,text="Forgot Password",font=("Arial",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forbtn.place(x=10,y=370,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","ALL Field Required")
        elif self.txtuser.get()=="ridham" and self.txtpass.get()=="password":
            messagebox.showinfo("Success","Welcome Ridham")
        else:
            messagebox.showinfo("Invalid","Invalid Username and Password") 


if __name__== "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

