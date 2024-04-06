import random
import time
import datetime
import PIL
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import END
import tempfile
import os


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\pexels-anna-shvets-3683088.jfif")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open(r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\user.png")
        img1 = img1.resize((100,100),PIL.Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=220)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=255,width=270)

        #***********Icon Image**********************
        img2 = Image.open(r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\user.png")
        img2 = img2.resize((25,25),PIL.Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3 = Image.open(r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\lock.png")
        img3 = img3.resize((25,25),PIL.Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        #Login button
        loginbtn=Button(frame,text="login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #Register
        registerbtn=Button(frame,text="New user register",command=self.register_form,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)

        #Forgotpassbtn
        forgotbtn=Button(frame,text="Forget Password",command=self.forgotpass_form,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=20,y=380,width=160)
    
    def register_form(self):
        self.new_window1=Toplevel(self.root)
        self.app=Register_Window(self.new_window1)

    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","all fields required",parent=self.root)
        
        else:
            conn1=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            cur1=conn1.cursor()
            cur1.execute("select * from register where Email=%s and Password=%s",(
                                                                                  self.txtuser.get(),
                                                                                  self.txtpassword.get()))
            row=cur1.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password",parent=self.root)  
            else:
                open_main=messagebox.askyesno("Yes/No","Acess only for admin",parent=self.root)
                if open_main>0:
                    self.new_window2=Toplevel(self.root)
                    self.app=Hospital(self.new_window2)
                else:
                   if not open_main:
                      return
            conn1.commit()
            conn1.close()
                        
             

    #*****************Reset function************
    def Reset_pass(self):
       if self.combo_security_Q.get()=="select":
          messagebox.showerror("Error","Select security question",parent=self.root2)
       elif self.Esecurity.get()=="":
          messagebox.showerror("Error","Please enter the answer",parent=self.root2)
       elif self.newpass.get=="":
          messagebox.showerror("Error","Please enter the new password,",parent=self.root2)
       else:
          conn1=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
          cur1=conn1.cursor()
          query=("select * from register where Email=%s and Security_Q=%s and Security_A=%s")
          value=(self.txtuser.get(),self.combo_security_Q.get(),self.Esecurity.get())
          cur1.execute(query,value)
          row=cur1.fetchone()
          if row==None:
             messagebox.showerror("Error","Please enter corect answer",parent=self.root2)
          else:
             query=("update register set Password=%s where Email=%s")
             value=(self.newpass.get(),self.txtuser.get())
             cur1.execute(query,value)

             conn1.commit()
             conn1.close()
             messagebox.showinfo("Info","Your password is reset , please login using new password",parent=self.root2)   
             self.root2.destroy()
    
    def forgotpass_form(self):
       if self.txtuser.get()=="":
          messagebox.showerror("Error","Please enter the email address to reset the password")
       else:
           conn1=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
           cur1=conn1.cursor()
           query=("select * from register where Email=%s")
           value=(self.txtuser.get(),)
           cur1.execute(query,value)
           row=cur1.fetchone()

           if row==None:
              messagebox.showerror("Error","Please enter the valid username")
           else:
              conn1.close()
              self.root2=Toplevel()
              self.root2.title("Forgot Password")
              self.root2.geometry("349x450+610+170")

              l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="Red",bg="white")   
              l.place(x=0,y=10,relwidth=1)

              security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
              security_Q.place(x=50,y=80)
                 
              self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",10,"bold"),state="readonly")
              self.combo_security_Q["values"]=("Select","Your Birthday Place","Your Bestfriend Name","Your Pet Name","Your School Name")
              self.combo_security_Q.place(x=50,y=110,width=250)
              self.combo_security_Q.current(0)

              security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
              security_A.place(x=50,y=150)

              self.Esecurity=ttk.Entry(self.root2,font=("times new roman",12))
              self.Esecurity.place(x=50,y=180,width=250)

              new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
              new_pass.place(x=50,y=220)

              self.newpass=ttk.Entry(self.root2,font=("times new roman",12))
              self.newpass.place(x=50,y=250,width=250)

              btn=Button(self.root2,text="Reset",command=self.Reset_pass,font=("times new roman",12,"bold"),fg="white",bg="green")
              btn.place(x=100,y=290)
                    


class Register_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #***********Text Variable*************
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confirmpass=StringVar()
        self.var_check=IntVar()
        
       #***********Background Image************
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\pexels-daniel-frank-287227.jfif")
        bg_lbl2=Label(self.root,image=self.bg)
        bg_lbl2.place(x=0,y=0,relwidth=1,relheight=3)

        #*************Left Side Image*************
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\gettyimages-1207212239-612x612.jfif")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=350)


        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=600,height=500)

        register_lbl=Label(frame,text="ADMIN REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #****************Label and entry ******************

        #*****row1*************
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12))
        self.fname_entry.place(x=50,y=130,width=250)

        txtlname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        txtlname.place(x=370,y=100)

        self.lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",12))
        self.lname.place(x=370,y=130,width=250)
        
        #*********row2*************
        txtcontact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        txtcontact.place(x=50,y=170)

        self.contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        self.contact.place(x=50,y=200,width=250)
        

        txtEmail=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        txtEmail.place(x=370,y=170)

        self.Email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",12))
        self.Email.place(x=370,y=200,width=250)

        #**********row3**************
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",10,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birthday Place","Your Bestfriend Name","Your Pet Name","Your School Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)

        self.Esecurity=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",12))
        self.Esecurity.place(x=370,y=270,width=250)


        #**************row4*******
        txtRpassword=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        txtRpassword.place(x=50,y=310)

        self.Rpassword=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",12))
        self.Rpassword.place(x=50,y=340,width=250)


        txtconpassword=Label(frame,text="Conform Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        txtconpassword.place(x=370,y=310)

        self.cpassword=ttk.Entry(frame,textvariable=self.var_confirmpass,font=("times new roman",12))
        self.cpassword.place(x=370,y=340,width=250)

        
        #*************Check box**********
        checkbtn=Checkbutton(frame,text="I Agree The Terms And Conditions",variable=self.var_check,font=("times new roman",10,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #*******Buttons**************

        img=Image.open(r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\th.jfif")
        img=img.resize((100,35),PIL.Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=50,y=420,width=100)


        img1=Image.open(r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\th2.jfif")
        img1=img1.resize((120,45),PIL.Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=370,y=420,width=120)

    def register(self):
        if self.var_fname.get()=="" or self.var_contact.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select" or self.var_securityA.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Password and Conformpassword must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our term and conditions",parent=self.root)
        else:
            conn1=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            cur1=conn1.cursor()
            query=("select * from register where Email=%s")
            value=(self.var_email.get(),)
            cur1.execute(query,value)
            row=cur1.fetchone()
            if row!=None:
                messagebox("Error","User already exists,please try another Email",parent=self.root)
            else:
                cur1.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get(),
                                                                                    self.var_confirmpass.get()))
            conn1.commit()
            conn1.close()           
            messagebox.showinfo("Sucess","Register sucessfully ,Click Login button for login",parent=self.root)       


    def return_login(self):
       self.root.destroy()



class Hospital:
   def __init__(self,root):
      self.root=root
      self.root.title("Hospital Management System")
      self.root.geometry("1540x800+0+0")
        
      self.Nameoftablets=StringVar()
      self.ref=StringVar()
      self.Dose=StringVar()
      self.NoOfTablets=StringVar()
      self.Lot=StringVar()
      self.IssueDate=StringVar()
      self.ExpDate=StringVar()
      self.DailyDose=StringVar()
      self.SideEfect=StringVar()
      self.FurtherInformation=StringVar()
      self.BloodPressure=StringVar()
      self.StorageAdvice=StringVar()
      self.DrivingUsingMachine=StringVar()
      self.HowToUseMedication=StringVar()
      self.PatientId=StringVar()
      self.nhsNumber=StringVar()
      self.PatientName=StringVar()
      self.DateOfBirth=StringVar()
      self.PatientAddress=StringVar()
      self.Medication=StringVar()



      lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",
                      fg="red",bg="white",font=("times new roman",50,"bold"))
      lbltitle.pack(side=TOP,fill=X)

      # ****************************Dataframe****************************#
      Dataframe=Frame(self.root,bd=20,relief=RIDGE)
      Dataframe.place(x=0,y=130,width=1530,height=350)


      DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                             font=("arial",12,"bold"),text="Patient Information",fg="green")
      DataframeLeft.place(x=0,y=5,width=800,height=290)   


      DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                             font=("times new roman",12,"bold"),text="Patient Info",fg="red")
      DataframeRight.place(x=830,y=5,width=460,height=290)

     #********************* Buttons frame **************************#
      Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
      Buttonframe.place(x=0,y=450,width=1530,height=70)

      #*********************Detail frame***************************#
      Detailframe=Frame(self.root,bd=20,relief=RIDGE)
      Detailframe.place(x=0,y=520,width=1530,height=190)

      #*********************DataframeLeft************************#

      lblNameTablet=Label(DataframeLeft,text="Names of Tablets",font=("arial",8,"bold"),
                             padx=2,pady=6)
      lblNameTablet.grid(row=0,column=0)

      comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("times new roman",8,"bold"),width=35)

      comNametablet["values"]=("None","Nice","Corona Vacaine","Acetaminophen","Adderall","Amlodipine","Ativan")
      comNametablet.current(0)
      comNametablet.grid(row=0,column=1)
      

      lblref=Label(DataframeLeft,font=("arial",8,"bold"),text="Reference No:",padx=2
                                                  ,pady=6)
      lblref.grid(row=1,column=0,sticky=W)
      txtref=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.ref,width=33)
      txtref.grid(row=1,column=1)

      lblDose=Label(DataframeLeft,font=("arial",8,"bold"),text="Dose:",padx=2
                                           ,pady=6)
      lblDose.grid(row=2,column=0,sticky=W)
      txtDose=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.Dose,width=33)
      txtDose.grid(row=2,column=1) 
        


      lblNoOftablets=Label(DataframeLeft,font=("arial",8,"bold"),text="No Of Tablets:",padx=2
                                           ,pady=6)
      lblNoOftablets.grid(row=3,column=0,sticky=W)
      txtNoOftablets=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.NoOfTablets,width=33)
      txtNoOftablets.grid(row=3,column=1) 

      lblLot=Label(DataframeLeft,font=("arial",8,"bold"),text="Lot:",padx=2
                                           ,pady=6)
      lblLot.grid(row=4,column=0,sticky=W)
      txtLot=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.Lot,width=33)
      txtLot.grid(row=4,column=1) 

      lblIssueDate=Label(DataframeLeft,font=("arial",8,"bold"),text="Issue Date:",padx=2
                                           ,pady=6)
      lblIssueDate.grid(row=5,column=0,sticky=W)
      txtIssueDate=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.IssueDate,width=33)
      txtIssueDate.grid(row=5,column=1)


      lblExpDate=Label(DataframeLeft,font=("arial",8,"bold"),text="Exp Date:",padx=2
                                           ,pady=6)
      lblExpDate.grid(row=6,column=0,sticky=W)
      txtExpDate=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.ExpDate,width=33)
      txtExpDate.grid(row=6,column=1)

      lblDailyDose=Label(DataframeLeft,font=("arial",8,"bold"),text="Daily Dose:",padx=2
                                           ,pady=6)
      lblDailyDose.grid(row=7,column=0,sticky=W)
      txtDailyDose=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.DailyDose,width=33)
      txtDailyDose.grid(row=7,column=1)

       
      lblSideEffect=Label(DataframeLeft,font=("arial",8,"bold"),text="Side Effect:",padx=2
                                           ,pady=6)
      lblSideEffect.grid(row=8,column=0,sticky=W)
      txtSideEffect=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.SideEfect,width=33)
      txtSideEffect.grid(row=8,column=1)


      lblFurtherInformation=Label(DataframeLeft,font=("arial",8,"bold"),text="Further Information:",padx=2
                                           ,pady=6)
      lblFurtherInformation.grid(row=0,column=2,sticky=W)
      txtFurtherInformation=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.FurtherInformation,width=33)
      txtFurtherInformation.grid(row=0,column=3)


      lblBloodPressure=Label(DataframeLeft,font=("arial",8,"bold"),text="Blood Pressure:",padx=2
                                           ,pady=6)
      lblBloodPressure.grid(row=1,column=2,sticky=W)
      txtBloodPressure=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.BloodPressure,width=33)
      txtBloodPressure.grid(row=1,column=3)


      lblStorageAdvice=Label(DataframeLeft,font=("arial",8,"bold"),text="Storage Advice:",padx=2
                                           ,pady=6)
      lblStorageAdvice.grid(row=2,column=2,sticky=W)
      txtStorageAdvice=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.StorageAdvice,width=33)
      txtStorageAdvice.grid(row=2,column=3)

      lblMedication=Label(DataframeLeft,font=("arial",8,"bold"),text="Medication:",padx=2
                                           ,pady=6)
      lblMedication.grid(row=3,column=2,sticky=W)
      txtMedication=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.Medication,width=33)
      txtMedication.grid(row=3,column=3)

      lblPatientId=Label(DataframeLeft,font=("arial",8,"bold"),text="Patient Id:",padx=2
                                           ,pady=6)
      lblPatientId.grid(row=4,column=2,sticky=W)
      txtPatientId=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.PatientId,width=33)
      txtPatientId.grid(row=4,column=3)

      lblNHSNumber=Label(DataframeLeft,font=("arial",8,"bold"),text="NHS Number:",padx=2
                                           ,pady=6)
      lblNHSNumber.grid(row=5,column=2,sticky=W)
      txtNHSNumber=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.nhsNumber,width=33)
      txtNHSNumber.grid(row=5,column=3)

      lblPatientName=Label(DataframeLeft,font=("arial",8,"bold"),text="Patient Name:",padx=2
                                           ,pady=6)
      lblPatientName.grid(row=6,column=2,sticky=W)
      txtPatientName=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.PatientName,width=33)
      txtPatientName.grid(row=6,column=3)


      lblDateOfBirth=Label(DataframeLeft,font=("arial",8,"bold"),text="Date Of Birth:",padx=2
                                           ,pady=6)
      lblDateOfBirth.grid(row=7,column=2,sticky=W)
      txtDateOfBirth=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.DateOfBirth,width=33)
      txtDateOfBirth.grid(row=7,column=3)


      lblPatientAddress=Label(DataframeLeft,font=("arial",8,"bold"),text="Patient Address:",padx=2
                                           ,pady=6)
      lblPatientAddress.grid(row=8,column=2,sticky=W)
      txtPatientAddress=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.PatientAddress,width=33)
      txtPatientAddress.grid(row=8,column=3)

        #*************************DataframeRight************************#
      self.txtPrescription=Text(DataframeRight,font=("times new roman",8,"bold"),width=60,height=19,padx=2,pady=6)
      self.txtPrescription.place(x=0,y=0,width=450,height=225)


        #*******************************Buttons************************#

      btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Patient Info",bg="purple",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnPrescription.grid(row=0,column=0)

      btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Record Save",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnPrescriptionData.grid(row=0,column=1)

      btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="violet",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnUpdate.grid(row=0,column=2)

      btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="blue",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnDelete.grid(row=0,column=3)

      btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="red",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnClear.grid(row=0,column=4)


      btnAvailable=Button(Buttonframe,command=self.iAvailable
                     ,text="Doctors Availability",bg="brown",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnAvailable.grid(row=0,column=5)

      btnprint=Button(DataframeRight,text="Print",command=self.print,bg="red",fg="white",font=("arial",12,"bold"),width=15,padx=2,pady=6)
      btnprint.place(x=110,y=228,width=100,height=30)
      #***********************Table************************************#
      #*********************ScrollBar**********************************#
      scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
      self.hospital_table=ttk.Treeview(Detailframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                                         "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      scroll_x.pack  (side = BOTTOM,fill = X)
      scroll_y.pack  (side = RIGHT,fill = Y)

      scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
      scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

      self.hospital_table.heading("nameoftablets",text="Name Of Tablets")
      self.hospital_table.heading("ref",text="Reference No.")
      self.hospital_table.heading("dose",text="Dose")
      self.hospital_table.heading("nooftablets",text="No Of Tablets")
      self.hospital_table.heading("lot",text="Lot")
      self.hospital_table.heading("issuedate",text="Issue Date")
      self.hospital_table.heading("expdate",text="Exp Date")
      self.hospital_table.heading("dailydose",text="Daily Dose")
      self.hospital_table.heading("storage",text="Storage")
      self.hospital_table.heading("nhsnumber",text="NHS Number")
      self.hospital_table.heading("pname",text="Patient Name")
      self.hospital_table.heading("dob",text="DOB")
      self.hospital_table.heading("address",text="Address")

      self.hospital_table["show"]="headings"

      self.hospital_table.column("nameoftablets",width=50)
      self.hospital_table.column("ref",width=50)
      self.hospital_table.column("dose",width=50)
      self.hospital_table.column("nooftablets",width=50)
      self.hospital_table.column("lot",width=50)
      self.hospital_table.column("issuedate",width=50)
      self.hospital_table.column("expdate",width=50)
      self.hospital_table.column("dailydose",width=50)
      self.hospital_table.column("storage",width=50)
      self.hospital_table.column("nhsnumber",width=50)
      self.hospital_table.column("pname",width=50)
      self.hospital_table.column("dob",width=50)
      self.hospital_table.column("address",width=50)

      self.hospital_table.pack(fill=BOTH,expand=1)
      self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
      self.fatch_data()
       
   #**********************Functionality Declaration*******************************#
   def iPrescriptionData(self):
        if self.Nameoftablets.get()=="None" or self.ref.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                     self.Nameoftablets.get(),
                                                                                                     self.ref.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.NoOfTablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.IssueDate.get(),
                                                                                                     self.ExpDate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.SideEfect.get(),
                                                                                                     self.FurtherInformation.get(),
                                                                                                     self.BloodPressure.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.Medication.get(),
                                                                                                     self.PatientId.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get()
                                                                                                                             ))    
            conn.commit()
            conn.close() 
            self.fatch_data()                                                                                           
            messagebox.showinfo("Sucess","Record has been inserted",parent=self.root)

   

   
   def update(self):
       conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
       my_cursor=conn.cursor()
       my_cursor.execute("update hospital set NameOfTablets=%s,Dose=%s, NoOfTablets=%s,Lot=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,SideEffect=%s,FurtherInformation=%s,BloodPressure=%s,StorageAdvice=%s,Medication=%s,PatientId=%s,NHSNumber=%s, PatientName=%s,DateOfBirth=%s, PatientAddress=%s where ReferenceNo=%s",(
                                                                                                                                                                                                                                                                                                        
                                                                                                     self.Nameoftablets.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.NoOfTablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.IssueDate.get(),
                                                                                                     self.ExpDate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.SideEfect.get(),
                                                                                                     self.FurtherInformation.get(),
                                                                                                     self.BloodPressure.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.Medication.get(),
                                                                                                     self.PatientId.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get(),
                                                                                                     self.ref.get() ))
        
       conn.commit()
       conn.close() 
       self.fatch_data()                                                                                            
       messagebox.showinfo("Sucess","Record has been updated",parent=self.root)                                                                                                                                                                                          
       




   def fatch_data(self):
      conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from hospital")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
         self.hospital_table.delete(*self.hospital_table.get_children())
         for i in rows:
            self.hospital_table.insert("",END,values=i)
         conn.commit()
      conn.close()      

   def get_cursor(self,event=""):
      cursor_row=self.hospital_table.focus()
      content=self.hospital_table.item(cursor_row)
      row=content["values"]
      self.Nameoftablets.set(row[0])
      self.ref.set(row[1])
      self.Dose.set(row[2])
      self.NoOfTablets.set(row[3])
      self.Lot.set(row[4])
      self.IssueDate.set(row[5]) 
      self.ExpDate.set(row[6])
      self.DailyDose.set(row[7])
      self.SideEfect.set(row[8])
      self.FurtherInformation.set(row[9])
      self.BloodPressure.set(row[10])
      self.StorageAdvice.set(row[11])
      self.Medication.set(row[12])
      self.PatientId.set(row[13])
      self.nhsNumber.set(row[14])
      self.PatientName.set(row[15])
      self.DateOfBirth.set(row[16])
      self.PatientAddress.set(row[17])


   def iPrescription(self):
      self.txtPrescription.insert(END,"Name of Tablets:\t\t\t "+ self.Nameoftablets.get() + "\n")
      self.txtPrescription.insert(END,"Reference No:\t\t\t " + self.ref.get() + "\n")
      self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
      self.txtPrescription.insert(END,"Number of Tablets:\t\t\t " + self.NoOfTablets.get() + "\n")
      self.txtPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get() + "\n")
      self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
      self.txtPrescription.insert(END,"Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
      self.txtPrescription.insert(END,"Daily Dose:\t\t\t "+ self.DailyDose.get() + "\n")
      self.txtPrescription.insert(END,"Side Effect:\t\t\t " + self.SideEfect.get() + "\n")
      self.txtPrescription.insert(END,"Further Information:\t\t\t " + self.FurtherInformation.get() + "\n")
      self.txtPrescription.insert(END,"StorageAdvice:\t\t\t " + self.StorageAdvice.get() + "\n")
      self.txtPrescription.insert(END,"PatientId:\t\t\t " + self.PatientId.get() + "\n")
      self.txtPrescription.insert(END,"NHS Number:\t\t\t" + self.nhsNumber.get() + "\n")
      self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.PatientName.get() + "\n")
      self.txtPrescription.insert(END,"DateOfBirth:\t\t\t " + self.DateOfBirth.get() + "\n")
      self.txtPrescription.insert(END,"PatientAddress:\t\t\t " + self.PatientAddress.get() + "\n")


   def idelete(self):
      conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
      my_cursor=conn.cursor()
      query="delete from hospital where ReferenceNo=%s"
      value=(self.ref.get(),)
      my_cursor.execute(query,value)
      conn.commit()
      conn.close()
      self.fatch_data()
      messagebox.showinfo("Derlete","Record has been Deleted",parent=self.root)   

   def clear(self):
      self.Nameoftablets.set("")
      self.ref.set("")
      self.Dose.set("")
      self.NoOfTablets.set("")
      self.Lot.set("")
      self.IssueDate.set("") 
      self.ExpDate.set("")
      self.DailyDose.set("")
      self.SideEfect.set("")
      self.FurtherInformation.set("")
      self.BloodPressure.set("")
      self.StorageAdvice.set("")
      self.Medication.set("")
      self.PatientId.set("")
      self.nhsNumber.set("")
      self.PatientName.set("")
      self.DateOfBirth.set("")
      self.PatientAddress.set("")
      self.txtPrescription.delete("1.0",END)

   def iAvailable(self):
        self.new_window3=Toplevel(self.root)
        self.app=Doctors_window(self.new_window3)


   def print(self):
        q=self.txtPrescription.get(1.0,'end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")     
            



class Doctors_window:
   def __init__(self,root):
      self.root=root
      self.root.title("Hospital Management System")
      self.root.geometry("1540x800+0+0")
        
      self.Specialist=StringVar()
      self.NameOfDoctors=StringVar()
      self.PatientId=StringVar()
      self.PatientName=StringVar()
      self.DoctorsId=StringVar()
      self.DoctorsAvailability=StringVar()
      self.Date=StringVar()
      self.Start=StringVar()
      self.End=StringVar()
      self.Patientref=StringVar()
      self.status=StringVar()

      

      

      lbltitle = Label(self.root,bd=20,relief=RIDGE,text="+HOSPITAL MANAGEMENT SYSTEM",
                      fg="red",bg="white",font=("times new roman",50,"bold"))
      lbltitle.pack(side=TOP,fill=X)

      # ****************************Dataframe****************************#
      Dataframe=Frame(self.root,bd=20,relief=RIDGE)
      Dataframe.place(x=0,y=130,width=1530,height=350)


      DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                             font=("arial",12,"bold"),fg="darkviolet",text="Doctors Information & Appointment")
      DataframeLeft.place(x=0,y=5,width=800,height=290)   


      DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                             font=("times new roman",12,"bold"),fg="blue",text="Appointment Info")
      DataframeRight.place(x=830,y=5,width=460,height=290)

     #********************* Buttons frame **************************#
      Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
      Buttonframe.place(x=0,y=450,width=1530,height=70)

      #*********************Detail frame***************************#
      Detailframe=Frame(self.root,bd=20,relief=RIDGE)
      Detailframe.place(x=0,y=520,width=1530,height=190)

      #*********************DataframeLeft************************#

      lblNameTablet=Label(DataframeLeft,text="Doctor Name:",font=("arial",8,"bold"),
                             padx=2,pady=6)
      lblNameTablet.grid(row=0,column=0)

      comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.NameOfDoctors,font=("arial",8,"bold"),width=35,state="readonly")

      comNametablet["values"]=("None","Dr.R.N Sahoo","Dr.Rajalaxmi Mishra","Dr.D.R.Panda","Dr.P.K.Mohanty","Dr.S.R.Behera","Dr.S.S.G.Mishra")
      comNametablet.current(0)
      comNametablet.grid(row=0,column=1)


      lblSpecialist=Label(DataframeLeft,text="Specialization:",font=("arial",8,"bold"),
                             padx=2,pady=6)
      lblSpecialist.grid(row=1,column=0)
      comSpecialist=ttk.Combobox(DataframeLeft,textvariable=self.Specialist,font=("times new roman",8,"bold"),width=35,state="readonly")

      comSpecialist["values"]=("All","Cardiologists","Audiologists","Dentist","Psychiatrists","Radiologist","Oncologis","Neurologist")
      comSpecialist.current(0)
      comSpecialist.grid(row=1,column=1)
      

      lblDoctorid=Label(DataframeLeft,font=("arial",8,"bold"),text="Doctors Id:",padx=2
                                                  ,pady=6)
      lblDoctorid.grid(row=2,column=0,sticky=W)
      txtDoctorid=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.DoctorsId,width=33)
      txtDoctorid.grid(row=2,column=1)

      lblAvailable=Label(DataframeLeft,font=("arial",8,"bold"),text="Doctors Availability:",padx=2
                                           ,pady=6)
      lblAvailable.grid(row=3,column=0,sticky=W)
      txtAvailable=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.DoctorsAvailability,width=33)
      txtAvailable.grid(row=3,column=1) 
        


      lblDate=Label(DataframeLeft,font=("arial",8,"bold"),text="Date:",padx=2
                                           ,pady=6)
      lblDate.grid(row=4,column=0,sticky=W)
      txtDate=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.Date,width=33)
      txtDate.grid(row=4,column=1) 

      lblAppointment=Label(DataframeLeft,font=("arial",8,"bold"),text="Appointment Start Time:",padx=2
                                           ,pady=6)
      lblAppointment.grid(row=5,column=0,sticky=W)
      txtAppointment=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.Start,width=33)
      txtAppointment.grid(row=5,column=1) 

      lblAppointmentEnd=Label(DataframeLeft,font=("arial",8,"bold"),text="Appointment Ending Time:",padx=2
                                           ,pady=6)
      lblAppointmentEnd.grid(row=6,column=0,sticky=W)
      txtAppointmentEnd=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.End,width=33)
      txtAppointmentEnd.grid(row=6,column=1)


      lblPatientId=Label(DataframeLeft,font=("arial",8,"bold"),text="Patient Id:",padx=2
                                           ,pady=6)
      lblPatientId.grid(row=7,column=0,sticky=W)
      txtPatientId=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.PatientId,width=33)
      txtPatientId.grid(row=7,column=1)

      lblPatientref=Label(DataframeLeft,font=("arial",8,"bold"),text="Patient Reference:",padx=2
                                           ,pady=6)
      lblPatientref.grid(row=8,column=0,sticky=W)
      txtPatientref=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.Patientref,width=33)
      txtPatientref.grid(row=8,column=1)

      
      lblPatientName=Label(DataframeLeft,font=("arial",8,"bold"),text="Patient Name:",padx=2
                                           ,pady=6)
      lblPatientName.grid(row=0,column=2,sticky=W)
      txtPatientName=Entry(DataframeLeft,font=("arial",9,"bold"),textvariable=self.PatientName,width=33)
      txtPatientName.grid(row=0,column=3)
      
      

      lblStatus=Label(DataframeLeft,text="Appointment Status:",font=("arial",8,"bold"),
                             padx=2,pady=6)
      lblStatus.grid(row=1,column=2)
      comStatus=ttk.Combobox(DataframeLeft,textvariable=self.status,font=("times new roman",8,"bold"),width=35,state="readonly")
      comStatus["values"]=("Sucess","Failed","Cancel")
      comStatus.current(0)
      comStatus.grid(row=1,column=3)
      #*********************Search frame******************
      Search_frame=LabelFrame(Dataframe,bd=2,relief=RIDGE,text="Search Record",font=("arial",12,"bold"),fg="red")
      Search_frame.place(x=440,y=100,width=350,height=230)
      
      lblsearchby=Label(Search_frame,font=("arial",11,"bold"),text="Search By:",padx=2
                                           ,pady=6,bg="red",fg="white")
      lblsearchby.grid(row=0,column=0,sticky=W,padx=5)
      
      self.com_search=StringVar()
      combo_search_box=ttk.Combobox(Search_frame,font=("arial",8,"bold"),textvariable=self.com_search,width=30,state="readonly")
      combo_search_box["values"]=("Select Option","PatientId","Patientref","DoctorId")
      combo_search_box.current(0)
      combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
      

      self.search=StringVar()
      txtsearch=Entry(Search_frame,font=("arial",9,"bold"),textvariable=self.search,width=30)
      txtsearch.place(x=90,y=45,width=230,height=30)

      btnsearch=Button(Search_frame,text="Search",command=self.search_data,bg="orange",fg="white",font=("arial",12,"bold"),width=15,padx=2,pady=6)
      btnsearch.place(x=90,y=90,width=230,height=30)

      btnsearchall=Button(Search_frame,text="SearchAll",command=self.fetch_data,bg="pink",fg="white",font=("arial",12,"bold"),width=15,padx=2,pady=6)
      btnsearchall.place(x=90,y=150,width=230,height=30)


      btnprint=Button(DataframeRight,text="Print",command=self.print,bg="red",fg="white",font=("arial",12,"bold"),width=15,padx=2,pady=6)
      btnprint.place(x=110,y=215,width=100,height=30)

      #*************************DataframeRight************************#
      self.txtAppointmentinfo=Text(DataframeRight,font=("times new roman",8,"bold"),width=60,height=19,padx=2,pady=6)
      self.txtAppointmentinfo.place(x=0,y=0,width=450,height=200)

      
        #*******************************Buttons************************#

      btnAppointmentinfo=Button(Buttonframe,command=self.iAppointment,text="Appointment Data",bg="blue",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnAppointmentinfo.grid(row=0,column=0)

      btnAppointmentData=Button(Buttonframe,command=self.iAppointmentData,text="Record Save",bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnAppointmentData.grid(row=0,column=1)

      btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="violet",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnUpdate.grid(row=0,column=2)

      btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="orange",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnDelete.grid(row=0,column=3)

      btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="red",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnClear.grid(row=0,column=4)


      btnPayment=Button(Buttonframe,
                     text="Payment",command=self.ipay,bg="purple",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
      btnPayment.grid(row=0,column=5)


      #***********************Table************************************#
      #*********************ScrollBar**********************************#
      scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
      self.doctor_table=ttk.Treeview(Detailframe,column=("Doctor Name","Specialization","Doctors Id","Doctors Availability","Date","Start Time","End Time","Patient Id","Patient Referenceno","Patient Name","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      scroll_x.pack  (side = BOTTOM,fill = X)
      scroll_y.pack  (side = RIGHT,fill = Y)

      scroll_x=ttk.Scrollbar(command=self.doctor_table.xview)
      scroll_y=ttk.Scrollbar(command=self.doctor_table.yview)

      self.doctor_table.heading("Doctor Name",text="Doctor Name")
      self.doctor_table.heading("Specialization",text="Specialization")
      self.doctor_table.heading("Doctors Id",text="Doctors Id")
      self.doctor_table.heading("Doctors Availability",text="Doctors Availability")
      self.doctor_table.heading("Date",text="Date")
      self.doctor_table.heading("Start Time",text="Start Time")
      self.doctor_table.heading("End Time",text="End Time")
      self.doctor_table.heading("Patient Id",text="Patient Id")
      self.doctor_table.heading("Patient Referenceno",text="Patient refno")
      self.doctor_table.heading("Patient Name",text="Patient Name")
      self.doctor_table.heading("Status",text="Status")

      self.doctor_table["show"]="headings"

      self.doctor_table.column("Doctor Name",width=50)
      self.doctor_table.column("Specialization",width=50)
      self.doctor_table.column("Doctors Id",width=50)
      self.doctor_table.column("Doctors Availability",width=50)
      self.doctor_table.column("Date",width=50)
      self.doctor_table.column("Start Time",width=50)
      self.doctor_table.column("End Time",width=50)
      self.doctor_table.column("Patient Id",width=50)
      self.doctor_table.column("Patient Referenceno",width=50)
      self.doctor_table.column("Patient Name",width=50)
      self.doctor_table.column("Status",width=50)

      self.doctor_table.pack(fill=BOTH,expand=1)
      self.doctor_table.bind("<ButtonRelease-1>",self.get_cursor)
      self.fetch_data()
       
   #**********************Functionality Declaration*******************************#
   def iAppointmentData(self):
        if self.NameOfDoctors.get()=="None" or self.PatientId.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.NameOfDoctors.get(),
                                                                                           self.Specialist.get(),
                                                                                           self.DoctorsId.get(),
                                                                                           self.DoctorsAvailability.get(),
                                                                                           self.Date.get(),
                                                                                           self.Start.get(),
                                                                                           self.End.get(),
                                                                                           self.PatientId.get(),
                                                                                           self.Patientref.get(),
                                                                                           self.PatientName.get(),
                                                                                           self.status.get()))    
            conn.commit()
            conn.close() 
            self.fetch_data()                                                                                           
            messagebox.showinfo("Sucess","Record has been inserted",parent=self.root)

   

   
   def update(self):
       conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
       my_cursor=conn.cursor()
       my_cursor.execute("update doctor set NameofDoctor=%s,Specialization=%s, DoctorId=%s,DoctorsAvailability=%s,Date=%s,StartTime=%s,EndTime=%s,Patientref=%s,PatientName=%s,status=%s where PatientId=%s",(
                                                                                           self.NameOfDoctors.get(),
                                                                                           self.Specialist.get(),
                                                                                           self.DoctorsId.get(),
                                                                                           self.DoctorsAvailability.get(),
                                                                                           self.Date.get(),
                                                                                           self.Start.get(),
                                                                                           self.End.get(),
                                                                                           self.Patientref.get(),
                                                                                           self.PatientName.get(),
                                                                                           self.status.get(),
                                                                                           self.PatientId.get()
                                                                                           ))
        
       conn.commit()
       conn.close() 
       self.fetch_data()                                                                                            
       messagebox.showinfo("Sucess","Record has been updated",parent=self.root)                                                                                                                                                                                          
       




   def fetch_data(self):
      try:
         conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from doctor")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
             self.doctor_table.insert("",END,values=i)
            conn.commit()
         conn.close()
      except Exception as es:
            messagebox.showerror("Error",f'Due To{str(es)}')                 
         

   def get_cursor(self,event=""):
      cursor_row=self.doctor_table.focus()
      content=self.doctor_table.item(cursor_row)
      row=content["values"]
      self.NameOfDoctors.set(row[0])
      self.Specialist.set(row[1])
      self.DoctorsId.set(row[2])
      self.DoctorsAvailability.set(row[3])
      self.Date.set(row[4])
      self.Start.set(row[5]) 
      self.End.set(row[6])
      self.PatientId.set(row[7])
      self.Patientref.set(row[8])
      self.PatientName.set(row[9])
      self.status.set(row[10])
      


   def iAppointment(self):
      self.txtAppointmentinfo.insert(END,"Doctor Name:\t\t\t "+ self.NameOfDoctors.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Specialization:\t\t\t " + self.Specialist.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Doctors Id:\t\t\t" + self.DoctorsId.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Doctors Availability:\t\t\t " + self.DoctorsAvailability.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Date:\t\t\t" + self.Date.get() + "\n")
      self.txtAppointmentinfo.insert(END,"StartTime:\t\t\t" + self.Start.get() + "\n")
      self.txtAppointmentinfo.insert(END,"EndTime:\t\t\t" + self.End.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Patient Id:\t\t\t "+ self.PatientId.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Patient refno:\t\t\t " + self.Patientref.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Patient Name:\t\t\t " + self.PatientName.get() + "\n")
      self.txtAppointmentinfo.insert(END,"Appointment Status:\t\t\t " + self.status.get() + "\n")      


   def idelete(self):
      conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
      my_cursor=conn.cursor()
      query="delete from doctor where PatientId=%s"
      value=(self.PatientId.get(),)
      my_cursor.execute(query,value)
      conn.commit()
      conn.close()
      self.fetch_data()
      messagebox.showinfo("Delete","Record has been Deleted",parent=self.root)   

   def clear(self):
      self.NameOfDoctors.set("")
      self.Specialist.set("")
      self.DoctorsId.set("")
      self.DoctorsAvailability.set("")
      self.Date.set("")
      self.Start.set("") 
      self.End.set("")
      self.PatientId.set("")
      self.Patientref.set("")
      self.PatientName.set("")
      self.status.set("")
      self.txtAppointmentinfo.delete("1.0",END)

   def ipay(self):
      self.new_window4=Toplevel(self.root)
      self.app=Payment_Window(self.new_window4)


   def search_data(self):
      if self.com_search.get()=="Select Option":
         messagebox.showerror("Error","Please select",parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            my_cursor=conn.cursor() 
            my_cursor.execute('select * from doctor where ' +str(self.com_search.get())+" LIKE'%"+str(self.search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
               self.doctor_table.delete(*self.doctor_table.get_children())
               for i in rows:
                  self.doctor_table.insert("",END,values=i)
            conn.commit()
            conn.close()
                
         except Exception as es:
            messagebox.showerror("Error",f'Due To{str(es)}')                                                                                                                                                                                         
       
   
   def print(self):
        q=self.txtAppointmentinfo.get(1.0,'end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")

class Payment_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Payment")
        self.root.geometry("1600x900+0+0")


        #***********Text Variable*************
        self.var_fname=StringVar()
        self.var_contact=StringVar()
        self.var_Paymentstatus=StringVar()
        self.var_id=StringVar()
        self.var_Fee=StringVar()
        self.var_Tranid=StringVar()
        self.var_Date=StringVar()
        
        
       #***********Background Image************
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\blue_background_with_blue_background_text.jfif")
        bg_lbl2=Label(self.root,image=self.bg)
        bg_lbl2.place(x=0,y=0,relwidth=1,relheight=3)

        #*************Left Side Image*************
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\slipu\OneDrive\Desktop\HMS\Images\asian-young-woman-smile-with-paying-credit-card-with-payment-terminal-with-salesman_49071-2635.jfif")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=0,y=80,width=550,height=350)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=80,width=400,height=550)

        payment_lbl=Label(frame,text="Payment Section",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        payment_lbl.place(x=20,y=20)

        DataframeRight=LabelFrame(self.root,bd=10,relief=RIDGE,padx=20,
                             font=("times new roman",12,"bold"),fg="blue",text="Payment Info")
        DataframeRight.place(x=830,y=80,width=600,height=550)


        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=500,width=520,height=190)

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=420,width=520,height=80)

        #****************Label and entry ******************

        #*****row1*************
        fname=Label(frame,text="Patient Full Name",font=("times new roman",12,"bold"),bg="white",fg="black")
        fname.place(x=50,y=70)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",12))
        self.fname_entry.place(x=50,y=100,width=250)

        
        #*********row2*************
        txtcontact=Label(frame,text="Contact No",font=("times new roman",12,"bold"),bg="white",fg="black")
        txtcontact.place(x=50,y=130)

        self.contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",12))
        self.contact.place(x=50,y=160,width=250)
        

        #**********row3**************
        
        txtPatientId=Label(frame,text="Patient_Id",font=("times new roman",12,"bold"),fg="black",bg="white")
        txtPatientId.place(x=50,y=190)

        self.Patientid=ttk.Entry(frame,textvariable=self.var_id,font=("times new roman",12))
        self.Patientid.place(x=50,y=220,width=250)
        

        lblsearchby=Label(Buttonframe,font=("arial",11,"bold"),text="Search By:",padx=2
                                           ,pady=6,bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=5)


        self.com_search=StringVar()
        combo_search_box=ttk.Combobox(Buttonframe,font=("arial",8,"bold"),textvariable=self.com_search,width=30,state="readonly")
        combo_search_box["values"]=("Select Option","PatientId","Transaction Id")
        combo_search_box.current(0)
        combo_search_box.place(x=100,y=3,width=140,height=30)

        self.search=StringVar()
        txtsearch=Entry(Buttonframe,font=("arial",9,"bold"),textvariable=self.search,width=30)
        txtsearch.place(x=245,y=3,width=120,height=30)

        btnsearch=Button(Buttonframe,text="Search",command=self.search_data,bg="orange",fg="white",font=("arial",12,"bold"),width=15,padx=2,pady=6)
        btnsearch.place(x=370,y=3,width=70,height=30)
        #**************row4*******
        
        txtFee=Label(frame,text="Appointment Fee",font=("times new roman",12,"bold"),fg="black",bg="white")
        txtFee.place(x=50,y=250)

        self.Fee=ttk.Entry(frame,textvariable=self.var_Fee,font=("times new roman",12))
        self.Fee.place(x=50,y=280,width=250)

        Trans_id=Label(frame,text="Transaction Id",font=("times new roman",12,"bold"),bg="white",fg="black")
        Trans_id.place(x=50,y=310)

        self.Trans_id=ttk.Entry(frame,textvariable=self.var_Tranid,font=("times new roman",12))
        self.Trans_id.place(x=50,y=340,width=250)

        Date=Label(frame,text="Date & Time",font=("times new roman",12,"bold"),bg="white",fg="black")
        Date.place(x=50,y=370)

        self.Date=ttk.Entry(frame,textvariable=self.var_Date,font=("times new roman",12))
        self.Date.place(x=50,y=400,width=250)
          
        payment_status=Label(frame,text="Payment Status",font=("times new roman",12,"bold"),fg="black",bg="white")
        payment_status.place(x=50,y=430)

        self.combo_payment_status=ttk.Combobox(frame,textvariable=self.var_Paymentstatus,font=("times new roman",10,"bold"),state="readonly")
        self.combo_payment_status["values"]=("None","Sucess","Failed","Cancel")
        self.combo_payment_status.place(x=50,y=460,width=250)
        self.combo_payment_status.current(0)

        self.txtPayment_info=Text(DataframeRight,font=("times new roman",8,"bold"),width=60,height=30,padx=2,pady=6)
        self.txtPayment_info.place(x=0,y=0)

        #*******Buttons**************

        btnSave=Button(frame,text="Save",command=self.Save_data,bg="green",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
        btnSave.place(x=70,y=495,width=100,height=30)
        
        btnprint3=Button(DataframeRight,text="Print",command=self.print,bg="red",fg="white",font=("arial",12,"bold"),width=20,padx=2,pady=6)
        btnprint3.place(x=90,y=420,width=100,height=30)
    

        #********************Table*************************
        #***********************ScrollBar******************
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.payment_table=ttk.Treeview(Detailframe,column=("Full_Name","Contactno","Patientid","Fee","Tranid","Date","paystatus"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack  (side = BOTTOM,fill = X)
        scroll_y.pack  (side = RIGHT,fill = Y)

        scroll_x=ttk.Scrollbar(command=self.payment_table.xview)
        scroll_y=ttk.Scrollbar(command=self.payment_table.yview)

        self.payment_table.heading("Full_Name",text="Full Name")
        self.payment_table.heading("Contactno",text="Contact No")
        self.payment_table.heading("Patientid",text="Patient Id")
        self.payment_table.heading("Fee",text="Appointment Fee")
        self.payment_table.heading("Tranid",text="Transaction Id")
        self.payment_table.heading("Date",text="Date & Time")
        self.payment_table.heading("paystatus",text="Payment Status")

        self.payment_table["show"]="headings"

        self.payment_table.column("Full_Name",width=50)
        self.payment_table.column("Contactno",width=50)
        self.payment_table.column("Patientid",width=50)
        self.payment_table.column("Fee",width=50)
        self.payment_table.column("Tranid",width=50)
        self.payment_table.column("Date",width=50)
        self.payment_table.column("paystatus",width=50)

        self.payment_table.pack(fill=BOTH,expand=1)
        self.payment_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
        
        
    def Save_data(self):
        if self.var_Paymentstatus.get()=="None" or self.Patientid.get()=="" or self.var_contact.get()=="" or self.var_Fee.get()=="" or self.var_id=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into payment values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_fname.get(),
                                                                            self.var_contact.get(),
                                                                            self.var_id.get(),
                                                                            self.var_Fee.get(),
                                                                            self.var_Tranid.get(),
                                                                            self.var_Date.get(),
                                                                            self.var_Paymentstatus.get()))    
            
            conn.commit()
            conn.close() 
            self.fatch_data()                                                                                         
            messagebox.showinfo("Save","Record has been inserted",parent=self.root)
            self.txtPayment_info.insert(END,"Patient Full Name:\t\t\t "+ self.var_fname.get() + "\n")
            self.txtPayment_info.insert(END,"Contact No:\t\t\t " + self.var_contact.get() + "\n")
            self.txtPayment_info.insert(END,"Patient Id:\t\t\t" + self.var_id.get() + "\n")
            self.txtPayment_info.insert(END,"Appointment Fee:\t\t\t " + self.var_Fee.get() + "\n")
            self.txtPayment_info.insert(END,"Transaction Id:\t\t\t " + self.var_Tranid.get() + "\n")
            self.txtPayment_info.insert(END,"Date & Time:\t\t\t " + self.var_Date.get() + "\n")
            self.txtPayment_info.insert(END,"Payment Status:\t\t\t" + self.var_Paymentstatus.get() + "\n")


    def fatch_data(self):
      conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from payment")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
         self.payment_table.delete(*self.payment_table.get_children())
         for i in rows:
            self.payment_table.insert("",END,values=i)
         conn.commit()
      conn.close()      

    def get_cursor(self,event=""):
      cursor_row=self.payment_table.focus()
      content=self.payment_table.item(cursor_row)
      row=content["values"]
      self.var_fname.set(row[0])
      self.var_contact.set(row[1])
      self.var_id.set(row[2])
      self.var_Fee.set(row[3])
      self.var_Tranid.set(row[4])
      self.var_Date.set(row[5]) 
      self.var_Paymentstatus.set(row[6])
    
    
    def print(self):
        q=self.txtPayment_info.get(1.0,'end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"Print")

    def search_data(self):
      if self.com_search.get()=="Select Option":
         messagebox.showerror("Error","Please select",parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",username="Rama",password="Rama@1234",database="patientdetails")
            my_cursor=conn.cursor() 
            my_cursor.execute('select * from payment where ' +str(self.com_search.get())+" LIKE'%"+str(self.search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
               self.payment_table.delete(*self.payment_table.get_children())
               for i in rows:
                  self.payment_table.insert("",END,values=i)
            conn.commit()
            conn.close()
         except Exception as es:
            messagebox.showerror("Error",f'Due To{str(es)}')    


if __name__ == "__main__": 
    main()