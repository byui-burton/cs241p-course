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

    # Base case: if the list has 1 we're done
    if len(items) <= 1:
        return

    # Break the list into halves
    middle = len(items) // 2
    part1 = items[:middle]
    part2 = items[middle:]

    # Recursively call this function to sort each half
    merge_sort(part1)
    merge_sort(part2)

    # Merge the two sorted parts
    i = 0 # iterator for part 1
    j = 0 # iterator for part 2
    k = 0 # iterator for complete list

    # As long as there are more items in each list
    while i < len(part1) and j < len(part2):
        # Get the smaller item from whichever part its in
        if part1[i] < part2[j]:
            items[k] = part1[i]
            i += 1
            k += 1
        else: # part2 <= part1
            items[k] = part2[j]
            j += 1
            k += 1

    # At this point, one or the other size is done

    # Copy any remaining items from part1
    while i < len(part1):
        items[k] = part1[i]
        i += 1
        k += 1

    # Copy any remaining items from part2
    while j < len(part2):
        items[k] = part2[j]
        j += 1
        k += 1

    # The list is now sorted!


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