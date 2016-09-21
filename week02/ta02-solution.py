"""
File: ta02-solution.py
Author: Br. Burton

Description:
    This program counts the occurrences of the word "pride"
    in a text file.

    It is not sophisticated, and there are better solutions,
    but it provides a simple look at basic file parsing.
"""


def prompt_filename():
    """
    Asks the user for a filename

    Returns:
        The filename
    """
    filename = input("Please enter the filename: ")
    return filename


def parse_file(filename):
    """
    Parses a file and counts the occurrences of the word "pride"

    Args:
        filename: The file to be parsed

    Returns:
        The number of occurrences
    """
    count = 0

    # this is a super cool way to open a file, so it will automatically
    # be closed / cleaned up when needed
    with open(filename) as f:
        # go through each line in the file, one by one
        for line in f:
            # split the line into words based on space (the default delimiter)
            words = line.split()

            # go through each word and see if it matches
            # (yes there are more clever ways to do this...)
            for word in words:
                if word == "pride":
                    count += 1

    return count


def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    filename = prompt_filename()
    print("Opening file '{}'".format(filename))

    count = parse_file(filename)
    print("The word pride occurs {} times in this file.".format(count))


# Check if this is the main program being run and if so, call main()
if __name__ == "__main__":
    main()