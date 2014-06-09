"""testing of Sorts package are carried out here"""
from Sorts.ArrayUtilities import gen_array, permute_array
from Sorts.Printing import print_array
from Sorts.Algorithms import heap_sort, bubble_sort
from timeit import default_timer as timer

import unittest
from numpy import sort as quick_sort

__author__ = 'Nicholas Branfield'


class TestProg(unittest.TestCase):
    """in each case a is set up with random numbers, sorted with one algorithm and then compared with a sorted_a"""
    """sorted_a generated using native python function as to not bias test results by using a algorithm to be tested"""
    a = list()
    sorted_a = list()

    def setUp(self):
        global a, sorted_a
        start = timer()
        size = 100
        a = gen_array(size)
        time_taken = timer() - start
        print_array("Original set", a, time_taken)

        start = timer()
        sorted_a = sorted(a)
        time_taken = timer() - start
        print_array("Sorted array - will be tested against", sorted_a, time_taken)

    def test_quick_sort(self):
        global a, sorted_a
        start = timer()
        a = quick_sort(a)
        time_taken = timer() - start
        print_array("Quick Sort", a, time_taken)
        self.assertListEqual(a.tolist(), sorted_a)

    def test_heap_sort(self):
        global a, sorted_a
        a = permute_array(a)

        start = timer()
        a = heap_sort(a)
        time_taken = timer() - start
        print_array("Heap Sort", a, time_taken)
        self.assertEqual(a, sorted_a)

    def test_bubble_sort(self):
        global a, sorted_a
        a = permute_array(a)

        start = timer()
        a = bubble_sort(a)
        time_taken = timer() - start
        print_array("Bubble Sort", a, time_taken)

        self.assertEqual(a, sorted_a)

if __name__ == '__main__':
    unittest.main()
