angka = [5,3,9,2,1,7]

print(sorted(angka))
print(sorted(angka, reverse=True))
angka.sort()

def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(n - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        kunci = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > kunci:
            arr[j + 1] = arr[j]     # geser ke kanan
            j -= 1
        arr[j + 1] = kunci          # sisipkan
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    tengah = len(arr) // 2
    kiri = merge_sort(arr[:tengah])
    kanan = merge_sort(arr[tengah:])
    return merge(kiri, kanan)

def merge(kiri, kanan):
    hasil = []
    i = j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    kiri = [x for x in arr if x < pivot]
    tengah = [x for x in arr if x == pivot]
    kanan = [x for x in arr if x > pivot]
    return quick_sort(kiri) + tengah + quick_sort(kanan)

menu = [("nasi goreng", 25000), ("es teh", 5000), ("mie ayam", 20000)]

# berdasarkan harga
print(sorted(menu, key=lambda m: m[1]))

# harga tertinggi dulu
print(sorted(menu, key=lambda m: m[1], reverse=True))

# berdasarkan nama
print(sorted(menu, key=lambda m: m[0]))