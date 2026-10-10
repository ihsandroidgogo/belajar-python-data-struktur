# Bentuk dasar lambda parameter: ekspresi

kuadrat = lambda x: x * x

print(kuadrat(5))  # 25

tambah = lambda a,b: a + b 

print(tambah(2,3))

cek = lambda angka: "Genap" if angka % 2 == 0 else "Ganjil"

print(cek(10))  # Genap
print(cek(7))   # Ganjil

# sorted(): Mengurutkan dengan Aturan Sendiri
siswa = [("Budi", 80), ("Ani", 95), ("Citra", 70)]

# Urutkan berdasarkan nilai (elemen ke-2)
hasil = sorted(siswa, key=lambda s: s[1])

print(hasil)

# map(): Mengubah Semua Elemen

angka = [1, 2, 3, 4, 5]

dua_kali = list(map(lambda x: x * 2, angka))

print(dua_kali) 

# filter(): Menyaring Elemen
angka = [1, 2, 3, 4, 5, 6]

genap = list(filter(lambda x: x % 2 == 0, angka))

print(genap)  