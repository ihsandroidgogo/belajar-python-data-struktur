# Contoh Sederhana
def greet():
    print("contoh decorator")

fungsi_decorator = greet
fungsi_decorator()

# Fungsi dengan Argumen
# Agar decorator bisa dipakai untuk fungsi apa pun, gunakan *args dan **kwargs:

def dekorator(fungsi):
    def pembungkus(*args, **kwargs):
        print("Fungsi mau dijalankan...")
        hasil = fungsi(*args, **kwargs)
        print("Fungsi Selesai")
        return hasil
    return pembungkus

@dekorator
def tambah(a,b):
    return a + b

print(tambah(3,5))


# Contoh nyata
import time

def hitung_waktu(fungsi):
    def pembungkus(*args,**kwargs):
        mulai = time.time()
        hasil = fungsi(*args,**kwargs)
        selesai = time.time()
        print(f"{fungsi.__name__} selesai dalam {selesai - mulai:.4f} detik")
        return hasil
    return pembungkus

@hitung_waktu
def proses_berat():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

proses_berat()

# Contoh Decorator dengan Parameter

from functools import wraps

def ulangi(n):
    def dekorator(fungsi):
        @wraps(fungsi)
        def pembungkus(*args, **kwargs):
            for _ in range(n):
                fungsi(*args, **kwargs)
        return pembungkus
    return dekorator

@ulangi(3)
def semangat():
    print("Ayo belajar Python!")

semangat()

'''
Catatan : 
*args digunakan untuk menampung argumen posisi (positional arguments).
**kwargs digunakan untuk menampung argumen kata kunci (keyword arguments).
- def dekorator dan @dekorator nama nya harus sama
- Perhatikan return hasil. Tanpa ini, nilai kembalian fungsi asli akan hilang
- Tips Penting: Pakai functools.wraps (Tanpa ini, fungsi yang didekorasi kehilangan nama dan dokumentasinya)
'''

