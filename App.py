from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import os



def mget():

    if CheckVar1.get() and CheckVar15.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo(" WARNING!!", "  You have Symptoms of COVID-19\n Dont panic , Firstly isolate yourself. Contact to Medical officials,online or offline ,Contact to Doctor now, Maintain Social didtance \n  contact-+ +91-11-23978046 ")

    elif CheckVar1.get() and CheckVar5.get() or CheckVar1.get() and CheckVar6.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO","You may have Covid -19 ,\n if you have fever for a long time. Contact to doctor soon contact-+ +91-11-23978046 ")

    elif CheckVar6.get()and CheckVar7.get and CheckVar8.get() or CheckVar5.get()and CheckVar7.get() and CheckVar8.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", "If you body temperature rises,\n and\n Dry Cough Continues , \nGet in touch with Doctors .\n or Contact To HElpLINE\n\n contact-+ +91-11-23978046 ")

    elif CheckVar5.get() and CheckVar9.get() and CheckVar15.get() or CheckVar6.get() and CheckVar9.get() and CheckVar15.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("WARNING !!!", "DON'T PANIC!!!\n You have high Chances of having Covid-19.\nFirstly Stay isolated\n Dont get in touch with any Family members, or Friends   \n  GO TO HOSPITAL NOW , \n and  contact-+ +91-11-23978046 ")

    elif CheckVar5.get() and CheckVar8.get() and CheckVar12.get() and CheckVar15.get() or CheckVar6.get() and CheckVar8.get() and CheckVar12.get() and CheckVar15.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", "WARNING !!!, DON'T PANIC!!!\n You have high Chances of having Covid-19.\nFirstly Stay isolated\n Dont get in touch with any Family members, or Friends   \n  GO TO HOSPITAL NOW , \n and  contact-+ +91-11-23978046 contact-+ +91-11-23978046 ")

    elif CheckVar13.get() and CheckVar15.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", " Dont panic !! You may have Covid-19 , get in touch of Doctor  soon contact-+ +91-11-23978046 ")

    elif CheckVar5.get() and CheckVar11.get() and CheckVar15.get() or CheckVar6.get() and CheckVar11.get() and CheckVar15.get() :
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", "Dont panic !! You may have Covid-19 ,get isolated , \n get in touch of Doctor as soon as possible\n contact-+ +91-11-23978046 ")

    elif CheckVar15.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO","Short Breathing is a symptom of Corona Virus( COVID-19 )\n it is recommended to contact Doctors as soon as possible. \n You may contact to this helpline number\n contact-+ +91-11-23978046 ")

    elif CheckVar2.get() and CheckVar3.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO","Your Health is Not Good As Mentioned By You,\n Consult Doctor,\n If your Condition Worsens, \n Or you Can Contact\n\n contact-+ +91-11-23978046 ")

    elif CheckVar3.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO","Stay safe,as you have CANCER \n also you have\n Weak Immune System\n Then , your Health is not that good\n,if any Symptoms like Dry Cough , Short Breath, Fever\nappears ,\n Contact with your Doctor, asap \n \n or contact-+ +91-11-23978046 ")

    elif CheckVar1.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", "TAKE FULL CHECKUP OF COVID-19 \n as you have Diagnosed a lung disease, and it may be due to Corona Virus as it also affects lungs ,and causes breathing Problems \n For further quieries contact-+ +91-11-23978046 ")

    elif CheckVar4.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO"," It seems you have weak immune System, Stay Sfe,clean,hygenic,\n IF any above mentioned Symptoms appears,\n contact your Doctor as soon as possible,\n\n\nContact Helpline For Further Help  , \n\n\n\n\n Contact-+ +91-11-23978046 ")

    elif CheckVar2.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", " Your Health is Not Good As Mentioned By You\n also YOU HAVE HEART DISEASE \nas mentiones by you\nIf Symptoms like Fever, Joint Pain,Difficulty in Breathing appears , Contact with  Doctors or  contact-+ +91-11-23978046 ")

    elif CheckVar14.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("WARNING!!!!", " You may have COVID-19 \n as Corona Virus attack LUNGS and Causes Breathing problems , Get Contact to Doctors  contact-+ +91-11-23978046 ")

    elif CheckVar6.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("WARNING!!!!", " As you have Fever,\n Tke Care of yourself, Stay isolated,\If-\n1-> BODY TEMPERATURE IS HIGH \n or\n2->BODY TEMPERATURE IS RISING\n 3->SHORTNESS OF BREATHING OCCURS,\n\nGet Contact to Doctors  contact-+ +91-11-23978046 ")

    elif CheckVar13.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO", "Diarrhoea is aslo a Symptom of Covid-19, \n\nBut Dont Panic!\n! If Condition worsens,\nand in addition you have Fever,Dry Cough,\nShorten Breath \n\n\n Get Contact with Doctors \n\n or \n\ncontact-+ +91-11-23978046 ")

    elif CheckVar5.get() or CheckVar7.get() or CheckVar8.get() or CheckVar9.get() or CheckVar10.get() or CheckVar11.get() or CheckVar12.get() or CheckVar3.get():
        msg = messagebox.showinfo(E1.get(), "PRESS OK! To Know Your Results/Report")
        msg = messagebox.showinfo("INFO"," You are fine, just take care of your self,\n donot come in contact with others. if your condition worsens,\nand other symptoms add to your condition\n\n Contact to Professional Doctors aas soon as possible or contact-+ +91-11-23978046 ")

    else:
        msg = messagebox.showinfo(E1.get(), "Enter Valid Choice!!!")






create_secondwindow1 = Tk()
create_secondwindow1.minsize(1920,1000)
create_secondwindow1.title("SVASTHYA APP")

fram1= Frame(create_secondwindow1,width=100,height=200)

lab=Label (create_secondwindow1,text="SVASTHYA APP", font='Helvetica 16 bold underline ',fg = "BLACK",bg = "light blue",bd=20,width=100)
lab.pack()

lab1=Label (create_secondwindow1,text="What concerns you about your health today?\n\n Try Our App To Check About Your Health", font='Helvetica 16 bold italic',fg = "BLACK",bg = "PINK",bd=30,width=100)
lab1.pack()

img = ImageTk.PhotoImage(Image.open("Adps.jpg"))
panel = Label(create_secondwindow1, image = img)

panel.pack(side = "left", expand = "no")


fram1.pack()
fram2= Frame(create_secondwindow1,width=10,height=10)

L1 = Label(create_secondwindow1, text="YOUR NAME")
L1.pack( side = TOP)

E1 = Entry(create_secondwindow1, bd =10)
E1.pack(side = TOP)

fram2.pack()

fram2= Frame(create_secondwindow1,width=1920,height=800)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10= IntVar()
CheckVar11 = IntVar()
CheckVar12 = IntVar()
CheckVar13 = IntVar()
CheckVar14 = IntVar()
CheckVar15 = IntVar()

C1 = Checkbutton(create_secondwindow1, text="Diagnosed chronic lung disease", variable=CheckVar1, anchor=W, onvalue=1, offvalue=0, height=1, width=40)

C2 = Checkbutton(create_secondwindow1, text="History of heart failure", variable=CheckVar2, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C3 = Checkbutton(create_secondwindow1, text="Current cancer", variable=CheckVar3, anchor=W, onvalue=1, offvalue=0,height=1, width=40)

C4 = Checkbutton(create_secondwindow1, text="Diseases or drugs that weaken immune system", variable=CheckVar4,anchor=W, onvalue=1, offvalue=0, height=1, width=40)

C5 = Checkbutton(create_secondwindow1, text=" MILD Fever", variable=CheckVar5, anchor=W, onvalue=1, offvalue=0, height=1,width=40)

C6 = Checkbutton(create_secondwindow1, text="HIGH fever", variable=CheckVar6, anchor=W, onvalue=1, offvalue=0, height=1,width=40)

C7 = Checkbutton(create_secondwindow1, text="TIREDNESS", variable=CheckVar7, anchor=W, onvalue=1, offvalue=0, height=1,width=40)

C8 = Checkbutton(create_secondwindow1, text="Dry Cough", variable=CheckVar8, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C9 = Checkbutton(create_secondwindow1, text="Joint Pain  or  Body Pain", variable=CheckVar9, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C10 = Checkbutton(create_secondwindow1, text="Nasal Congession", variable=CheckVar10, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C11 = Checkbutton(create_secondwindow1, text="Runny Nose", variable=CheckVar11, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C12 = Checkbutton(create_secondwindow1, text="Sore Throat", variable=CheckVar12, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C13 = Checkbutton(create_secondwindow1, text="Diarrhoea", variable=CheckVar13, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C14 = Checkbutton(create_secondwindow1, text=" Are you coughing up blood? ", variable=CheckVar14, anchor=W, onvalue=1,offvalue=0, height=1, width=40)

C15 = Checkbutton(create_secondwindow1, text="Difficulty in Breathing! or Are you breathing very fast? ", variable=CheckVar15, anchor=W, onvalue=1,offvalue=0, height=1, width=40)




button3 = Button(create_secondwindow1, text="Confirm", command=mget,bd=20,bg='Light Blue',padx=200)
button4 = Button(create_secondwindow1, text="Exit",bd=20,bg='Red',padx=200, command=exit)

C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
C6.pack()
C7.pack()
C8.pack()
C9.pack()
C10.pack()
C11.pack()
C12.pack()
C13.pack()
C14.pack()
C15.pack()

button3.pack()
button4.pack()

create_secondwindow1.mainloop()