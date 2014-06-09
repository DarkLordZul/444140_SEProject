__author__ = 'Nicholas Branfield'
"""Script containing source code for the 2 sorting algorithms"""


def heap_sort(arr):
    """Repeatedly scan and remove the maximal element from the heap; building a sorted list from back to front"""
    for start in range((len(arr) - 2) // 2, -1, -1):
        siftdown(arr, start, len(arr) - 1)

    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)
    return arr


def siftdown(arr, start, end):
    """Heap (layout of a binary tree) is built out of initial array"""
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def bubble_sort(arr):
    """Loops through array (arr) comparing each pair of adjacent items and swapping them if they are not in order"""
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr