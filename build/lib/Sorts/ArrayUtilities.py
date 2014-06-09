__author__ = 'Nicholas Branfield'
"""This script contains functions which create the initial array and "re-randomize" an array"""


def permute_array(arr):
    """randomly shuffles elements in array - generating a new ordering of the same data"""
    import random

    random.shuffle(arr)
    return arr


def gen_array(size):
    """creates initial array of parsed size - using randomly generated numbers between 1 and 65536"""
    import random
    return [random.randint(1, 65536) for _ in range(size)]
