from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
import os
import tempfile
from time import strftime
import datetime

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
        img11=Image.open(r"C:\Users\Ridham Jasani\OneDrive\Documents\ridmy\billing\image2.jpg")
        img11=img11.resize((500,150),Image.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        lbimg11= Label(self.root,image=self.photoimage11,bg="black",borderwidth=0)
        lbimg11.place(x=0,y=0,width=500,height=130)

# Image 2
        img12=Image.open(r"C:\Users\Ridham Jasani\OneDrive\Documents\ridmy\billing\image.jpg")
        img12=img12.resize((500,130),Image.LANCZOS)
        self.photoimage12=ImageTk.PhotoImage(img12)
        lbimg12= Label(self.root,image=self.photoimage12,bg="black",borderwidth=0)
        lbimg12.place(x=500,y=0,width=500,height=130)

# Image 3
        img13=Image.open(r"C:\Users\Ridham Jasani\OneDrive\Documents\ridmy\billing\image5.jpg")
        img13=img13.resize((500,150),Image.LANCZOS)
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
        searchcombo["values"]=("ref","Medname")
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

        self.medicinetable=ttk.Treeview(sideframe,column=("ref","medname","price"),xscrollcommand=sfx.set,yscrollcommand=sfy.set)
        sfx.config(command=self.medicinetable.xview)
        sfy.config(command=self.medicinetable.yview)

        self.medicinetable.heading("ref",text="Reference No.")
        self.medicinetable.heading("medname",text="Medicine Name")
        self.medicinetable.heading("price",text="Price")
        self.medicinetable["show"]="headings"
        self.medicinetable.pack(fill=BOTH,expand=1)
        self.medicinetable.column("ref",width=100)
        self.medicinetable.column("medname",width=100)
        self.medicinetable.column("price",width=100)
        self.medicinetable.bind("<ButtonRelease-1>",self.medgetcursor)

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
        taxs=18
        self.n=self.price.get()
        self.m=self.qty.get()*self.n   
        self.l.append(self.m)
        if self.entrymed.get()=="" or self.ref_var.get()=='' or self.price.get()=='':
            messagebox.showerror("Error","Please Select Medicine.")
        else :
            qua=self.qty.get()
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("select lot from pharma where ref=%s",(self.ref_var.get(),))
            myquantity=mycursor.fetchone()
            listy=list(myquantity)
            oty=listy[0]
            if(oty>qua):   
                self.textarea.insert(END,f"\n {self.entrymed.get()}\t\t{self.qty.get()}\t\t{self.price.get()}")
                self.subtotal.set(str('Rs.%.2f'%(sum(self.l))))
                self.tax.set(str('Rs.%.2f'%((((sum(self.l))-(self.price.get()))*taxs)/100)))
                self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.price.get()))*taxs)/100)))))
            else :
                messagebox.showinfo("Quantity Error","Insufficient Quantity.")  
            conn.commit()
            self.fetchmed()
            conn.close()

    def genbill(self):
        if self.cname.get()=="" or self.cphone.get()=="" or self.cemail.get()=="":
            messagebox.showerror("Error","Please Enter Customer Details.")
        elif self.entrymed.get()=="" or self.ref_var.get=='' or self.price.get()=='':
            messagebox.showerror("Error","Please Select Medicine.")
        else:
            m=self.qty.get()
            now=datetime.datetime.now()
            # year=now.strftime("%Y")
            # month=now.strftime("%m")
            # self.date=(year,"-",month)
            self.date=now.strftime("%Y-%m-%d")
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor1=conn.cursor()
            mycursor2=conn.cursor()
            mycursor1.execute("select lot from pharma where ref=%s",(self.ref_var.get(),))
            
            myquantity=mycursor1.fetchone()
            listy=list(myquantity)
            oty=listy[0]
            if(oty>m):  
                q=oty-m            
                mycursor1.execute("update pharma set lot=%s where ref=%s",(                                                                                           
                                                                        q,
                                                                        self.ref_var.get()      
                                                                     ))
                mycursor2.execute("insert into bill values (%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.date,
                                                                                    self.billno.get(),
                                                                                    self.cname.get(),
                                                                                    self.cemail.get(),
                                                                                    self.cphone.get(),
                                                                                    self.subtotal.get(),
                                                                                    self.tax.get(),
                                                                                    self.total.get()
                                                                                    ))
                text=self.textarea.get(10.0,(10.0+float(len(self.l))))
                self.welcome()
                self.textarea.insert(END,text)
                self.textarea.insert(END,f"======================================================")
                self.textarea.insert(END,f"\n Sub Total : {self.subtotal.get()}") 
                self.textarea.insert(END,f"\n Tax : {self.tax.get()}") 
                self.textarea.insert(END,f"\n Amount Total : {self.total.get()}") 
                self.textarea.insert(END,f"\n======================================================")
                
                messagebox.showinfo("Success","Success")
            else :
                messagebox.showinfo("Quantity Error","Insufficient Quantity.")  
            conn.commit()
            self.fetchmed()
            conn.close()
          
    def savebill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.billdata=self.textarea.get(1.0,END)
            f1=open('C:/Users/Ridham Jasani/OneDrive/Documents/ridmy/billing/bills/'+str(self.billno.get())+".txt",'w')
            f1.write(self.billdata)
            messagebox.showinfo("Saved",f"Bill No.{self.billno.get()}")
            f1.close()

    def printbill(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def findbill(self):
        found="no"
        for i in os.listdir("C:/Users/Ridham Jasani/OneDrive/Documents/ridmy/billing/bills/"):
            if i.split('.')[0]==self.srchbill.get():
                f1=open(f'C:/Users/Ridham Jasani/OneDrive/Documents/ridmy/billing/bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No.")

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
        self.textarea.insert(END,"\t Welcome Ridham Pharmacy")
        self.textarea.insert(END,f"\n Bill Number : {self.billno.get()}") 
        self.textarea.insert(END,f"\n Customer Name : {self.cname.get()}") 
        self.textarea.insert(END,f"\n Phone Number : {self.cphone.get()}") 
        self.textarea.insert(END,f"\n Email Address : {self.cemail.get()}") 
        self.textarea.insert(END,f"\n======================================================")
        self.textarea.insert(END,f"\n Products\t\tQuantity\t\tPrice")
        self.textarea.insert(END,f"\n======================================================\n")


    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select ref,medname,price from pharma where "+str(self.search_var.get())+" LIKE '"+str(self.searchTxt_var.get())+"%'")

        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.medicinetable.delete(*self.medicinetable.get_children())
            for i in rows:
                self.medicinetable.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def fetchmed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select ref,medname,price from pharma")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.medicinetable.delete(*self.medicinetable.get_children())
            for i in rows:
                self.medicinetable.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    
   

    
    
    def medgetcursor(self,evenet=""):
        cursorrow=self.medicinetable.focus()
        contents=self.medicinetable.item(cursorrow)
        row=contents["values"]
        self.ref_var.set(row[0])
        self.medname_var.set(row[1])
        self.price.set(row[2])



if __name__== "__main__":
    root=Tk()
    obj=bill(root)
    root.mainloop()
