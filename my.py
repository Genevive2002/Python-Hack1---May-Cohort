# 1. Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = list(s)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# 2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x: int):
        self.stack1.append(x)
    
    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        return self.stack2.pop()

# 3. Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value: int):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def find_max(self) -> int:
        if not self.head:
            raise ValueError("Linked list is empty")
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

# Example usages

# Reverse a string
print(reverse_string("hello"))  # Output: "olleh"

# Queue operations
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2

# Linked list operations
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
