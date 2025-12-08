from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

class mainapp:

    def __init__(self, root):
        self.root = root
        self.root.title("LMS")
        self.root.geometry("5000x3000")
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

        Button(self.root, text="Logout", bg="#d9534f", fg="white",
               command=self.halaman_login).place(x=430, y=10)

        Label(self.root, text="MENU UTAMA LMS", bg="#f2f2f2",
              font=("Segoe UI", 17, "bold")).pack(pady=25)

        frame = Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=10)

        Button(frame, text="Data Mahasiswa", width=20, height=2,
               command=self.buka_data_mahasiswa).grid(row=0, column=0, padx=10, pady=10)

        Button(frame, text="Mata Kuliah", width=20, height=2,
               command=self.buka_mata_kuliah).grid(row=0, column=1, padx=10, pady=10)

    # ============================
    # HALAMAN DATA MAHASISWA
    # ============================
    def buka_data_mahasiswa(self):
        messagebox.showinfo("Info", "Menu Data Mahasiswa dibuka.\nSambungkan ke mahasiswa.py")

    # ============================
    # HALAMAN PILIH KELAS MATA KULIAH
    # ============================
    def buka_mata_kuliah(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#f2f2f2")

        Button(self.root, text="Kembali", bg="#0275d8", fg="white",
               command=self.halaman_menu).place(x=10, y=10)

        Label(self.root, text="Pilih Kelas", bg="#f2f2f2",
              font=("Segoe UI", 17, "bold")).pack(pady=25)

        frame = Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=10)

        Button(frame, text="KELAS TIMA", width=20, height=2,
               command=lambda: self.tampilkan_mk("tima")).grid(row=0, column=0, padx=10, pady=10)

        Button(frame, text="KELAS TIMB", width=20, height=2,
               command=lambda: self.tampilkan_mk("timb")).grid(row=0, column=1, padx=10, pady=10)

    # ============================
    # TAMPILKAN DATA MATA KULIAH
    # ============================
    def tampilkan_mk(self, nama_kelas):
        for widget in self.root.winfo_children():
            widget.destroy()

        Button(self.root, text="Kembali", bg="#0275d8", fg="white",
               command=self.buka_mata_kuliah).place(x=10, y=10)

        Label(self.root, text=f"DAFTAR MATA KULIAH - {nama_kelas.upper()}",
              font=("Segoe UI", 16, "bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack()

        kolom = ("hari", "jam", "nama_mk", "dosen")

        tabel = ttk.Treeview(frame, columns=kolom, show="headings", height=10)
        tabel.pack()

        tabel.heading("hari", text="Hari")
        tabel.heading("jam", text="Jam")
        tabel.heading("nama_mk", text="Nama Mata Kuliah")
        tabel.heading("dosen", text="Dosen Pengampu")

        tabel.column("hari", width=100)
        tabel.column("jam", width=100)
        tabel.column("nama_mk", width=230)
        tabel.column("dosen", width=200)

        # ========================================
        # TIMA → ambil dari tabel matakuliah
        # TIMB → ambil dari tabel tabel_matakuliah
        # ========================================
        if nama_kelas == "tima":
            query = """
            SELECT jadwal_matakuliah, jam_matakuliah, nama_matakuliah, nama_dosen_matakuliah 
            FROM matakuliah
            """
        else:
            query = """
            SELECT jadwal_matakuliah, jam_matakuliah, nama_matakuliah, nama_dosen_matakuliah 
            FROM tabell_matakuliah
            """

        database.db_conn.cursor.execute(query)
        data = database.db_conn.cursor.fetchall()

        for row in data:
            tabel.insert("", "end", values=row)


root = Tk()
app = mainapp(root)
root.mainloop()