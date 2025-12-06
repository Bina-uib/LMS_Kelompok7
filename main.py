from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

class mainapp:
<<<<<<< HEAD
    def __init__(self,root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("300x200")
        ttk.Label(self.root,text="username: ").pack()
        self.entry_username=ttk.Entry(self.root)
=======
    def __init__(self, root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("500x200")

        ttk.Label(self.root, text="username: ").pack()
        self.entry_username = ttk.Entry(self.root)
>>>>>>> 372084b513046f35a00beeff1c543353faeee26b
        self.entry_username.pack()

    
        ttk.Label(self.root, text="password: ").pack()
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()

        
        ttk.Button(self.root, text="login", command=self.proses_login).pack(pady=20)

    def proses_login(self):
        nama_mahasiswa = self.entry_username.get()
        password = self.entry_password.get()

        query = f"SELECT * FROM tabel_mahasiswa WHERE Nama_mahasiswa= '{nama_mahasiswa}' AND Password_mahasiswa= '{password}'"
        print(query)
        database.db_conn.cursor.execute(query)
        result = database.db_conn.cursor.fetchone()

        if result:
            messagebox.showinfo("Sukses", "Login berhasil!")
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")


root = Tk()
app = mainapp(root)
root.mainloop()