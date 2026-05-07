"""
Implement a heap sort algorithm to sort any list
example  : [5,6,2,9,10,1,25]
output : [1,2,5,6,9,10,25]
"""


def heapsort(lst):
    # Build max heap from bottom up
    for i in range(len(lst)//2 - 1, -1, -1):
        shiftDown(lst, i, len(lst))
    # Extract max element one by one
    for i in range(len(lst)-1, 0, -1):
        swap(lst, 0, i)  # Move max to end
        shiftDown(lst, 0, i)  # Restore heap property
    return lst

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def shiftDown(lst, i, upper):
    while True:
        left, right = i*2+1, i*2+2
        largest = i
        # Check if left child is larger
        if left < upper and lst[left] > lst[largest]:
            largest = left
        # Check if right child is larger
        if right < upper and lst[right] > lst[largest]:
            largest = right
        # If parent is largest, heap property satisfied
        if largest == i:
            break
        # Swap and continue down the tree
        swap(lst, i, largest)
        i = largest

