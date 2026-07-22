#Linear Search
deserts = ["chocalate lava", "banana_cruse", "mangosirub", "applebun"]

def dessert_choose(deserts, target):
    for i, dessert in enumerate(deserts):
        if dessert == target:
            return i
    return -1



#Binary search
def guess_number(secret):
    low = 1
    high = 100

    while low <= high:
        mid = (low + high) // 2
        print(f"Guessing: {mid}")

        if mid == secret:
            print(f"I found it! The number is {mid}.")
            return

        elif mid < secret:
            print("Too low! Guessing higher.\n")
            low = mid + 1

        else:
            print("Too high! Guessing lower.\n")
            high = mid - 1

guess_number(77)


# 1. List Index
# Big-O: O(1) - Constant Time
# Explanation:
# Accessing an element by its index takes the same amount of
# time regardless of the size of the list.


numbers = [10, 20, 30, 40, 50]

print("1. List Index")
print(numbers[2])      # Output: 30



# 2. Single Loop
# Big-O: O(n) - Linear Time
# Explanation:
# The loop visits each element exactly once.
# If the list grows, the number of operations grows linearly.


print("\n2. Single Loop")

for number in numbers:
    print(number)



# 3. Nested Loop
# Big-O: O(n²) - Quadratic Time
# Explanation:
# For every element in the outer loop, the inner loop runs
# through the entire list again.

print("\n3. Nested Loop")

for i in numbers:
    for j in numbers:
        print(i, j)



# 4. Dictionary Lookup
# Big-O: O(1) - Constant Time (Average Case)
# Explanation:
# Python dictionaries use hash tables, allowing direct access
# to values by their keys.


students = {
    "Alazar": 90,
    "John": 85,
    "Sara": 95,
    "Helen": 88
}

print("\n4. Dictionary Lookup")

print(students["Sara"])



# 5. Binary Search
# Big-O: O(log n) - Logarithmic Time
# Explanation:
# Binary Search repeatedly divides the search space in half,
# making it much faster than checking every element.
# NOTE: The list MUST be sorted.


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

print("\n5. Binary Search")

result = binary_search(sorted_numbers, 23)

if result != -1:
    print(f"23 found at index {result}")
else:
    print("23 not found")



import time


# Create a list and a dictionary with 100,000 fake account numbers


accounts_list = []
accounts_dict = {}

for i in range(100000):
    account = f"ACC{i}"
    accounts_list.append(account)
    accounts_dict[account] = f"Customer {i}"

# The account we'll search for (near the end)
target = "ACC99999"


# List Lookup (Linear Search - O(n))
 

start = time.perf_counter()

for account in accounts_list:
    if account == target:
        break

end = time.perf_counter()

list_time = end - start

print("List Lookup")
print(f"Found: {target}")
print(f"Time: {list_time:.8f} seconds")


# Dictionary Lookup (Hash Table - O(1))


start = time.perf_counter()

customer = accounts_dict[target]

end = time.perf_counter()

dict_time = end - start

print("\nDictionary Lookup")
print(f"Found: {customer}")
print(f"Time: {dict_time:.8f} seconds")


# Stack Class
# A stack follows the LIFO principle:
# Last In, First Out


class Stack:
    def __init__(self):
        self.items = []

    # Add an item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Remove and return the top item
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    # Return the top item without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0



# Original List of Names

names = ["Alazar", "John", "Sara", "Helen", "Abel"]

print("Original List:")
print(names)


# Push all names onto the stack


stack = Stack()

for name in names:
    stack.push(name)


# Pop all names from the stack to reverse the list

reversed_names = []

while not stack.is_empty():
    reversed_names.append(stack.pop())

print("\nReversed List:")
print(reversed_names)
  
 
from collections import deque


# Create an empty queue


bank_queue = deque()


# Enqueue (Add) five customers

bank_queue.append("Alazar")
bank_queue.append("John")
bank_queue.append("Sara")
bank_queue.append("Helen")
bank_queue.append("Abel")

print("Customers waiting in line:")
print(bank_queue)


# Serve customers in the order they arrived


print("\nServing Customers:")

while bank_queue:
    customer = bank_queue.popleft()
    print(f"{customer} has been served.")

print("\nAll customers have been served.")

# Node Class
# Each node stores data and a reference to the next node.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the list
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print all nodes in the linked list
    def print_all(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")



# Test the Linked List


my_list = LinkedList()

my_list.push_front("Abel")
my_list.push_front("Helen")
my_list.push_front("Sara")
my_list.push_front("John")
my_list.push_front("Alazar")

print("Linked List:")
my_list.print_all()