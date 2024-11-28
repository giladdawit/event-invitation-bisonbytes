#singly Linked List
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def __init__(self, node):
        self.headval = node

    def print_list(self):
        current_node = self.headval
        while current_node:
            print(current_node.dataval, end = "--> " if current_node.next else"\n")
            current_node = current_node.next

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.headval
        self.headval = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if not self.headval:
            self.headval = new_node
            return
        last_node = self.headval
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "The stack is empty"
        
#Singly Linked List is a type of Linked list where each Node in the list contains the 
#the address to the next node in the list it allows one way of traversal

#Doubly Linked List is a type of Linked list where each Node in the list contains the 
#the address to the next node and previous node in the list, it allows both forward and backward traversal
        
class Car:
    def __init__(self, type, mileage, max_speed):
        self.type = type
        self.mileage = mileage
        self.max_speed = max_speed
    
Car1 = Car("Tesla",10000, 250)
Car2 = Car("Hell Cat", 20000, 300)

print(f" {Car1.type} has {Car1.mileage:,} miles, and {Car1.max_speed:} max speed")
print(f" {Car2.type} has {Car2.mileage:,} miles, and {Car2.max_speed:} max speed")