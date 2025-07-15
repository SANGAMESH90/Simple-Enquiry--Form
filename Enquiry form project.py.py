from tkinter import *
window=Tk()
#window1=Tk()
window.title("sign up")
window.configure(background = "skyblue")
window.geometry("700x700")
dvar=StringVar()
fNvar=StringVar()
lNvar=StringVar()
mobvar=StringVar()
altmobvar=StringVar()
emailvar=StringVar()
addressvar=StringVar()
coursevar=StringVar()
batchvar=StringVar()
knowUsvar=StringVar()
expvar=StringVar()
contactpersonvar=StringVar()
counselorvar=StringVar()
fessvar=StringVar()
commentsvar=StringVar()
def storeDataInTextfile():
    fobj=open("studentData.txt","a")
def showhworld():
    date=dvar.get()
    fNam=fNvar.get()
    lNam=lNvar.get()
    MobileNo=mobvar.get()
    Altmobile=altmobvar.get()
    email=emailvar.get()
    address=addressvar.get()
    course=coursevar.get()
    batch=batchvar.get()
    know_Us_var=knowUsvar.get()
    experience=expvar.get()
    contactPerson=contactpersonvar.get()
    counselor=counselorvar.get()
    fess=fessvar.get()
    comments=commentsvar.get()
    
    
    #print("Hello world")
    print("Date:",date)
    print("first name:",fNam)
    print("last name:",lNam)
    print("Mobile number:",MobileNo)
    print("Alternate mobile:",Altmobile)
    print("Email ID:",email)
    print("Address:",address)
    print("Course Insterested:",course)
    print("Batch preferred",batch)
    print("How you come to konwUs:",know_Us_var)
    print("Experience or fresher:",experience)
    print("Contact person from Basent Technologies:",contactPerson)
    print("Counselor:",counselor)
    print("fees:",fess)
    print("comments:",comments)
def storeData():
    showhworld()
    storeDataInTextfile()
def storeDataInTextfile():
    fobj = open("studentData.txt", "a")
    fobj.write("DATE: " + dvar.get() + "\n")
    fobj.write("NAME: " + fNvar.get() + "\n")
    fobj.write("MOBILE NO: " + mobvar.get() + "\n")
    fobj.write("ALTERNATE NO: " + altmobvar.get() + "\n")
    fobj.write("EMAIL ID: " + emailvar.get() + "\n")
    fobj.write("ADDRESS: " + addressvar.get() + "\n")
    fobj.write("COURSE INTERESTED: " + coursevar.get() + "\n")
    fobj.write("BATCH PREFERRED: " + batchvar.get() + "\n")
    fobj.write("HOW YOU CAME TO KNOW US: " + knowUsvar.get() + "\n")
    fobj.write("ARE YOU EXPERIENCE OR FRESHER: " + expvar.get() + "\n")
    fobj.write("CONTACT PERSON FROM BESANT TECHNOLOGIES: " + contactpersonvar.get() + "\n")
    fobj.write("COUNSELOR: " + counselorvar.get() + "\n")
    fobj.write("FEES: " + fessvar.get() + "\n")
    fobj.write("COMMENT: " + commentsvar.get() + "\n")
    fobj.close()
def signup():
   Label(window, text="Besant Technologies \n Enquiry Form",bg="white",fg="red",font="arial 15").grid(row=1,column=1,sticky="EW" )
   Label(window,text="date:",bg="skyblue",fg="black").grid(row=2,column=0,sticky=W)
   Label(window,text="first name:",bg="skyblue",fg="black").grid(row=3,column=0,sticky=W)
   Label(window,text="last name:",bg="skyblue",fg="black"). grid(row=4,column=0,sticky=W)
   Label(window,text="Mobile No:",bg="skyblue",fg="black"). grid(row=5,column=0,sticky=W)
   Label(window,text="Alternate Mobile:",bg="skyblue",fg="black"). grid(row=6,column=0,sticky=W)
   Label(window,text="Email ID:",bg="skyblue",fg="black"). grid(row=7,column=0,sticky=W)
   Label(window,text="Address:",bg="skyblue",fg="black").grid(row=8,column=0,sticky=W)
   Label(window,text="Course Insterested:",bg="skyblue",fg="black").grid(row=9,column=0,sticky=W)
   Label(window,text="Batch Preferred:",bg="skyblue",fg="black").grid(row=10,column=0,sticky=W)
   Label(window,text="How you come to konw us:",bg="skyblue",fg="black").grid(row=11,column=0,sticky=W)
   Label(window,text="Experience or fresher:",bg="skyblue",fg="black").grid(row=12,column=0,sticky=W)
   Label(window,text="Contact person from Basent Technologies:",bg="skyblue",fg="black").grid(row=13,column=0,sticky=W)
   Label(window,text="Counselor:",bg="skyblue",fg="black").grid(row=14,column=0,sticky=W)
   Label(window,text="fees:",bg="skyblue",fg="black").grid(row=15,column=0,sticky=W)
   Label(window,text="comments:",bg="skyblue",fg="black").grid(row=16,column=0,sticky=W)

 

   
   Entry(window ,textvariable=dvar).grid(row=2,column=1,ipadx=120)
   Entry(window ,textvariable=fNvar).grid(row=3,column=1,ipadx=120)
   Entry(window ,textvariable=lNvar).grid(row=4,column=1,ipadx=120)
   Entry(window ,textvariable=mobvar).grid(row=5,column=1,ipadx=120)
   Entry(window ,textvariable=altmobvar).grid(row=6,column=1,ipadx=120)
   Entry(window ,textvariable=emailvar).grid(row=7,column=1,ipadx=120)
   Entry(window ,textvariable=addressvar).grid(row=8,column=1,ipadx=120)
   Entry(window ,textvariable=coursevar).grid(row=9,column=1,ipadx=120)
   Entry(window ,textvariable=batchvar).grid(row=10,column=1,ipadx=120)
   Entry(window ,textvariable=knowUsvar).grid(row=11,column=1,ipadx=120)
   Entry(window ,textvariable=expvar).grid(row=12,column=1,ipadx=120)
   Entry(window ,textvariable=contactpersonvar).grid(row=13,column=1,ipadx=120)
   Entry(window ,textvariable=counselorvar).grid(row=14,column=1,ipadx=120)
   Entry(window ,textvariable=fessvar).grid(row=15,column=1,ipadx=120)
   Entry(window ,textvariable=commentsvar).grid(row=16,column=1,ipadx=120)
   
   Button(window,text="Submit",bg="green",fg="black",command=storeData).grid(row=18,column=1,sticky=W)
   Checkbutton(window,text="Enquiry",bg="white",fg="black",command=storeData).grid(row=17,column=1,sticky=W)
   Button(window,text="Quite",bg="red",fg="black",command=storeData).grid(row=18,column=2,sticky=W)
   Checkbutton(window,text="Registration",bg="white",fg="black",command=storeData).grid(row=17,column=2,sticky=W)
signup()



























