import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.geometry('300x300')
States=["Gujarat","Punjab","MP","UP","Rajsthan"]
combo1=ttk.Combobox(root,values=States)
combo1.grid(column=0,row=1)
combo1.current(2)
print(combo1.current(),combo1.get())
root.mainloop
     

