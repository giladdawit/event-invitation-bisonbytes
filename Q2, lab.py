#In question 1 above, the state, Pennsylvania is missing between New Jersey and Delaware.
#Question 2:  Write python code to insert Pennsylvania between New Jersey and Delaware in the doubly linked list in question 1


class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                new_node.prev = current
                
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node 
                
                current.next = new_node
                return
            
            current = current.next
        
        print(f"State '{target_data}' not found in the list.")
    
    def display_forward(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=', ')
            current = current.next
        print("None")

I95 = DoublyLinkedList()

states = [
    "Maine", "New Hampshire", "Massachusetts", "Rhode Island", 
    "Connecticut", "New York", "New Jersey", "Delaware", 
    "Maryland", "District of Columbia", "Virginia", 
    "North Carolina", "South Carolina", "Georgia", "Florida"
]

for state in states:
    I95.append(state)

I95.display_forward()

I95.insert_after("New Jersey", "Pennsylvania")

print("\nList after inserting the new state:")
I95.display_forward()

