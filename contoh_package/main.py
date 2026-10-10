# 1. Import module dari package

from utils import matematika
print(matematika.tambah(2,3))

# 2. Import fungsi langsung

from utils.teks import huruf_besar
print(huruf_besar("mona"))

# 3. Import dengan alias
import utils.matematika as mtk
print(mtk.kali(2,5))

# 4. Contoh manfaat dan __init__.py
from utils import tambah, huruf_besar
print(tambah(5,10))
print(huruf_besar("ihsan"))