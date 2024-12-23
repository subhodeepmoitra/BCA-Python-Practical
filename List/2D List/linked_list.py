class Node:
    def __init__(self, data):
        self.data = data # the data inside the node
        self.next = None # the reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None # initializing the LL with no elements and head set to None
    
    def append(self, data):
        new_node = Node(data) # create a new node with the given data
        if not self.head: # if list is empty set the new node as the head
            self.head = new_node
            return
        current = self.head # else traverse to the end of the LL
        while current.next:
            current = current.next
        current.next = new_node # set the next of the last node to the new node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") # end of the LL
    
    def delete(self, key):
        current = self.head
        # If the head node itself holds the key to be deleted
        if current and current.data == key: #if head node matches the key
            self.head = current.next # update to the head of the node to the next node
            current = None # free the old head node
            return
        #search for the key
        prev = None # keeps tract of the previous node
        while current and current.data != key:
            prev = current # move to the next node keeping track of the previous node
            current = current.next
        # if key is not found in the list. In context of delete the 'key' refers to the value of the node that is to be deleted
        if current is None:
            print(f"Key {key} not found in the list")
            return
        #Now unlinking the node
        prev.next = current.next
        current = None # free the memory of the deleted node

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
