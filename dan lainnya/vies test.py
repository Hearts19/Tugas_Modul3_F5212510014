import tkinter as tk
from tkinter import ttk

# Membuat Jendela Utama
root = tk.Tk()
root.title("Aplikasi Manajemen Perpustakaan")
root.geometry("900x500")
root.configure(bg="#2b2b2b")

# Frame Kiri (Form Input)
frame_kiri = tk.Frame(root, bg="#2b2b2b")
frame_kiri.pack(side="left", fill="both", expand=True, padx=20, pady=20)

tk.Label(frame_kiri, text="Form Data Buku", fg="white", bg="#2b2b2b", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(frame_kiri, text="Judul Buku", fg="white", bg="#2b2b2b", anchor="w").pack(fill="x", pady=(5,0))
entry_judul = tk.Entry(frame_kiri, bg="#3c3f41", fg="white", insertbackground="white")
entry_judul.pack(fill="x", pady=5)

tk.Label(frame_kiri, text="Penulis", fg="white", bg="#2b2b2b", anchor="w").pack(fill="x", pady=(5,0))
entry_penulis = tk.Entry(frame_kiri, bg="#3c3f41", fg="white", insertbackground="white")
entry_penulis.pack(fill="x", pady=5)

tk.Label(frame_kiri, text="Tahun Terbit", fg="white", bg="#2b2b2b", anchor="w").pack(fill="x", pady=(5,0))
entry_tahun = tk.Entry(frame_kiri, bg="#3c3f41", fg="white", insertbackground="white")
entry_tahun.pack(fill="x", pady=5)

btn_simpan = tk.Button(frame_kiri, text="Simpan Data", bg="green", fg="white", font=("Arial", 10, "bold"))
btn_simpan.pack(fill="x", pady=20)

# Frame Kanan (Tabel/View)
frame_kanan = tk.Frame(root, bg="#2b2b2b")
frame_kanan.pack(side="right", fill="both", expand=True, padx=20, pady=20)

tk.Label(frame_kanan, text="Daftar Koleksi Buku", fg="white", bg="#2b2b2b", font=("Arial", 14, "bold")).pack(pady=10)

columns = ("id", "judul", "penulis", "tahun")
tabel = ttk.Treeview(frame_kanan, columns=columns, show="headings")
tabel.heading("id", text="ID")
tabel.heading("judul", text="Judul")
tabel.heading("penulis", text="Penulis")
tabel.heading("tahun", text="Tahun")

tabel.column("id", width=50)
tabel.column("judul", width=150)
tabel.column("penulis", width=120)
tabel.column("tahun", width=80)

tabel.pack(fill="both", expand=True)

root.mainloop()