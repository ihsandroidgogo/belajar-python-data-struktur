# Contoh Sederhana

import re

teks = "Saya suka Belajar Python"

hasil = re.search("Python", teks)
print(hasil)
print(hasil.group) # Python

# Kalau tidak ketemu, hasilnya None
print(re.search("Java", teks))  # None

# Contoh: mengambil semua angka dari teks
kalimat = "Harga apel 15000, jeruk 20000, mangga 35000"
angka = re.findall(r"\d+", kalimat)
print(angka)

# Posisi (Anchor)
print(re.search(r"^Halo", "Halo dunia"))   # cocok
print(re.search(r"^Halo", "Oh, Halo"))     # None (Halo tidak di awal)
print(re.search(r"dunia$", "Halo dunia"))  # cocok

# Kumpulan Karakter [ ]
contoh_teks = "Kode: AB123, CD456"
print(re.findall(r"[A-Z]{2}\d{3}", contoh_teks))

# Grup ( ) untuk Mengambil Bagian Tertentu
tanggal_lahir = "Tanggal lahir: 17-08-1945"

hasil = re.search(r"(\d{2})-(\d{2})-(\d{4})", tanggal_lahir)

print(hasil.group(0))  # 17-08-1945 (semuanya)
print(hasil.group(1))  # 17 (hari)
print(hasil.group(2))  # 08 (bulan)
print(hasil.group(3))  # 1945 (tahun)

r'''
Catatan : 
Biasakan menulis pola dengan awalan r (raw string), contoh r"\d+". Ini mencegah Python salah mengartikan tanda \.
'''