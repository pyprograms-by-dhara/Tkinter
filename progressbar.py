#progressbar
from  tkinter  import*
from  tkinter.ttk  import* 
def bar():
     import time
     for i in range(11):
             pbar['value']=i*10
             lblpbarval.config(text=str(i*10)+"%")
             root.update_idletasks()
             time.sleep(1)
def resetbar():
          pbar['value']=0
          lblpbarval.config(text="0%")

root=Tk()
root.title("Progressbar Demo")
root.geometry("500x500")
pbar=Progressbar(root,orient=HORIZONTAL,length=200)
pbar.place(x=50,y=50)
lblpbarval=Label(root,text="0%",font=("bold",10))
lblpbarval.place(x=250,y=50)
Button(root,text='Start Progressbar',command=bar).place(x=50,y=100)
Button(root,text='Reset Progressbar',command=resetbar).place(x=250,y=100)
root.mainloop()
