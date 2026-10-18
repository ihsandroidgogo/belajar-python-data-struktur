class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node_baru

    def prepend(self,data):
        node_baru = Node(data)
        node_baru.next = self.head
        self.head = node_baru

    def delete(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data :
                current.next = current.next.next
                return
            current = current.next

    def find(self,data):
        current = self.head
        while current :
            if current.data == data:
                return True
            current = current.next
        return False

    def tampilkan(self):
        hasil = []
        current = self.head
        while current:
            hasil.append(str(current.data))
            current = current.next
        print(" -> ".join(hasil) + " => None ")

# Contoh Pemakaian
isiLinkedList = LinkedList()
isiLinkedList.append(10)
isiLinkedList.append(20)
isiLinkedList.append(30)
isiLinkedList.prepend(5)
isiLinkedList.tampilkan()

print(isiLinkedList.find(30))