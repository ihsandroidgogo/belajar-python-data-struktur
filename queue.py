from collections import deque

antrean = deque()

antrean.append("Ihsan")
antrean.append("Ayana")
antrean.append("Mona")
print(antrean)

print(antrean.popleft())
print(antrean.popleft())
print(antrean[0])

# Contoh klasik: BFS (pencarian level demi level)

graf = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

def bfs(mulai):
    dikunjungi = {mulai}
    antrean = deque([mulai])
    while antrean:
        node = antrean.popleft()
        print(node, end=" ")
        for tetangga in graf[node]:
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                antrean.append(tetangga)

bfs("A")   # A B C D