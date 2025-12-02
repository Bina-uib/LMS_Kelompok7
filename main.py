from tkinter import*
from tkinter import ttk

class mainapp:
    def __init__(self,root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("300x200")
        ttk.Label(self.root,text="usename: ").pack()
        self.entry_username=ttk.Entry(self.root)
        self.entry_username.pack()
        ttk.Label(self.root,text="pasword:").pack()
        self.entry_pasword=ttk.Entry(self.root,show="*")
        self.entry_pasword.pack()
        ttk.Button(self.root,text="login",command=self.proses_login ).pack(pady='20')

    def proses_login (self):
        username=self.entry_username.get()
        pasword=self.entry_pasword.get()


root=Tk() 
app=mainapp(root)
root.mainloop()
