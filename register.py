from tkinter import*
from tkinter import messagebox
import sqlite3
def showdata():
    window=Tk()
    window.geometry("600x800")
    window.title("Records")
    connection=sqlite3.connect("Form.db")
    cur=connection.cursor()
    namelbl=Label(window,text="Name",width=20,bg="green",)
    namelbl.grid(row=0,column=0)
    emaillbl=Label(window,text="Email",width=20,bg="green",)
    emaillbl.grid(row=0,column=1)
    genderlbl=Label(window,text="Gender",width=20,bg="green",)
    genderlbl.grid(row=0,column=2)
    countrylbl=Label(window,text="Country",width=20,bg="green",)
    countrylbl.grid(row=0,column=3)
    prolbl=Label(window,text="Programming",width=20,bg="green",)
    prolbl.grid(row=0,column=4)
    cur.execute("SELECT * FROM Student")
    data=cur.fetchall()
    for index,dat in enumerate(data):
        Label(window,text=dat[0]).grid(row=index+1,column=0)
        Label(window,text=dat[1]).grid(row=index+1,column=1)
        if dat[2]=="2":
            Label(window,text="Female").grid(row=index+1,column=2)
        else:
            Label(window,text="Male").grid(row=index+1,column=2)
        Label(window,text=dat[3]).grid(row=index+1,column=3)
        Label(window,text=dat[4]).grid(row=index+1,column=4)
              
    
def database():
    name1=Fullname.get()
    email1=Email.get()
    gender=var.get()
    country=c.get()
    prog1=""
   # print(var1.get())
   # print(var2.get())
    if var1.get==1:
        print="Java"
    if var2.get==1:
        prog1=prog1+" Python"
    prog=var1.get()
    conn=sqlite3.connect("Form.db")
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Student(Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)")
        cur.execute("INSERT INTO Student(Fullname,Email,Gender,country,Programming)VALUES(?,?,?,?,?)",(name1,email1,gender,country,prog1))
        conn.commit()
    Fullname.set("")
    Email.set("")
    var.set(0)
    c.set('select your country')
    var1.set(0)
    var2.set(0)
    messagebox.showinfo("Message","Record added successfully")

root=Tk()
root.geometry("500x500")
root.title("Registration Form")

Fullname=StringVar()
Email=StringVar()
var=IntVar()
c=StringVar()
var1=IntVar()
var2=IntVar()

lbltitle=Label(root,text="Registration Form",width=20,font=("bold",20))
lbltitle.place(x=90,y=53)

lblfnm=Label(root,text="Full Name",width=20,font=("bold",10))
lblfnm.place(x=50,y=130)
txtfnm=Entry(root,textvar=Fullname)
txtfnm.place(x=200,y=130)

lblemail=Label(root,text="Email",width=20,font=("bold",10))
lblemail.place(x=45,y=180)
txtemail=Entry(root,textvar=Email)
txtemail.place(x=200,y=180)

lblgen=Label(root,text="Gender",width=20,font=("bold",10))
lblgen.place(x=45,y=230)
Radiobutton(root,text="Male",variable=var,padx=5,value=1).place(x=185,y=230)
Radiobutton(root,text="Female",variable=var,padx=5,value=2).place(x=250,y=230)

lblcon=Label(root,text="Country",width=20,font=("bold",10))
lblcon.place(x=45,y=280)
list1=["India","USA","UK","Nepal","Canada","Pak"]
c.set("Select Your Country")
dropdownlist=OptionMenu(root,c,*list1)
dropdownlist.place(x=180,y=270)

lblprg=Label(root,text="Programming",width=20,font=("bold",10))
lblprg.place(x=45,y=320)
Checkbutton(root,text="Java",variable=var1).place(x=185,y=320)
Checkbutton(root,text="Python",variable=var2).place(x=250,y=320)

Button(root,text="Submit",bg="brown",width=15,fg="white",relief=GROOVE,font=("bold",15),command=database).place(x=100,y=380)
Button(root,text="Show Data",bg="brown",width=15,fg="white",relief=GROOVE,font=("bold",15),command=showdata).place(x=280,y=380)
             



root.mainloop()

