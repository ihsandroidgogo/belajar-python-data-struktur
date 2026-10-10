# Keyword global
skor = 0

def tambah_skor():
    global skor          # beri tahu Python: pakai skor yang global
    skor = skor + 10

tambah_skor()
tambah_skor()
print(skor)              # 20

# Scope Bersarang dan nonlocal
def luar():
    hitung = 0

    def dalam():
        nonlocal hitung   # pakai variabel dari fungsi luar
        hitung += 1

    dalam()
    dalam()
    print(hitung)         # 2

luar()