def factorial(n):
    if n == 0 or n == 1 :
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def jumlah(n):
    if n == 0:
        return 0
    return n + jumlah(n - 1)

print(jumlah(4))   # 10

def sum_list(lst):
    if not lst:                 # list kosong
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))   # 10

# Contoh Menarik :
def ratakan(data):
    hasil = []
    for item in data:
        if isinstance(item, list):
            hasil.extend(ratakan(item))   # rekursi untuk list di dalam list
        else:
            hasil.append(item)
    return hasil

print(ratakan([1, [2, [3, 4]], 5]))   # [1, 2, 3, 4, 5]

