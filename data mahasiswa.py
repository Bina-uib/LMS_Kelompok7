from tkinter import*
from tkinter import ttk

class mainapp:
    def __init__(self,root):
        self.root=root
        self.main_page()

    def main_page (self):
        self.root.title("Data Matakuliah")
        self.root.geometry("500x250")
        ttk.Label(self.root,text="Nama Matakuliah:   ").pack()
        self.entry_Nama_Matakuliah=ttk.Entry(self.root)
        self.entry_Nama_Matakuliah.pack()
        ttk.Label(self.root,text="Kode kelas:   ").pack()
        self.entry_Kode_kelas=ttk.Entry(self.root)
        self.entry_Kode_kelas.pack()
        ttk.Button(self.root,text="Enter",command=self.proses_loading   ).pack(pady='20')
    
    def sub_page (self):
        self.clear_window ()

        self.root.title("Data Jadwal")
        self.root.geometry("500x250")
        ttk.Label(self.root,text="Nama Matakuliah:   ").pack()
        self.entry_Nama_Matakuliah=ttk.Entry(self.root)
        self.entry_Nama_Matakuliah.pack()
        ttk.Label(self.root,text="Waktu (Pagi atau Malam):    ").pack()
        self.entry_Waktu_Pagi_atau_Malam=ttk.Entry(self.root,show="*")
        self.entry_Waktu_Pagi_atau_Malam.pack()

    def proses_loading (self):
        Nama=self.entry_Nama_Matakuliah.get()
        Prodi=self.entry_Kode_kelas.get()

        self.sub_page ()

    def clear_window(self):
        for widget in self.root.winfo_children():
                widget.destroy()
        


root=Tk() 
app=mainapp(root)
root.mainloop()