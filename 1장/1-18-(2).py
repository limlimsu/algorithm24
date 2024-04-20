<<<<<<< HEAD
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        current_node = self.head
        while current_node.link:
            current_node = current_node.link
        current_node.link = Node(data, None)

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.link
        print()

mylist = LinkedList()  # LinkedList 객체 생성

num = int(input("노드의 개수: "))  # 리스트의 크기

for i in range(num):
    data = int(input(f"노드 #{i + 1} 데이터: ")) # f 문자열 리터럴 
    mylist.append(data)

print("리스트의 내용:", end=" ")
=======
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        current_node = self.head
        while current_node.link:
            current_node = current_node.link
        current_node.link = Node(data, None)

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.link
        print()

mylist = LinkedList()  # LinkedList 객체 생성

num = int(input("노드의 개수: "))  # 리스트의 크기

for i in range(num):
    data = int(input(f"노드 #{i + 1} 데이터: ")) # f 문자열 리터럴 
    mylist.append(data)

print("리스트의 내용:", end=" ")
>>>>>>> a796d30380d346a231c2907501bf5f71f82f0634
mylist.display()  # 리스트에 저장된 데이터 출력