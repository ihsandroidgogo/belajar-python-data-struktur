class HashMap:
    def __init__(self, ukuran=8):
        self.ukuran = ukuran
        self.bucket = [[] for _ in range(ukuran)]

    def _index(self, key):
        return hash(key) % self.ukuran

    def put(self, key, value):
        b = self.bucket[self._index(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b[i] = (key, value)   # key sudah ada -> update
                return
        b.append((key, value))

    def get(self, key, default=None):
        b = self.bucket[self._index(key)]
        for k, v in b:
            if k == key:
                return v
        return default

    def remove(self, key):
        b = self.bucket[self._index(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                del b[i]
                return


hm = HashMap()
hm.put("nasi goreng", 25000)
hm.put("mie ayam", 20000)
print(hm.get("mie ayam"))   # 20000
print(hm.get("soto", 0))    # 0
hm.remove("mie ayam")
print(hm.get("mie ayam"))   # None