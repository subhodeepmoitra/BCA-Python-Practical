class Node:
    def __init__(self, data, node_id):
        self.data = data # the data inside the node
        self.id = node_id # a unique identifier for the node
        self.next = None # the reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None # initializing the LL with no elements and head set to None
        self.counter = 0 # counter to generate the unique ID
    
    def append(self, data):
        new_node = Node(data, self.counter) # create a new node with the given data
        self.counter += 1
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
            print(f"ID: {current.id} Data: {current.data}")
            current = current.next
        print("None") # end of the LL
    
    def delete_by_id(self, node_id):
        current = self.head
        # If the head node itself holds the key to be deleted
        if current and current.id == node_id: #if head node matches the key
            self.head = current.next # update to the head of the node to the next node
            current = None # free the old head node
            return
        #search for the key
        prev = None # keeps tract of the previous node
        while current and current.id != node_id:
            prev = current # move to the next node keeping track of the previous node
            current = current.next
        # if key is not found in the list. In context of delete the 'key' refers to the value of the node that is to be deleted
        if current is None:
            print(f"ID {node_id} not found in the list")
            return
        #Now unlinking the node
        prev.next = current.next
        current = None # free the memory of the deleted node

ll = LinkedList()
ll.append({"name":"J. Robert Oppenheimer", "famous for":"Atom bomb and quantum mechanics"})
ll.append({"name":"Heisenburg", "famous for":"Uncertainty Principle"})
ll.append({"name":"Goodfellow", "famous for":"Deep learning"})
print("The initial likedlist is: ")
ll.print_list()
ll.delete_by_id(1)
print("After deleting 2 from the linkedlist")
ll.print_list()
ll.delete_by_id(0)
print("After deleting 1 from the linkedlist")
ll.print_list()
ll.delete_by_id(0)
ll.delete_by_id(2)
print("After deleting 3 from the linkedlist")
ll.print_list()
