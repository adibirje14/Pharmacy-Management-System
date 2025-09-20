from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    
    
    def __init__(self,root):
        self.root=root
        self. root.title("Register")
        self.root.geometry("1600x800+0+0")

        self.varfname=StringVar()
        self.varlname=StringVar()
        self.varcontact=StringVar()
        self.varemail=StringVar()
        self.varsecurity=StringVar()
        self.varsecurityans=StringVar()
        self.varpass=StringVar()
        self.varconpass=StringVar()
        

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Ridham Jasani\Documents\ridmy\register\bg.jpg")
        lbbg1 = Label(self.root,image=self.bg1)
        lbbg1.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg2=ImageTk.PhotoImage(file=r"C:\Users\Ridham Jasani\Documents\ridmy\register\back.jpeg")
        lbbg2 = Label(self.root,image=self.bg2)
        lbbg2.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        registerlbl=Label(frame,text="Register Here",font=("Arial",20,"bold"),fg="darkgreen",bg="white")
        registerlbl.place(x=20,y=20)
       

        fname=Label(frame,text="First Name",font=("Arial",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)
        self.fnameentry=ttk.Entry(frame,textvariable=self.varfname,font=("Arial",15,"bold"))
        self.fnameentry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("Arial",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)
        self.lnameentry=ttk.Entry(frame,textvariable=self.varlname,font=("Arial",15,"bold"))
        self.lnameentry.place(x=370,y=130,width=250)
        
        contact=Label(frame,text="Contact",font=("Arial",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=180)
        self.contact=ttk.Entry(frame,textvariable=self.varcontact,font=("Arial",15,"bold"))
        self.contact.place(x=50,y=210,width=250)

        email=Label(frame,text="Email",font=("Arial",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=180)
        self.email=ttk.Entry(frame,textvariable=self.varemail,font=("Arial",15,"bold"))
        self.email.place(x=370,y=210,width=250)

        security=Label(frame,text="Select Security Questions",font=("Arial",15,"bold"),fg="black",bg="white")
        security.place(x=50,y=260)
        self.combo=ttk.Combobox(frame,text="Contact",textvariable=self.varsecurity,font=("Arial",15,"bold"),state="readonly")
        self.combo["values"]=("Select","Birth Place","Mother Name","Father Name")
        self.combo.place(x=50,y=290,width=250)
        self.combo.current(0)

        secans=Label(frame,text="Security Answer",font=("Arial",15,"bold"),fg="black",bg="white")
        secans.place(x=370,y=260)
        self.secans=ttk.Entry(frame,textvariable=self.varsecurityans,font=("Arial",15,"bold"))
        self.secans.place(x=370,y=290,width=250)

        password=Label(frame,text="Password",font=("Arial",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=340)
        self.password=ttk.Entry(frame,textvariable=self.varpass,font=("Arial",15,"bold"))
        self.password.place(x=50,y=370,width=250)

        conpassword=Label(frame,text="Confirm Password",font=("Arial",15,"bold"),fg="black",bg="white")
        conpassword.place(x=370,y=340)
        self.conpassword=ttk.Entry(frame,textvariable=self.varconpass,font=("Arial",15,"bold"))
        self.conpassword.place(x=370,y=370,width=250)

        self.varcheck=IntVar()
        chkbtn = Checkbutton(frame,variable=self.varcheck,text="I agree terms & conditions",font=("Arial",11,"bold"),onvalue=1,offvalue=0)
        chkbtn.place(x=50,y=420)

        img1=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\register\register.jpg")
        img1=img1.resize((150,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.regdata,borderwidth=0,cursor="hand2",font=("Arial",15,"bold"))
        b1.place(x=90,y=470,width=150,height=50)

        img2=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\register\login.jpeg")
        img2=img2.resize((150,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        b2=Button(frame,image=self.photoimage2,borderwidth=0,cursor="hand2",font=("Arial",15,"bold"))
        b2.place(x=410,y=460,width=150,height=50)

    def regdata(self):
        if self.varfname.get()=="" or self.varemail.get()=="" or self.varsecurity.get()=="Select":
            messagebox.showerror("Error","All fields required.")
        elif self.varpass.get() != self.varconpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same.")
        elif self.varcheck.get() == 0 :
            messagebox.showerror("Error","Please agree our terms & conditions.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            query=("select * from register where email =%s")
            value=(self.varemail.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Registered, please try another email.")
            else : 
                mycursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.varfname.get(),
                                                                                        self.varlname.get(),
                                                                                        self.varcontact.get(),
                                                                                        self.varemail.get(),
                                                                                        self.varsecurity.get(),
                                                                                        self.varsecurityans.get(),
                                                                                        self.varpass.get(),
                                                                                      ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully.")



if __name__== "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

