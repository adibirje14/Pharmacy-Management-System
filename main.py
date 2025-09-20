from logging import root
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
import os
import tempfile
from time import strftime
import datetime
from tkinter import END

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self. root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_user=StringVar()
        self.var_pass=StringVar()


        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\1.jpg")
        lbbg = Label(self.root,image=self.bg1)
        lbbg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\user.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg1= Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Arial",21,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text="Username",font=("Arial",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_user,font=("Arial",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("Arial",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,show='*',textvariable=self.var_pass,font=("Arial",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        img2=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\user.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbimg2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\lock.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbimg3.place(x=650,y=393,width=25,height=25)

        lgnbtn = Button(frame,command=self.login,text="Login",font=("Arial",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        lgnbtn.place(x=110,y=300,width=120,height=35)

        regbtn = Button(frame,text="New User Register",command=self.registerwindow,font=("Arial",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=15,y=350,width=160)  

        forbtn = Button(frame,text="Forgot Password",command=self.forgotwindow,font=("Arial",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forbtn.place(x=10,y=370,width=160)

    def registerwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=Register(self.newwindow)

    def pharwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=PharmacyManagementSystem(self.newwindow)
        
   
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","ALL Field Required")
        elif self.txtuser.get()=="user" and self.txtpass.get()=="password":
            messagebox.showinfo("Success","Welcome User")
            self.pharwindow()
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
            mycursor=conn.cursor()
            value=(self.var_user.get(),self.var_pass.get())
            mycursor.execute("select * from register where email=%s and password=%s",value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showinfo("Invalid","Invalid Username and Password")
            else:
                openmain=messagebox.askyesno("YesNo","Access only admin")
                if openmain>0:
                    self.pharwindow()
                else:
                    if not openmain:
                        return
            conn.commit()
            conn.close

    def resetpass(self):
        if self.combo.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.secans.get()=="":
            messagebox.showerror("Error","Please Enter Answer",parent=self.root2)
        elif self.newpass.get()=="":
            messagebox.showerror("Error","Please New Password",parent=self.root2)
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
            mycursor=conn.cursor()
            que=("select * from register where email=%s and securityQ=%s and securityA=%s")
            val=(self.txtuser.get(),self.combo.get(),self.secans.get(),)
            mycursor.execute(que,val)
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter correct Answer",parent=self.root2)
            else : 
                qury=("update register set password=%s where email=%s")
                vale=(self.newpass.get(),self.txtuser.get())
                mycursor.execute(qury,vale)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password has been Reset.",parent=self.root2)

    def forgotwindow(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)
            if row!=None:
                messagebox.showerror("Error","Please Enter Valid Username.")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("Arial",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=20,relwidth=1) 

                security=Label(self.root2,text="Select Security Questions",font=("Arial",15,"bold"),fg="black",bg="white")
                security.place(x=50,y=80)
                self.combo=ttk.Combobox(self.root2,text="Contact",font=("Arial",15,"bold"),state="readonly")
                self.combo["values"]=("Select","Birth Place","Mother Name","Father Name")
                self.combo.place(x=50,y=120,width=250)
                self.combo.current(0)

                secans=Label(self.root2,text="Security Answer",font=("Arial",15,"bold"),fg="black",bg="white")
                secans.place(x=50,y=180)
                self.secans=ttk.Entry(self.root2,font=("Arial",15,"bold"))
                self.secans.place(x=50,y=220,width=250)

                newpass=Label(self.root2,text="New Password",font=("Arial",15,"bold"),fg="black",bg="white")
                newpass.place(x=50,y=260)
                self.newpass=ttk.Entry(self.root2,font=("Arial",15,"bold"))
                self.newpass.place(x=50,y=300,width=250)

                bt=Button(self.root2,text="Reset",command=self.resetpass,font=("Arial",15,"bold"),fg="white",bg="green")
                bt.place(x=140,y=360)


             




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
        

        self.bg2=ImageTk.PhotoImage(file=r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\bg.jpg")
        lbbg1 = Label(self.root,image=self.bg2)
        lbbg1.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg3=ImageTk.PhotoImage(file=r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\back.jpeg")
        lbbg2 = Label(self.root,image=self.bg3)
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

        img4=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\register.jpg")
        img4=img4.resize((150,50),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage4,command=self.regdata,borderwidth=0,cursor="hand2",font=("Arial",15,"bold"))
        b1.place(x=90,y=470,width=150,height=50)

        img5=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\login.jpeg")
        img5=img5.resize((150,50),Image.Resampling.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b2=Button(frame,command=self.loginwindow,image=self.photoimage5,borderwidth=0,cursor="hand2",font=("Arial",15,"bold"))
        b2.place(x=410,y=460,width=150,height=50)
    
    def loginwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=Login_Window(self.newwindow)

    def regdata(self):
        if self.varfname.get()=="" or self.varemail.get()=="" or self.varsecurity.get()=="Select":
            messagebox.showerror("Error","All fields required.")
        elif self.varpass.get() != self.varconpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same.")
        elif self.varcheck.get() == 0 :
            messagebox.showerror("Error","Please agree our terms & conditions.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
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

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")
        
        lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                            ,bg='white',fg="navyblue",font=("times new roman",50,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)
        
        
        
        img1=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\log.jpg")
        img1=img1.resize((80,80),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=15)
        
        #==========================addMed variable=================================
        self.addmed_var=StringVar()
        self.ref_var=StringVar()
        
        #============================================MAIN TEXT VARIABLE============================================
        self.refmed_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()
        
        
        #===========================================DATA FRAME=============================================================
        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1535,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="blue",font=("verdana",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        DataFramerRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="blue",font=("verdana",14,"bold"))
        DataFramerRight.place(x=910,y=5,width=550,height=350)
        
        
        #==============================================BUTTON FRAME========================================================
        
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1535,height=65)
        
        #================================================MAIN BUTTON=====================================================
        btnAddData=Button(ButtonFrame,text="Add Medicines",command=self.add_data,font=("comic sans ms",13,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateMed=Button(ButtonFrame,text="UPDATE",command=self.Update,font=("comic sans ms",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)
        
        btnDeleteMed=Button(ButtonFrame,text="DELETE",command=self.Delete_data,font=("comic sans ms",13,"bold"),width=14,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)
        
        btnRestMed=Button(ButtonFrame,text="RESET",command=self.reset,font=("comic sans ms",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnRestMed.grid(row=0,column=3)
        
        btnbillMed=Button(ButtonFrame,text="BILL",command=self.billwindow,font=("comic sans ms",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnbillMed.grid(row=0,column=4)
        
       
        
        #======================================SEARCH BY====================================================
        lblSearch=Label(ButtonFrame,font=("comic sans ms",18,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        
        #variable for search
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=13,font=("comic sans ms",13,"bold"),state="readonly")
        search_combo["values"]=("reg","tabletname","lotno")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        self.searchvar=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchvar,bd=3,relief=RIDGE,width=12,font=("comic sans ms",16,"bold"))
        txtSearch.grid(row=0,column=7)
                
        searchBtn=Button(ButtonFrame,command=self.searching_data,text="SEARCH",font=("comic sans ms",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("comic sans ms",13,"bold"),width=13,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
        
        #==================================LABELS AND ENTRY==========================================================================
        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma")
        row=my_cursor.fetchall()
        
        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.refmed_var,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        
        lblcompany=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2)
        lblcompany.grid(row=1,column=0,sticky=W)
        txtcompany=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtcompany.grid(row=1,column=1)
        
        
        lblMedicineType=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Type:",padx=2)
        lblMedicineType.grid(row=2,column=0,sticky=W)
        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",font=("arial",12,"bold"),width=27)
        comTypeofMedicine['value']=("Tablet","Syrup","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)
        
        #====================AddMedicine================================================================
        
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select medname from pharma")
        med=my_cursor.fetchall()
        
        
        
        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly",font=("arial",12,"bold"),width=27)
        comMedicineName['value']=med
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)
        
        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)
        
        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)
        
        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)
        
        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=4)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)
        
        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=14,pady=6)
        lblDosage.grid(row=0,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=0,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price:",padx=14,pady=6)
        lblPrice.grid(row=1,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=1,column=3)
        
        lblProductQT=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=14,pady=6)
        lblProductQT.grid(row=2,column=2,sticky=W)
        txtProductQT=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQT.grid(row=2,column=3,sticky=W)
        
        #===========================================Images=====================================================
        
        lblhome=Label(DataFrameLeft,font=("comic sans ms",14,"bold"),text="FEEL WELL, LIVE BETTER",fg="purple",padx=15,pady=6)
        lblhome.place(x=500,y=100)
        
        img2=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\icon.jpg")
        img2=img2.resize((180,165),Image.Resampling.LANCZOS)
        self.photosimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photosimg2,borderwidth=0)
        b1.place(x=480,y=310)
        
        img3=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\tablet.jpg")
        img3=img3.resize((180,165),Image.Resampling.LANCZOS)
        self.photosimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photosimg3,borderwidth=0)
        b1.place(x=740,y=310)
        
        
        #=================================DATA FRAME RIGHT======================================
        
        DataFramerRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="blue",font=("verdana",14,"bold"))
        DataFramerRight.place(x=910,y=5,width=550,height=350)
        
        img4=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\med1.jpg")
        img4=img4.resize((200,75),Image.Resampling.LANCZOS)
        self.photosimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photosimg4,borderwidth=0)
        b1.place(x=960,y=165)
        
        img5=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\ss11.jpg")
        img5=img5.resize((165,145),Image.Resampling.LANCZOS)
        self.photosimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photosimg5,borderwidth=0)
        b1.place(x=1320,y=160)
        
        img6=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\images\pill.ico")
        img6=img6.resize((150,85),Image.Resampling.LANCZOS)
        self.photosimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photosimg6,borderwidth=0)
        b1.place(x=1160,y=170)
        
        lblrefno=Label(DataFramerRight,font=("arial",12,"bold"),text="Reference No:")
        lblrefno.place(x=0,y=95)
        txtrefno=Entry(DataFramerRight,textvariable=self.ref_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=95)
        
        lblmedName=Label(DataFramerRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=130)
        txtmedName=Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=130)
        
        #===================================================SIDE FRAME=============================================
        side_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=160,width=290,height=150)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        
        #=============================================MEDICINE ADD BUTTON===================================
        down_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)
        
        btnAddmed=Button(down_frame,text="ADD",command=self.AddMed,font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)
        
        btnUpdatemed=Button(down_frame,text="UPDATE",command=self.UpdateMed,font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)
        
        btnDeletemed=Button(down_frame,text="DELETE",command=self.DeleteMed,font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)
        
        btnClearmed=Button(down_frame,text="CLEAR",command=self.ClearMed,font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)

        
        
        #==============================================FRAME DETAILS=================================================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1535,height=215)
        
        
        #===========================================MAIN TABLE AND SCROLLBAR=======================================
        Table_frame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=580,width=1535,height=215)
        
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","dosage","price","productqt")
                                         ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        
        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QTs")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        #=========================================add medicine functionality declaration==========================
        
    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(ref,medname) values(%s,%s)",(self.ref_var.get(),self.addmed_var.get()))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")
        
    def fetch_dataMed(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Aditya@1411", database="project")
            with conn.cursor() as my_cursor:
                my_cursor.execute("SELECT * FROM pharma")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.medicine_table.delete(*self.medicine_table.get_children())
                    for i in rows:
                        self.medicine_table.insert("", tk.END, values=i)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            conn.close()

        
    #=======================================MED GET CURSOR===================================================
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]

        if len(row) == 2:
            self.ref_var.set(row[0])
            self.addmed_var.set(row[1])
        
    def UpdateMed(self):
        if self.ref_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Aditya@1411", database="project")
            my_cursor = conn.cursor()

            try:
                my_cursor.execute("UPDATE pharma SET medname=%s WHERE ref=%s", (
                    self.addmed_var.get(),
                    self.ref_var.get(),
                ))
                conn.commit()
                self.fetch_dataMed()  # Ensure this method refreshes the data in the table

                # Refresh the table widget after update
                self.medicine_table.delete(*self.medicine_table.get_children())  # Clear the existing table
                self.fetch_dataMed()  # Fetch and display updated data

                messagebox.showinfo("Success", "Medicine has been Updated")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                conn.close()


    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        sql="delete from pharma where ref=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_dataMed()
        conn.close()
    
    def ClearMed(self):
        self.ref_var.set("")
        self.addmed_var.set("")
        
    #========================================MAIN TABLE==========================================================
    
    def add_data(self):
        if self.refmed_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.refmed_var.get(),
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideEffect_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.product_var.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Data has been inserted")
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]
        

        # Check if row has the expected number of columns
        if len(row) == 12:  # Ensure there are at least 12 columns in the row
            self.refmed_var.set(row[0])
            self.cmpName_var.set(row[1])
            self.typeMed_var.set(row[2])
            self.medName_var.set(row[3])
            self.lot_var.set(row[4])
            self.issuedate_var.set(row[5])
            self.expdate_var.set(row[6])
            self.uses_var.set(row[7])
            self.sideEffect_var.set(row[8])
            self.dosage_var.set(row[9])
            self.price_var.set(row[10])
            self.product_var.set(row[11])
        else:
            messagebox.showerror("Error", "The selected row does not contain enough data.")

        
    def Update(self):
        if self.refmed_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set companyname=%s,type=%s,tabletname=%s,lotno=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,dosage=%s,price=%s,productqt=%s where reg=%s",(
                                                                            self.cmpName_var.get(),
                                                                            self.typeMed_var.get(),
                                                                            self.medName_var.get(),
                                                                            self.lot_var.get(),
                                                                            self.issuedate_var.get(),
                                                                            self.expdate_var.get(),
                                                                            self.uses_var.get(),
                                                                            self.sideEffect_var.get(),
                                                                            self.dosage_var.get(),
                                                                            self.price_var.get(),
                                                                            self.product_var.get(),
                                                                             self.refmed_var.get()
                                                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()                 
            messagebox.showinfo("Success","Record has been Updated successfully")
            
    def Delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        sql="delete from pharmacy where reg=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Information Deleted Successfully")
    
    def billwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=bill(self.newwindow)
        
    def reset(self):
        #self.refmed_var.set(""),
        self.cmpName_var.set(""),
        #self.typeMed_var.set(""),
        #self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.product_var.set("")
        
    def searching_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy WHERE " + str(self.search_var.get()) + " LIKE '" + str(self.searchvar.get()) + "%'")
        rowss=my_cursor.fetchall()
        if len(rowss)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rowss:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    ##def iExit(self):
     #   answer =messagebox.askyesno("Pharmacy Management System","Do you want to exit")
     #   if answer:
     #       return root.destroy
    
class bill:
    def __init__(self,root):
        self.root=root
        self. root.title("Billing System")
        self.root.geometry("1550x800+0+0")

        self.ref_var=StringVar()
        self.medname_var=StringVar()
        self.search_var=StringVar()
        self.searchTxt_var=StringVar()

        self.cname=StringVar()
        self.cphone=StringVar()
        self.cemail=StringVar()
        self.billno=StringVar()
        z = random.randint(1000,9999)
        self.billno.set(z)
        self.srchbill=StringVar()
        self.price=IntVar()
        self.qty=IntVar()
        self.qty.set(1)
        self.subtotal=StringVar()
        self.subtotal1=IntVar()
        self.tax=StringVar()
        self.tax1=IntVar()
        self.total=StringVar()
        self.total1=IntVar()
        self.lot=IntVar()
        self.date=StringVar()

# Image 1
        img11=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\Login\ridmy\billing\image2.jpg")
        img11=img11.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        lbimg11= Label(self.root,image=self.photoimage11,bg="black",borderwidth=0)
        lbimg11.place(x=0,y=0,width=500,height=130)

# Image 2
        img12=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\Login\ridmy\billing\image.jpg")
        img12=img12.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage12=ImageTk.PhotoImage(img12)
        lbimg12= Label(self.root,image=self.photoimage12,bg="black",borderwidth=0)
        lbimg12.place(x=500,y=0,width=500,height=130)

# Image 3
        img13=Image.open(r"C:\Users\Asus\OneDrive\Desktop\Project SE\New Project\Login\ridmy\billing\image5.jpg")
        img13=img13.resize((500,150),Image.Resampling.LANCZOS)
        self.photoimage13=ImageTk.PhotoImage(img13)
        lbimg13= Label(self.root,image=self.photoimage13,bg="black",borderwidth=0)
        lbimg13.place(x=1000,y=0,width=500,height=130)


# BILLING Title         
        titlelbl=Label(self.root,text="BILLING SOFTWARE",font=("Arial",35,"bold"),fg="red",bg="white")
        titlelbl.place(x=0,y=130,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S:%p')
            lbltime.config(text=string)
            lbltime.after(1000,time)

        lbltime=Label(titlelbl,font=("Arial",15,"bold"),fg="red",bg="white")
        lbltime.place(x=0,y=0,width=120,height=45)
        time()


# Main Frame
        mainframe=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        mainframe.place(x=0,y=175,width=1530,height=620)

#-------------------------------------------------------------------------------------------------------
# Customer Frame
        custframe=LabelFrame(mainframe,text="Customer",font=("Arial",12,"bold"),fg="red",bg="white")
        custframe.place(x=10,y=5,width=400,height=140)

        # Mobile Input
        self.lblmobile=Label(custframe,text="Mobile No. :",font=("Arial",12,"bold"),fg="black",bg="white")
        self.lblmobile.grid(row=0,column=0,sticky=W,padx=5,pady=7)
        self.entrymobile=ttk.Entry(custframe,textvariable=self.cphone,font=("Arial",12,"bold"),width=18)
        self.entrymobile.grid(row=0,column=1)
        
        # Customer Name
        self.lblcust=Label(custframe,text="Name :",font=("Arial",12,"bold"),fg="black",bg="white")
        self.lblcust.grid(row=1,column=0,sticky=W,padx=5,pady=7)
        self.entrycust=ttk.Entry(custframe,textvariable=self.cname,font=("Arial",12,"bold"),width=18)
        self.entrycust.grid(row=1,column=1)
        
        # Email 
        self.lblemail=Label(custframe,text="Email :",font=("Arial",12,"bold"),fg="black",bg="white")
        self.lblemail.grid(row=2,column=0,sticky=W,padx=5,pady=7)
        self.entryemail=ttk.Entry(custframe,textvariable=self.cemail,font=("Arial",12,"bold"),width=18)
        self.entryemail.grid(row=2,column=1)

#------------------------------------------------------------------------------------------------------
# Product Frame
        proframe=LabelFrame(mainframe,text="Product",font=("Arial",12,"bold"),fg="red",bg="white")
        proframe.place(x=450,y=5,width=500,height=450)


        lblSearch=Label(proframe,font=("Arial",12,"bold"),text="Search",padx=2,bg="white",fg="red",width=6)
        lblSearch.grid(row=0,column=0,sticky=W)
        
        searchcombo=ttk.Combobox(proframe,textvariable=self.search_var,width=7,font=("Arial",10,"bold"))
        searchcombo["values"]=("reg","tabletname")
        searchcombo.grid(row=1,column=0,padx=5,pady=10)
        searchcombo.current(0)

        txtSearch=Entry(proframe,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("Arial",10,"bold"))
        txtSearch.grid(row=1,column=1,padx=5,pady=10)


        # Search Button
        searchbtn=Button(proframe,command=self.search_data,text="SEARCH",font=("Arial",10,"bold"),fg="darkgreen",bg="white",width=10)
        searchbtn.grid(row=1,column=2)

        # Show all Button
        showAll=Button(proframe,command=self.fetchmed,text="SHOW ALL",font=("Arial",10,"bold"),fg="darkgreen",bg="white",width=10)
        showAll.grid(row=1,column=3,padx=5,pady=10)

        # Ref No. in Product Info
        self.lblref=Label(proframe,text="Ref No. :",font=("Arial",10,"bold"),fg="black",bg="white")
        self.lblref.grid(row=3,column=0,sticky=W,padx=10,pady=10)
        self.entryref=ttk.Entry(proframe,textvariable=self.ref_var,font=("Arial",12,"bold"),width=15)
        self.entryref.grid(row=3,column=1)

        # Quantity in Product info
        self.lblquan=Label(proframe,text="Quantity :",font=("Arial",10,"bold"),fg="black",bg="white")
        self.lblquan.grid(row=3,column=2,sticky=W,padx=10,pady=10)
        self.entryquan=ttk.Entry(proframe,textvariable=self.qty,font=("Arial",12,"bold"),width=15)
        self.entryquan.grid(row=3,column=3)

        # Medname in Product Info
        self.lblmed=Label(proframe,text="Medname :",font=("Arial",10,"bold"),fg="black",bg="white")
        self.lblmed.grid(row=4,column=0,sticky=W,padx=10,pady=10)
        self.entrymed=ttk.Entry(proframe,textvariable=self.medname_var,font=("Arial",12,"bold"),width=15)
        self.entrymed.grid(row=4,column=1)

        # Price in Product Info
        self.lblpri=Label(proframe,text="Price :",font=("Arial",10,"bold"),fg="black",bg="white")
        self.lblpri.grid(row=5,column=0,sticky=W,padx=10,pady=10)
        self.entrypri=ttk.Entry(proframe,textvariable=self.price,font=("Arial",12,"bold"),width=15)
        self.entrypri.grid(row=5,column=1)

        #Table of Ref , Med and price
        sideframe=Frame(proframe,bd=4,relief=RIDGE,bg="white")
        sideframe.place(x=10,y=221,width=400,height=160)

        sfx=ttk.Scrollbar(sideframe,orient=HORIZONTAL)
        sfx.pack(side=BOTTOM,fill=X)
        sfy=ttk.Scrollbar(sideframe,orient=VERTICAL)
        sfy.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(sideframe,column=("reg","tabletname","price"),xscrollcommand=sfx.set,yscrollcommand=sfy.set)
        sfx.config(command=self.medicine_table.xview)
        sfy.config(command=self.medicine_table.yview)

        self.medicine_table.heading("reg",text="Reference No.")
        self.medicine_table.heading("tabletname",text="Medicine Name")
        self.medicine_table.heading("price",text="Price")
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("reg",width=100)
        self.medicine_table.column("tabletname",width=100)
        self.medicine_table.column("price",width=100)
        self.medicine_table.bind("<ButtonRelease-1>",self.medgetcursor)

        self.fetchmed()


#------------------------------------------------------------------------------------------------------
# Bill Frame
        billframe=LabelFrame(mainframe,text="Bill Area",font=("Arial",12,"bold"),fg="red",bg="white")
        billframe.place(x=1000,y=45,width=500,height=430)

        
        scrolly=Scrollbar(billframe,orient=VERTICAL)
        self.textarea=Text(billframe,yscrollcommand=scrolly.set,font=("Arial",10,"bold"),bg="white",fg="black")
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        
#------------------------------------------------------------------------------------------------------
#Search Frame 
        searchframe=LabelFrame(mainframe,bd=0,fg="red",bg="white")
        searchframe.place(x=1000,y=0,width=500,height=45)

        #Bill Number
        self.lblsubtotal=Label(searchframe,text="Bill Number : ",font=("Arial",11,"bold"),fg="white",bg="red")
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=1,pady=5)
        self.entrysearch=ttk.Entry(searchframe,textvariable=self.srchbill,font=("Arial",12,"bold"),width=21)
        self.entrysearch.grid(row=0,column=1,sticky=W,padx=10,pady=5)

        # Search Button
        self.searchbtn=Button(searchframe,command=self.findbill,text="Search",font=("Arial",11,"bold"),fg="white",bg="red",cursor="hand2",width=11)
        self.searchbtn.grid(row=0,column=2,sticky=W,padx=30,pady=10)


#------------------------------------------------------------------------------------------------------
# Bill Counter Frame        
        
        billcounterframe=LabelFrame(mainframe,text="Bill Counter",font=("Arial",12,"bold"),fg="red",bg="white")
        billcounterframe.place(x=10,y=475,width=1490,height=130)

        # Subtotal
        self.lblsubtotal=Label(billcounterframe,text="Sub Total :",font=("Arial",12,"bold"),fg="black",bg="white",bd=4)
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=5)
        self.entrysubtotal=ttk.Entry(billcounterframe,textvariable=self.subtotal,font=("Arial",12,"bold"),width=21)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        # Govt Tax
        self.lbltax=Label(billcounterframe,text="Govt. Tax :",font=("Arial",12,"bold"),fg="black",bg="white")
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=5)
        self.entrytax=ttk.Entry(billcounterframe,textvariable=self.tax,font=("Arial",12,"bold"),width=21)
        self.entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        # Total Amount
        self.lbltotal=Label(billcounterframe,text="Amount Total :",font=("Arial",12,"bold"),fg="black",bg="white")
        self.lbltotal.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        self.entrytotal=ttk.Entry(billcounterframe,textvariable=self.total,font=("Arial",12,"bold"),width=21)
        self.entrytotal.grid(row=2,column=1,sticky=W,padx=5,pady=5)


#Button Frame
        buttonframe=LabelFrame(billcounterframe,font=("Arial",12,"bold"),fg="red",bg="white",bd=0)
        buttonframe.place(x=375,y=10)

        # Add to Cart Button
        self.addcart=Button(buttonframe,command=self.additem,text="ADD to Cart",font=("Arial",21,"bold"),fg="white",bg="green",bd=4,width=11,cursor="hand2")
        self.addcart.grid(row=0,column=0,sticky=W,padx=10,pady=10)

        # Generate Bill
        self.generate=Button(buttonframe,command=self.genbill,text="Generate Bill",font=("Arial",21,"bold"),fg="white",bg="green",bd=4,width=11,cursor="hand2")
        self.generate.grid(row=0,column=1,sticky=W,padx=10,pady=10)

        # Save Bill
        self.save=Button(buttonframe,command=self.savebill,text="Save Bill",font=("Arial",21,"bold"),fg="white",bg="green",bd=4,width=9,cursor="hand2")
        self.save.grid(row=0,column=2,sticky=W,padx=10,pady=10)

        # Print
        self.print=Button(buttonframe,command=self.printbill,text="Print",font=("Arial",21,"bold"),fg="white",bg="green",bd=4,width=7,cursor="hand2")
        self.print.grid(row=0,column=3,sticky=W,padx=10,pady=10)

        # Clear
        self.clear=Button(buttonframe,command=self.clearbill,text="Clear",font=("Arial",21,"bold"),fg="white",bg="green",bd=4,width=7,cursor="hand2")
        self.clear.grid(row=0,column=4,sticky=W,padx=10,pady=10)
        
        # Exit
        self.exit=Button(buttonframe,command=self.root.destroy,text="Exit",font=("Arial",21,"bold"),fg="white",bg="red",bd=4,width=7,cursor="hand2")
        self.exit.grid(row=0,column=5,sticky=W,padx=10,pady=10)
        

#------------------------------------------------------------------------------------------------------
        self.welcome()

        self.l=[]

#------------------------------------------------------------------------------------------------------
    def additem(self):
        taxs = 18
        self.n = float(self.price.get())  # Ensure price is a float
        self.m = self.qty.get() * self.n
        self.l.append(self.m)

        if self.entrymed.get() == "" or self.ref_var.get() == '' or self.price.get() == '':
            messagebox.showerror("Error", "Please Select Medicine.")
        else:
            qua = int(self.qty.get())  # Convert qua to integer
            conn = mysql.connector.connect(host="localhost", user="root", password="Aditya@1411", database="project")
            mycursor = conn.cursor()
            mycursor.execute("select lotno from pharmacy where reg=%s", (self.ref_var.get(),))
            myquantity = mycursor.fetchone()
            
            if myquantity is not None:
                oty = int(myquantity[0])  # Convert oty to integer
                
                if oty > qua:
                    self.textarea.insert(END, f"\n {self.entrymed.get()}\t\t{self.qty.get()}\t\t{self.price.get()}")
                    self.subtotal.set(str('Rs.%.2f' % (sum(self.l))))
                    self.tax.set(str('Rs.%.2f' % ((((sum(self.l)) - (self.price.get())) * taxs) / 100)))
                    self.total.set(str('Rs.%.2f' % ((sum(self.l)) + ((((sum(self.l)) - (self.price.get())) * taxs) / 100))))
                else:
                    messagebox.showinfo("Quantity Error", "Insufficient Quantity.")
            else:
                messagebox.showerror("Error", "Medicine not found in the database.")
            
            conn.commit()
            self.fetchmed()
            conn.close()


    def genbill(self):
        if self.cname.get() == "" or self.cphone.get() == "" or self.cemail.get() == "":
            messagebox.showerror("Error", "Please Enter Customer Details.")
        elif self.entrymed.get() == "" or self.ref_var.get() == '' or self.price.get() == '':
            messagebox.showerror("Error", "Please Select Medicine")
        else:
            m = int(self.qty.get())  # Convert m to integer
            now = datetime.datetime.now()
            self.date = now.strftime("%Y-%m-%d")
            
            conn = mysql.connector.connect(host="localhost", user="root", password="Aditya@1411", database="project")
            mycursor1 = conn.cursor()
            mycursor2 = conn.cursor()
            
            mycursor1.execute("select lotno from pharmacy where reg=%s", (self.ref_var.get(),))
            myquantity = mycursor1.fetchone()
            
            if myquantity is not None:
                oty = int(myquantity[0])  # Convert oty to integer
                
                if oty > m:  
                    q = oty - m
                    mycursor1.execute("update pharmacy set lotno=%s where reg=%s", (
                        q,
                        self.ref_var.get()
                    ))
                    
                    mycursor2.execute("insert into bill values (%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.date,
                        self.billno.get(),
                        self.cname.get(),
                        self.cemail.get(),
                        self.cphone.get(),
                        self.subtotal.get(),
                        self.tax.get(),
                        self.total.get()
                    ))
                    
                    text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
                    self.welcome()
                    self.textarea.insert(END, text)
                    self.textarea.insert(END, f"======================================================")
                    self.textarea.insert(END, f"\n Sub Total : {self.subtotal.get()}") 
                    self.textarea.insert(END, f"\n Tax : {self.tax.get()}") 
                    self.textarea.insert(END, f"\n Amount Total : {self.total.get()}") 
                    self.textarea.insert(END, f"\n======================================================")
                    
                    messagebox.showinfo("Success", "Bill Generated Successfully!")
                else:
                    messagebox.showinfo("Quantity Error", "Insufficient Quantity.")
            else:
                messagebox.showerror("Error", "Medicine not found in the database.")
            
            conn.commit()
            self.fetchmed()
            conn.close()

          
    def savebill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.billdata=self.textarea.get(1.0,END)
            f1=open('C:/Users/Asus/OneDrive/Desktop/Project SE/New Project/Login/ridmy/billing/bills/'+str(self.billno.get())+".txt",'w')
            f1.write(self.billdata)
            messagebox.showinfo("Saved",f"Bill No.{self.billno.get()}")
            f1.close()

    def printbill(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def findbill(self):
        found = "no"
        bills_directory = "C:/Users/Asus/OneDrive/Desktop/Project SE/New Project/Login/ridmy/billing/bills/"

        for i in os.listdir(bills_directory):
            if i.split('.')[0] == self.srchbill.get():
                try:
                    # Open the file with utf-8 encoding
                    with open(f'{bills_directory}{i}', 'r', encoding='utf-8') as f1:
                        self.textarea.delete(1.0, END)
                        for d in f1:
                            self.textarea.insert(END, d)
                    found = "yes"
                    break  # Exit the loop once the bill is found
                except UnicodeDecodeError:
                    messagebox.showerror("Error", "The bill file contains unsupported characters.")
                    found = "yes"  # Mark as found to avoid triggering the "Invalid Bill No." error

        if found == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clearbill(self):
        self.textarea.delete(1.0,END)
        self.ref_var.set("")
        self.medname_var.set("")
        self.cname.set("")
        self.cphone.set("")
        self.cemail.set("")
        x=random.randint(1000,9999)
        self.billno.set(x)
        self.srchbill.set("")
        self.price.set("")
        self.qty.set(1)
        self.subtotal.set("")
        self.tax.set("")
        self.total.set("")
        self.welcome()




    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome Sunshine Pharmacy")
        self.textarea.insert(END,f"\n Bill Number : {self.billno.get()}") 
        self.textarea.insert(END,f"\n Customer Name : {self.cname.get()}") 
        self.textarea.insert(END,f"\n Phone Number : {self.cphone.get()}") 
        self.textarea.insert(END,f"\n Email Address : {self.cemail.get()}") 
        self.textarea.insert(END,f"\n======================================================")
        self.textarea.insert(END,f"\n Products\t\tQuantity\t\tPrice")
        self.textarea.insert(END,f"\n======================================================\n")


    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        mycursor=conn.cursor()
        mycursor.execute("select reg,tabletname,price from pharmacy where "+str(self.search_var.get())+" LIKE '"+str(self.searchTxt_var.get())+"%'")

        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def fetchmed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@1411",database="project")
        mycursor=conn.cursor()
        mycursor.execute("select reg,tabletname,price from pharmacy")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def medgetcursor(self,evenet=""):
        cursorrow=self.medicine_table.focus()
        contents=self.medicine_table.item(cursorrow)
        row=contents["values"]
        self.ref_var.set(row[0])
        self.medname_var.set(row[1])
        self.price.set(row[2])

if __name__== "__main__":
    main()
 



          

