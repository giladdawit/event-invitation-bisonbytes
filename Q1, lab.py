#I95 is an interstate highway in the United States that goes through the following states:

#Maine, New Hampshire, Massachusetts, Rhode Island, Connecticut, New York,  New Jersey, Delaware, Maryland, District of Columbia, Virginia, North Carolina, South Carolina, Georgia, and Florida.

#Question 1 : Write python code to create a Doubly linked list to represent these states in the order they are written above

class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail= None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        if not current:
            print("The list is empty")
            return
        while current:
            print(current.data, end= ', ')
            current = current.next

I95 = DoublyLinkedList()

states = [
    "Maine", "New Hampshire", "Massachusetts", "Rhode Island", 
          "Connecticut", "New York",  "New Jersey", "Delaware", 
          "Maryland", "District of Columbia", "Virginia", 
          "North Carolina", "South Carolina", "Georgia", "Florida"
]
for state in states:
    I95.append(state)
I95.display_forward()