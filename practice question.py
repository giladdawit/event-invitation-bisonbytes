class Node:
    """Class representing a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

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
        else:
            return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

def is_balanced(string):
    """Check if the brackets in the string are balanced."""
    stack = Stack()
    opening_brackets = '([{'
    closing_brackets = ')]}'
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in opening_brackets:
            stack.push(char)  # Push opening brackets onto the stack
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != matching_bracket[char]:
                return False  # Unmatched closing bracket found

    return stack.is_empty()  # Return True if all brackets are matched

# Test cases
print(is_balanced("()"))          # True
print(is_balanced("([])"))        # True
print(is_balanced("{[()]}"))      # True
print(is_balanced("{[(])}"))      # False
print(is_balanced("{[}"))         # False
print(is_balanced("((()))"))      # True
print(is_balanced(""))             # True (empty string is balanced)
