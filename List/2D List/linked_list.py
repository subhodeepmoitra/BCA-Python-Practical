class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def delete(self, key):
        current = self.head
        if current and current.data == key: #if head node matches the key
            self.head = current.next
            current = None
            return
        #search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print(f"Key {key} not found in the list")
            return
        #Now unlinking the node
        prev.next = current.next
        current = None

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("The initial likedlist is: ")
ll.print_list()
ll.delete(20)
print("After deleting 20 from the linkedlist")
ll.print_list()
ll.delete(10)
print("After deleting 10 from the linkedlist")
ll.print_list()
ll.delete(10)
ll.delete(30)
print("After deleting 30 from the linkedlist")
ll.print_list()
