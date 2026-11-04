from models.buku_models import BukuModel

model = BukuModel()

# 1. Kirim data sesuai kolom tabel di Laragon (id_buku, judul_buku, stok)
print("Menambahkan data buku...")
model.create_buku("BK005", "Pemrograman Python MVC", 10)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Tampilkan daftar buku sesuai kolom tabel di Laragon
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul_buku']} - Stok: {buku['stok']}")