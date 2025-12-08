from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

class mainapp:

    def __init__(self, root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("500x300")
        self.root.configure(bg="#e8e8e8")   

        self.halaman_login()

    # ============================
    # HALAMAN LOGIN
    # ============================
    def halaman_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = Frame(self.root, bg="white", relief="raised", bd=2)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=220)

        Label(frame, text="LOGIN LMS", bg="white", fg="#333",
              font=("Segoe UI", 16, "bold")).pack(pady=10)

        Label(frame, text="username:", bg="white").pack()
        self.entry_username = ttk.Entry(frame, width=30)
        self.entry_username.pack(pady=3)

        Label(frame, text="password:", bg="white").pack()
        self.entry_password = ttk.Entry(frame, width=30, show="*")
        self.entry_password.pack(pady=3)

        ttk.Button(frame, text="login", command=self.proses_login).pack(pady=15)

    def proses_login(self):
        nama = self.entry_username.get()
        pw = self.entry_password.get()

        query = f"""
        SELECT * FROM tabel_mahasiswa
        WHERE Nama_mahasiswa = '{nama}' AND Password_mahasiswa = '{pw}'
        """

        database.db_conn.cursor.execute(query)
        result = database.db_conn.cursor.fetchone()

        if result:
            messagebox.showinfo("Sukses", "Login berhasil!")
            self.halaman_menu()
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")

    # ============================
    # HALAMAN MENU UTAMA
    # ============================
    def halaman_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#f2f2f2")

        # Tombol Logout kanan atas
        Button(self.root, text="Logout", bg="#d9534f", fg="white",
               command=self.halaman_login).place(x=430, y=10)

        # Judul
        Label(self.root, text="MENU UTAMA LMS", bg="#f2f2f2",
              font=("Segoe UI", 17, "bold")).pack(pady=25)

        # Frame tombol
        frame = Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=10)

        # Tombol Data Mahasiswa
        Button(frame, text="Data Mahasiswa", width=20, height=2,
               command=self.buka_data_mahasiswa).grid(row=0, column=0, padx=10, pady=10)

        # Tombol Mata Kuliah
        Button(frame, text="Mata Kuliah", width=20, height=2,
               command=self.buka_mata_kuliah).grid(row=0, column=1, padx=10, pady=10)

    # ============================
    # HALAMAN DATA MAHASISWA
    # ============================
    def buka_data_mahasiswa(self):
        messagebox.showinfo("Info", "Menu Data Mahasiswa dibuka.\nSambungkan ke mahasiswa.py")

    # ============================
    # HALAMAN MATA KULIAH
    # ============================
    def buka_mata_kuliah(self):
        messagebox.showinfo("Info", "Menu Mata Kuliah dibuka.\nSambungkan ke prodi.py")


root = Tk()
app = mainapp(root)
root.mainloop()
