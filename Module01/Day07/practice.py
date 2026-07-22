
# Day 07 Practice
# Data Structures & Big-O


import time
from collections import deque



# Exercise 1: Name the Big-O


print("Exercise 1 \n")

# O(1) - Constant Time
# Accessing an element by index takes the same time regardless
# of the list size.
numbers = [10, 20, 30, 40, 50]
print("List Index:", numbers[2])

# O(n) - Linear Time
# The loop visits every element once.
print("\nSingle Loop:")
for number in numbers:
    print(number)

# O(n²) - Quadratic Time
# Every element is compared with every other element.
print("\nNested Loop:")
for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        print(i, j)

# O(1) - Constant Time (Average)
# Dictionary lookup uses a hash table.
students = {
    "Alazar": 90,
    "Sara": 95,
    "John": 80
}

print("\nDictionary Lookup:")
print(students["Sara"])


# O(log n) - Logarithmic Time
# Binary search repeatedly halves the search range.

def binary_search(items, target):

    low = 0
    high = len(items) - 1

    while low <= high:

        mid = (low + high) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56]

print("\nBinary Search:")
print(binary_search(sorted_numbers, 23))



# Exercise 2: List vs Dict Lookup


print("\nExercise 2 \n")

accounts_list = []
accounts_dict = {}

for i in range(100000):
    account = f"ACC{i}"
    accounts_list.append(account)
    accounts_dict[account] = f"Customer {i}"

target = "ACC99999"

# List Lookup
start = time.perf_counter()

for account in accounts_list:
    if account == target:
        break

end = time.perf_counter()

print(f"List Lookup Time: {end - start:.8f} seconds")

# Dictionary Lookup
start = time.perf_counter()

customer = accounts_dict[target]

end = time.perf_counter()

print(f"Dictionary Lookup Time: {end - start:.8f} seconds")



# Exercise 3: Stack


print("\n Exercise 3 \n")


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]


names = ["Alazar", "John", "Sara", "Helen", "Abel"]

stack = Stack()

for name in names:
    stack.push(name)

reversed_names = []

while stack.items:
    reversed_names.append(stack.pop())

print("Original:", names)
print("Reversed:", reversed_names)



# Exercise 4: Queue


print("\n Exercise 4 \n")

bank_queue = deque()

bank_queue.append("Alazar")
bank_queue.append("John")
bank_queue.append("Sara")
bank_queue.append("Helen")
bank_queue.append("Abel")

print("Serving Customers:")

while bank_queue:
    customer = bank_queue.popleft()
    print(customer, "has been served.")



# Exercise 5: Singly Linked List


print("\n Exercise 5 \n")


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push_front(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def print_all(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


linked_list = LinkedList()

linked_list.push_front("Abel")
linked_list.push_front("Helen")
linked_list.push_front("Sara")
linked_list.push_front("John")
linked_list.push_front("Alazar")

print("Linked List:")
linked_list.print_all()