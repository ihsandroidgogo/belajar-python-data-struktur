import heapq # hanya untuk Min-Heap

heap = []

heapq.heappush(heap,5)
heapq.heappush(heap,1)
heapq.heappush(heap,3)
heapq.heappush(heap,8)
heapq.heappush(heap,4)
heapq.heappush(heap,2)

print(heap[0])
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

# Contoh Max-heap
mh = []
for x in [5, 1, 8, 3]:
    heapq.heappush(mh, -x)

print(-heapq.heappop(mh))      # 8 (terbesar)

# Priority queue dengan tuple

tugas = []
heapq.heappush(tugas, (2, "balas email"))
heapq.heappush(tugas, (1, "deadline laporan"))
heapq.heappush(tugas, (3, "rapikan meja"))

while tugas:
    prioritas, nama = heapq.heappop(tugas)
    print(prioritas, nama)
# 1 deadline laporan
# 2 balas email
# 3 rapikan meja