# Function to convert words to numbers
def integers(word_list):
    number_list = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1_000_000
    }

    result = []

    for word in word_list:
        parts = word.split()
        total = 0
        current = 0

        for part in parts:
            if part in number_list:
                scale = number_list[part]
                if scale == 100:
                    current *= scale
                elif scale >= 1000:
                    total += current * scale
                    current = 0
                else:
                    current += scale

        total += current
        result.append(total)
    return result

# Stack implementation using a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node(None)
        self.size = 0   

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
    
    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    
    def maximum(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        max_value = self.head.next.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
    
    def minimum(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        min_value = self.head.next.value
        current = self.head.next
        while current:
            if current.value < min_value:
                min_value = current.value
            current = current.next
        return min_value

# Insert Numbers into the Stack
if __name__ == "__main__":
    words = ["one thousand", "fifty thousand", "three", "twenty thousand", "forty", "ten", "ten thousand"]
    numbers = integers(words)  

    stack = Stack()
    for number in numbers:
        stack.push(number) 

    print(f"Numbers in stack: {numbers}")
    print(f"Maximum value in stack: {stack.maximum()}")
    print(f"Minimum value in stack: {stack.minimum()}")

