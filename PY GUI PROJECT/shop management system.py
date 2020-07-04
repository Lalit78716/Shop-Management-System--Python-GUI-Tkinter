from tkinter import *
import math,random
from tkinter import messagebox
import os
import smtplib
from PIL import Image,ImageTk
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen

class Bill_App:
    def __init__(self, master):
        self.master=master
        self.master.geometry("1920x1080+-10+0")
        self.master.title("CRP shp management system")

        title=Label(self.master,text="SHOP MANAGEMENT",bd=12,relief=GROOVE,bg="orange red",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #    variable ---------------------------------------
        
        #   cosmatic variable
        self.soap=IntVar()
        self.facecream=IntVar()
        self.facewash=IntVar()
        self.hair_spry=IntVar()
        self.hair_gel=IntVar()
        self.body_lotion=IntVar()
        
        # grocery varible
        self.maggie=IntVar()
        self.rice=IntVar()
        self.wheat=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.sugar=IntVar()
        
        # cold drink
        self.maza=IntVar()
        self.coca_cola=IntVar()
        self.thumbs_up=IntVar()
        self.slice=IntVar()
        self.frooti=IntVar()
        self.pepsi=IntVar()
        
        # biscuit varible 
        
        self.parle=IntVar()
        self.britania=IntVar()
        self.goodday=IntVar()
        self.oreo=IntVar()
        self.sunfist=IntVar()
        self.monaco=IntVar()
        
        #product price varible
        
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        self.biscuit_price=StringVar()
        
        # tax varible
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        self.biscuit_tax=StringVar()
        
        #customer details
        
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.c_mail=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        # admin
        self.admin_id=StringVar()
        self.admin_pass=StringVar()
        
        
        
        # ------------>>> CUSTOMER DETAILS <<<<<-----------------
        F0=LabelFrame(self.master,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F0.place(x=0,y=70,width=950)
        
        cname_label=Label(F0,text="Customer Name",bg="tomato",font=("times new romen",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F0,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_label=Label(F0,text="Phone No.",bg="tomato",font=("times new romen",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F0,width=20,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
         ################################ send email button
        F1=LabelFrame(self.master,bd=10,relief=GROOVE,text="send bill via Email ",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F1.place(x=950,y=70,width=587)
        
        cmail_label=Label(F1,text="Email",bg="tomato",font=("times new romen",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cmail_txt=Entry(F1,width=20,textvariable=self.c_mail,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        #bn_txt=Entry(F9,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        send_btn=Button(F1,text="Send",command=self.check_mail,bg="cyan",bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=7)

        
        #----------------->>>>> COsmetic frame <<<----------------
        F2=LabelFrame(self.master,bd=10,relief=GROOVE,text="Cosmetic",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F2.place(x=5,y=152,width=277,height=393)
        
        
        bath_txt=Entry(F2,width=2,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        bath_label=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        #face cream
        facecream_label=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        facecream_txt=Entry(F2,width=2,textvariable=self.facecream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #Facewash
        facewash_label=Label(F2,text="Facewash",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        facewash_txt=Entry(F2,width=2,textvariable=self.facewash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #hair spray
        hair_Spry_label=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_spry_txt=Entry(F2,width=2,textvariable=self.hair_spry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        #Hair gel
        hair_gel_label=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=2,textvariable=self.hair_gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        #bodylotion
        body_lt_label=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lt_txt=Entry(F2,width=2,textvariable=self.body_lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        
        # you can use scroll bar here for frame
        
        #bath_shampoo_label=Label(F2,text="Bath Shampoo",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        #bath_shampoo_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        
        #bath_shampoo_label=Label(F2,text="hair oil",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        #bath_shampoo_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
        
         #----------------->>>>> Groccery frame <<<----------------
        F3=LabelFrame(self.master,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F3.place(x=276,y=152,width=220,height=393)
        
        g1_label=Label(F3,text="Meggie",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=4,textvariable=self.maggie,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        g2_label=Label(F3,text="Rice",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=4,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        g3_label=Label(F3,text="Wheat",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=4,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
            
        g4_label=Label(F3,text="Food oil",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=4,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        g5_label=Label(F3,text="Daal",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=4,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        g6_label=Label(F3,text="Sugar",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=4,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
         
         #----------------->>>>> cold-drink frame <<<----------------
        F4=LabelFrame(self.master,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F4.place(x=490,y=152,width=220,height=393)
        
        c1_label=Label(F4,text="Maza",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=4,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F4,text="Coca cola",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=4,textvariable=self.coca_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F4,text="Thumbs-up",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=4,textvariable=self.thumbs_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F4,text="Slice",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=4,textvariable=self.slice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F4,text="Frooti",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=4,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=4,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        #----------------->>>>> Biscuit frame <<<----------------
        F4=LabelFrame(self.master,bd=10,relief=GROOVE,text="Biscuits",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F4.place(x=705,y=152,width=230,height=393)
        
        c1_label=Label(F4,text="Parle-G",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=4,textvariable=self.parle,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F4,text="Britania",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=4,textvariable=self.britania,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F4,text="Oreo",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=4,textvariable=self.oreo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F4,text="Good Day",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=4,textvariable=self.goodday,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F4,text="Sunfist",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=4,textvariable=self.sunfist,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F4,text="Monaco",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=4,textvariable=self.monaco,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)
        
        
         #----------------->>>>> image frame <<<----------------
         
        
        
        self.image_section()
        
        
        # bill Area ....................................
        
        F6=LabelFrame(self.master,bd=10,relief=GROOVE)
        F6.place(x=1160,y=152,width=380,height=393)
        bill_title=Label(F6,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #  bottom button frame----------------------------------
        
        F7=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F7.place(x=0,y=540,relwidth=1,height=180)
        
        m1=Label(F7,text="Total Cosmetic Price",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky=W)
        ml_txt=Entry(F7,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F7,text="Total Grocery Price",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky=W)
        m2_txt=Entry(F7,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F7,text="Total Cold-drink Price",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky=W)
        m3_txt=Entry(F7,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m4=Label(F7,text="Total Biscuit Price",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky=W)
        m4_txt=Entry(F7,width=18,textvariable=self.biscuit_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)

        # for tax
        
        tax1=Label(F7,text="Cosmetic Tax (28%)",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky=W)
        taxl_txt=Entry(F7,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        tax2=Label(F7,text="Grocery Tax (5%)",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky=W)
        tax2_txt=Entry(F7,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        tax3=Label(F7,text="Cold-drink Tax (40%)",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky=W)
        tax3_txt=Entry(F7,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        tax4=Label(F7,text="Biscuit Tax (5%)",bg="tomato",fg="black",font=("times new roman",14,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky=W)
        tax4_txt=Entry(F7,width=18,textvariable=self.biscuit_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=1)


        btn_frame=Frame(F7,bd=7,relief=GROOVE)
        btn_frame.place(x=810,y=10,width=700,height=115)
        
        total_btn=Button(btn_frame,command=self.total,text="Total",bg="cyan",bd=5,fg="black",pady=15,width=14,font="arial 12 bold").grid(row=0,column=0,padx=15,pady=15)

        genbill_btn=Button(btn_frame,text="Generate Bill",command=self.bill_area,bg="cyan",bd=5,fg="black",pady=15,width=14,font="arial 12 bold").grid(row=0,column=1,padx=15,pady=15)

        clear_btn=Button(btn_frame,text="Clear",command=self.clear_data,bg="cyan",bd=5,fg="black",pady=15,width=11,font="arial 12 bold").grid(row=0,column=2,padx=15,pady=15)

        exit_btn=Button(btn_frame,text="Exit",command=self.exit_app,bg="cyan",bd=5,fg="black",pady=15,width=11,font="arial 12 bold").grid(row=0,column=3,padx=15,pady=15)
        
        self.welcome_bill()
        #----------------->>>>> bill search frame <<<----------------
        F8=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Search ",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F8.place(x=0,y=712,width=350,height=80)
        
        bn_txt=Entry(F8,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        search_btn=Button(F8,text="Search",command=self.find_bill,bg="cyan",bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=2)

           #---------------Admin area-----------------------
        F9=LabelFrame(self.master,bd=10,relief=GROOVE,text="Admin area ",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F9.place(x=351,y=712,width=1186,height=80)
            
        
        
        Label(F9,text="Login :  | ",font=("times new roman",15,"bold"),fg="black",bg="tomato").grid(row=0,column=0)
        Label(F9,text="ID ",font=("times new roman",15,"bold"),fg="black",bg="tomato").grid(row=0,column=1)
        
        admin_id1=Entry(F9,width=25,textvariable=self.admin_id,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=2,sticky=E)
        
        Label(F9,text="  Password",font=("times new roman",15,"bold"),fg="black",bg="tomato").grid(row=0,column=3)
        
        admin_pass1=Entry(F9,width=18,textvariable=self.admin_pass,font="arial 10 bold",bd=7,relief=SUNKEN,show='X').grid(row=0,column=4,sticky=E)
        
        a_login=Button(F9,text="Login",command=self.login_page,bg="cyan",bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=5,padx=35)
        
        
        #-------sign up----------------
        Label(F9,text="  Create New Account",font=("times new roman",15,"bold"),fg="black",bg="tomato").grid(row=0,column=6)
        a_sign_up=Button(F9,text="Sign Up",bg="cyan",bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=7,padx=35)
        
        
    
    
    
    

    def image_section(self):
        img=Image.open("shoping3.jpg")
        pic=ImageTk.PhotoImage(img)
        F5=LabelFrame(self.master,bd=10,relief=GROOVE,bg="tomato")
        F5.place(x=930,y=152,width=230,height=393)
        
        F5_label=Label(F5,image=pic)
        F5_label.image=pic
        F5_label.pack()
    
    def total(self):
        self.c_sp=self.soap.get()*25
        self.c_fc=self.facecream.get()*132#*self.find_price("Face cream",self.fcream_clicked.get())
        self.c_fw=self.facewash.get()*122#*self.find_price("Face wash",self.fwash_clicked.get())
        self.c_hsp=self.hair_spry.get()*154#*self.find_price("Hair Spray",self.hairspray_clicked.get())
        self.c_hg=self.hair_gel.get()*45#*self.find_price("Hair gel",self.hairgel_clicked.get())
        self.c_bl=self.body_lotion.get()*78#*self.find_price("Bodylotion",self.bodylotion_clicked.get())
        self.total_cosmetic_price=float(
                self.c_sp+
                self.c_bl+
                self.c_fc+
                self.c_fw+
                self.c_hg+
                self.c_hsp
                )
        
        self.c_tax=round((self.total_cosmetic_price*0.28),2)
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        
        
        
        self.g_mg=self.maggie.get()*30
        self.g_rc=self.rice.get()*70
        self.g_wh=self.wheat.get()*150
        self.g_sg=self.sugar.get()*200
        self.g_fol=self.food_oil.get()*100
        self.g_dl=self.daal.get()*140
        
        self.total_grocery_price=float(
                self.g_dl+
                self.g_fol+
                self.g_mg+
                self.g_rc+
                self.g_sg+
                self.g_wh
                )
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        
        self.cd_mz=self.maza.get()*30
        self.cd_cc=self.coca_cola.get()*70
        self.cd_sl=self.slice.get()*150
        self.ccd_thu=self.thumbs_up.get()*200
        self.cd_ft=self.frooti.get()*100
        self.cd_ps=self.pepsi.get()*140
        
        self.total_cold_drink_price=float(
                self.cd_cc+
                self.cd_ft+
                self.cd_mz+
                self.cd_ps+
                self.cd_sl+
                self.ccd_thu
                )
        self.cd_tax=round((self.total_cold_drink_price*0.40),2)
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
         
        self.bc_pr=self.parle.get()*30
        self.bc_o=self.oreo.get()*70
        self.bc_mc=self.monaco.get()*150
        self.bc_bt=self.britania.get()*200
        self.bc_gd=self.goodday.get()*100
        self.bc_sf=self.sunfist.get()*140
        
        self.total_biscuit_price=float(
                self.bc_bt+
                self.bc_gd+
                self.bc_mc+
                self.bc_o+
                self.bc_pr+
                self.bc_sf
                )
        self.bc_tax=round((self.total_biscuit_price*0.05),2)
        self.biscuit_price.set("Rs. "+str(self.total_biscuit_price))
        self.biscuit_tax.set("Rs. "+str(self.bc_tax))
        
        self.total_bill=float(
                self.total_cosmetic_price+
                self.total_grocery_price+
                self.total_cold_drink_price+
                self.total_biscuit_price+
                self.c_tax+
                self.g_tax+
                self.cd_tax+
                self.bc_tax
                )
        
    def stock_update_after_purchased(self,name,n):
        f1=open("stock.csv","w+",encoding='utf-8-sig')
        for i in f1:
            data=i.split(",")
            if data[0]==name:
                if n<=int(data[1]):
                    x=int(data[1])
                    x=x-n
                    return n
        
        
        
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t|| CRP SHOP ||")
        self.txtarea.insert(END,"\n_________________________________________\n")
        self.txtarea.insert(END,f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name :   {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone no.:    {self.c_phon.get()}")
        self.txtarea.insert(END,"\n==========================================")
        self.txtarea.insert(END,"\nProducts\t\t\tQTY\t   Price")
        self.txtarea.insert(END,"\n==========================================")
        
        
    def bill_area(self):
       
       if self.c_name.get()=="" or self.c_phon.get()=="":
           messagebox.showerror("Error","Fill Customer details")
       elif self.cosmetic_price=="Rs. 0.0" and self.grocery_price=="Rs. 0.0" and self.cold_drink_price=="Rs. 0.0" and self.biscuit_price=="Rs. 0.0":
           messagebox.showerror("Error","No product purchased")
       else: 
           self.welcome_bill()
           # cosmetic
           if self.soap.get()!=0:
               self.txtarea.insert(END,f"\nSoap    \t\t\t{self.soap.get()}\t    {self.c_sp}")
           if self.facewash.get()!=0:
               self.txtarea.insert(END,f"\nFacewash \t\t\t{self.facewash.get()}\t    {self.c_fw}")
           if self.facecream.get()!=0:
               self.txtarea.insert(END,f"\nFacecream\t\t\t{self.facecream.get()}\t    {self.c_fc}")
           if self.hair_spry.get()!=0:
               self.txtarea.insert(END,f"\nHairSpray\t\t\t{self.hair_spry.get()}\t    {self.c_hsp}")
           if self.hair_gel.get()!=0:
               self.txtarea.insert(END,f"\nHair Gel \t\t\t{self.hair_gel.get()}\t    {self.c_hg}")
           if self.body_lotion.get()!=0:
               self.txtarea.insert(END,f"\nBody Lotion\t\t\t{self.body_lotion.get()}\t    {self.c_bl}")
            
            #Grocery print
           if self.maggie.get()!=0:
               self.txtarea.insert(END,f"\nMaggie   \t\t\t{self.maggie.get()}\t    {self.g_mg}")
           if self.rice.get()!=0:
               self.txtarea.insert(END,f"\nRice     \t\t\t{self.rice.get()}\t    {self.g_rc}")
           if self.wheat.get()!=0:
               self.txtarea.insert(END,f"\nWheat    \t\t\t{self.wheat.get()}\t    {self.g_wh}")
           if self.food_oil.get()!=0:
               self.txtarea.insert(END,f"\nFood oil \t\t\t{self.food_oil.get()}\t    {self.g_fol}")
           if self.sugar.get()!=0:
               self.txtarea.insert(END,f"\nSugar    \t\t\t{self.sugar.get()}\t    {self.g_sg}")
           if self.daal.get()!=0:
               self.txtarea.insert(END,f"\nDaal     \t\t\t{self.daal.get()}\t    {self.g_dl}")
    
            
            #Biscuit print
           if self.parle.get()!=0:
               self.txtarea.insert(END,f"\nParle-G  \t\t\t{self.parle.get()}\t    {self.bc_pr}")
           if self.oreo.get()!=0:
               self.txtarea.insert(END,f"\nOreo     \t\t\t{self.oreo.get()}\t    {self.bc_o}")
           if self.britania.get()!=0:
               self.txtarea.insert(END,f"\nBritania \t\t\t{self.britania.get()}\t    {self.bc_bt}")
           if self.goodday.get()!=0:
               self.txtarea.insert(END,f"\nGood-Day \t\t\t{self.goodday.get()}\t    {self.bc_gd}")
           if self.sunfist.get()!=0:
               self.txtarea.insert(END,f"\nSunfist  \t\t\t{self.sunfist.get()}\t    {self.bc_sf}")
           if self.monaco.get()!=0:
               self.txtarea.insert(END,f"\nMonaco   \t\t\t{self.monaco.get()}\t    {self.bc_mc}")
            
            
            #Cold-drink print
           if self.maza.get()!=0:
               self.txtarea.insert(END,f"\nMaza     \t\t\t{self.maza.get()}\t    {self.cd_mz}")
           if self.coca_cola.get()!=0:
               self.txtarea.insert(END,f"\nCoca-Cola\t\t\t{self.coca_cola.get()}\t    {self.cd_cc}")
           if self.slice.get()!=0:
               self.txtarea.insert(END,f"\nSlice    \t\t\t{self.slice.get()}\t    {self.cd_sl}")
           if self.thumbs_up.get()!=0:
               self.txtarea.insert(END,f"\nThumbs-up\t\t\t{self.thumbs_up.get()}\t    {self.ccd_thu}")
           if self.pepsi.get()!=0:
               self.txtarea.insert(END,f"\nPepsi    \t\t\t{self.pepsi.get()}\t    {self.cd_ps}")
           if self.frooti.get()!=0:
               self.txtarea.insert(END,f"\nFrooti   \t\t\t{self.frooti.get()}\t    {self.cd_ft}")
            
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           if self.cosmetic_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t       {self.cosmetic_tax.get()}")
           if self.grocery_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nGrocery  Tax\t\t\t       {self.grocery_tax.get()}")
           if self.biscuit_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nBiscuit  Tax\t\t\t       {self.biscuit_tax.get()}")
           if self.cold_drink_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nColdDrink Tax\t\t\t      {self.cold_drink_tax.get()}")
           
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           self.txtarea.insert(END,f"\nTotal Bill :\t\t\t      Rs. {str(self.total_bill)}") 
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           
           self.save_bill()
       
    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
            fp1.write(self.bill_data)
            fp1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved successfuly")
        else:
            return 
    
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,f1.read())
                f1.close()
                present="yes"
                
                
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

        
    def clear_data(self):
        #   cosmatic variable
        op=messagebox.askyesno("Exit","Do you want to Exit")
        if op>0:
            self.soap.set(0)
            self.facecream.set(0)
            self.facewash.set(0)
            self.hair_spry.set(0)
            self.hair_gel.set(0)
            self.body_lotion.set(0)
            
            # grocery varible
            self.maggie.set(0)
            self.rice.set(0)
            self.wheat.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            
            # cold drink
            self.maza.set(0)
            self.coca_cola.set(0)
            self.thumbs_up.set(0)
            self.slice.set(0)
            self.frooti.set(0)
            self.pepsi.set(0)
            
            # biscuit varible 
            
            self.parle.set(0)
            self.britania.set(0)
            self.goodday.set(0)
            self.oreo.set(0)
            self.sunfist.set(0)
            self.monaco.set(0)
            
            #product price varible
            
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.biscuit_price.set("")
            
            # tax varible
            
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            self.biscuit_tax.set("")
            
            #customer details
            
            self.c_name.set("")
            self.c_phon.set("")
            self.c_mail.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.welcome_bill()
    
        else:
            return
                
        
    def exit_app(self):
        op1=messagebox.askyesno("Exit","Do you want to Exit")
        if op1>0:
            root.destroy()
        else:
            return
    
    def check_mail(self):
        txt_msg= self.send_email_bill()
        messagebox.showinfo("Sent",f"Bill No. :{self.bill_no.get()} Sent successfuly")
        
        
    def send_email_bill(self):
        get_3 = self.c_mail.get()
        store_get_3 = get_3
        
        op=messagebox.askyesno("Send bill","Do you want to Send the bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            #fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
            msg=self.bill_data
        else:
            return  
        get_4 = msg
        store_get_4 = get_4
    
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("shopcrp040@gmail.com","crpshop040@")
            server.sendmail("shopcrp040@gmail.com",store_get_3,store_get_4)
            statement_1 = "MAIL HAS BEEN SENT"
            return statement_1
        except:
            statement_2 = "SOMETHING WENT WRONG"
            return statement_2
    def login_page(self):
        ad_id=self.admin_id.get()
        ad_pass=self.admin_pass.get()
        if(ad_id=="crpshop123"):
            if(ad_pass=="123456789"):
                global login_window
                login_window=Tk()
                
                obj1=login_page_window(login_window)
                
                
                
                login_window.mainloop()
            else:
                messagebox.showerror("Error","invalid password")
        else:
            messagebox.showerror("Error","invalid User id")
                
class login_page_window:
    def __init__(self, master1):
        self.master1=master1
        self.master1.geometry("1920x1080+-10+0")
        self.master1.title("Admin Area")

        title=Label(self.master1,text="CRP SHOP MANAGEMENT",bd=12,relief=GROOVE,bg="orange red",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #self.image_section2()
        
        F0=LabelFrame(self.master1,bd=10,relief=GROOVE,bg="orange red")
        F0.place(x=0,y=73,height=60,width=1537)
        F1=LabelFrame(self.master1,bd=10,relief=GROOVE,text="MENU",font=("times new roman",15,"bold"),fg="black",bg="tomato")
        F1.place(x=0,y=133,width=230,height=600)
        
        today_sell=Button(F1,text="Today's Sell",bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        
        total_sell=Button(F1,text="Total Sell",bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=1,column=0,padx=10,pady=15)
        
        stock=Button(F1,text="Stock",command=self.check_stock,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=2,column=0,padx=10,pady=15)
        
        update_stock=Button(F1,text="Update Stock",command=self.Update_stock,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=3,column=0,padx=10,pady=15)
        
        change_password=Button(F1,text="Change password",bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=4,column=0,padx=10,pady=15)
        
        lis_of_bill=Button(F1,text="Bill List",command=self.bill_list,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=5,column=0,padx=10,pady=15)
        
        clear=Button(F1,text="Clear",command=self.clear_admin_notebook,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=6,column=0,padx=10,pady=15)
        
        
        
        F3=LabelFrame(self.master1,bd=10,text="Bottom",relief=GROOVE,bg="tomato")
        F3.place(x=0,y=733,width=1537,height=60)
        
        
        
        
        # Notepad Area ....................................
        
        F4=LabelFrame(self.master1,bd=10,relief=GROOVE)
        F4.place(x=780,y=133,width=757,height=600)
        bill_title=Label(F4,text="Notepad Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.welcome_bill_admin()
        
        
        
        #---------------------------------------------
        
        
        
        
        
        
        img1=Image.open("onlineshop1.jpg")
        pic1=ImageTk.PhotoImage(img1)
        F2=LabelFrame(self.master1,bd=10,relief=GROOVE,bg="tomato")
        F2.place(x=230,y=133,width=550,height=600)
        
        F2_label1=Label(F2,image=pic1)
        F2_label1.image=pic1
        F2_label1.pack()
        # isko resolve krne k liye ek method hai ki close privious window and open this
        
        #F2=LabelFrame(self.master1,bd=10,text="image",relief=GROOVE,bg="tomato")
        #F2.place(x=230,y=133,width=550,height=600)
        
    def welcome_bill_admin(self):
            
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\t\t\t\t\t|| CRP SHOP ||")
            self.txtarea.insert(END,"\n_________________________________________________________________________________________\n")
    def check_stock(self):
        
        self.txtarea.delete('1.0',END)
        
        self.welcome_bill_admin()
        
        f1=open("stock.csv","r",encoding='utf-8-sig')
        
        #self.txtarea.insert(END,f1.read())
        self.txtarea.insert(END,"|| Product    || \t\t\t\t\t\t\t\t ||Quantity")
        self.txtarea.insert(END,"\n_________________________________________________________________________________________\n")
        for i in f1:
            data=i.split(",")
        #    print((data[0],data[1]))
            
            self.txtarea.insert(END,"\n"+data[0]+"\t\t\t\t\t\t\t\t "+data[1])
        
        f1.close()
    def clear_admin_notebook(self):
        self.txtarea.delete('1.0',END)
        self.welcome_bill_admin()
    
    def bill_list(self):
        
        j=1 
        self.txtarea.insert(END,"S.No.\t Bill \n\n")
        for i in os.listdir("bills/"):
           self.txtarea.insert(END,str(j)+".\t"+str(i)+"\n\n")
           j+=1
    def Update_stock(self):
        #os.startfile('stock.csv','r')            
         p=Popen('stock.csv',shell=True)       
        
        
        
global root       
root=Tk()

#obj=login_page_window(root)       
obj = Bill_App(root)
root.mainloop()