"""Script involves running the various algorithms over an array of 10 000 integers and tabulating resulting timings"""
from Sorts.ArrayUtilities import gen_array, permute_array
from Sorts.Printing import print_table
from Sorts.Algorithms import heap_sort, bubble_sort
from timeit import default_timer as timer

from numpy import sort as quick_sort

__author__ = 'Nicholas Branfield'


def tabulate_timings(self):
    times = {"Algorithm": ["quickSort", "heapSort", "bubbleSort"], "Time (seconds)": [0.0, 0.0, 0.0]}

    size = 10000
    a = gen_array(size)

    start = timer()
    a = quick_sort(a)
    time_taken = timer() - start
    times["Time (seconds)"][0] = time_taken

    a = permute_array(a)

    start = timer()
    a = heap_sort(a)
    time_taken = timer() - start
    times["Time (seconds)"][1] = time_taken

    a = permute_array(a)

    start = timer()
    a = bubble_sort(a)
    time_taken = timer() - start
    times["Time (seconds)"][2] = time_taken

    print_table(times)