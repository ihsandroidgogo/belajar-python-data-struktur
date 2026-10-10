# Contoh 1

buah = ["apel","jeruk","mangga"] # ini iterable

it = iter(buah) # ubah jadi iterator

print(next(it))
print(next(it))
print(next(it))

# Contoh 2

class Hitung:
    def __init__(self,batas):
        self.batas = batas
        self.angka = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.angka >= self.batas:
            raise StopIteration
        self.angka += 1
        return self.angka

for n in Hitung(5):
    print(n)



'''
Catatan : 
Membuat Iterator Sendiri

Sebuah class menjadi iterator jika punya dua method:

__iter__() → mengembalikan dirinya sendiri
__next__() → mengembalikan item berikutnya

Kenapa Iterator Berguna?

Hemat memori. Iterator tidak menyimpan semua data sekaligus, hanya membuat item saat diminta.
Ini penting saat memproses file besar atau data tak terbatas.

Hal Penting yang Perlu Diingat!

Iterator hanya bisa dipakai sekali

'''
