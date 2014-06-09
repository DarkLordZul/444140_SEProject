"""Script which deals all the required printing"""
__author__ = 'Nicholas Branfield'


def print_array(title, arr, time_taken):
    """prints out name of algorithm as well as time taken in seconds"""
    print("{} took {:.10f} seconds".format(title, time_taken))
    for n in range(0, len(arr), 10):
        print("\t\t".join(map(str, arr[n:n + 10])))
    print("*"*114)


def print_table(times):
    """prints out formatted table of results containing algorithm names and timings"""
    print("Sorting of 10,000 integers using the following algorithms:\n")
    print("{:<15} {:<25}".format("Algorithm", "Time (seconds)"))
    print("--"*15)
    for i in range(0, 3):
        print("{:<15} {:<25.10f}".format(times["Algorithm"][i], times["Time (seconds)"][i]))
    print("--"*15)