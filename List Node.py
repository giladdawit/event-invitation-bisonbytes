class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def set_head(self, node):
        self.headval = node
    
    def print_list(self):
        current_node = self.headval
        while current_node:
            print(current_node.dataval, end= "--> " if current_node.next else "\n")
            current_node = current_node.next

list1 = SLinkedList()

list1.headval = Node("Mon")
list1.headval.next = Node("Tue")

list1.print_list()

class Node:
    """Class representing a single node in the stack."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class Stack:
    """Class implementing a stack using a singly linked list."""
    def __init__(self):
        self.top = None  # Initialize the top of the stack to None

    def push(self, item):
        """Add an item to the top of the stack."""
        new_node = Node(item)  # Create a new node
        new_node.next = self.top  # Point new node to the current top
        self.top = new_node  # Update the top to the new node

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            popped_node = self.top  # Get the top node
            self.top = self.top.next  # Move the top pointer to the next node
            return popped_node.data  # Return the data of the popped node
        return "Stack is empty"

    def peek(self):
        """Get the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.top.data  # Return the top data
        return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display the contents of the stack."""
        current_node = self.top
        stack_items = []
        while current_node:
            stack_items.append(current_node.data)
            current_node = current_node.next
        print("Stack (top to bottom):", " -> ".join(map(str, stack_items)))

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.display()  # Output: Stack (top to bottom): 30 -> 20 -> 10

    print("Top element:", stack.peek())  # Output: Top element: 30

    print("Popped element:", stack.pop())  # Output: Popped element: 30
    stack.display()  # Output: Stack (top to bottom): 20 -> 10

    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

    stack.pop()  # Remove 20
    stack.pop()  # Remove 10
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True
