"""
File: ta10-solution.py
Author: Br. Burton

This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    pass


def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()