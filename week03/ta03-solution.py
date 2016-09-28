"""
File: ta03-solution.py
Author: Br. Burton

This file contains a Rational class to hold fractions and
demonstrates their basic functions.
"""

class Rational:
    """
    The Rational class stores a rational number (i.e., fraction)
    in the form of a top and bottom number.
    """
    def __init__(self):
        """
        Initializes the number to 0/1
        """
        self.top = 0
        self.bottom = 1

    def prompt(self):
        """
        Asks the user for a numerator and denominator and saves them
        """
        # Some error checking here would be nice...
        self.top = int(input("Enter the numerator: "))
        self.bottom = int(input("Enter the denominator: "))

    def display(self):
        """
        Displays the number in the format "top/bottom"
        """
        print("{}/{}".format(self.top, self.bottom))

    def display_decimal(self):
        """
        Displays the number in the format "0.75" for 3/4
        """

        # Note that Python 3 by default will do floating point
        # division instead of integer division like Python 2 or C++
        print(self.top/self.bottom)


def main():
    """
    Tests the Rational number class.
    """
    # Create a new rational number
    fraction = Rational()

    # Display the default value
    fraction.display()

    # Prompt the user for their values
    fraction.prompt()

    # Display the new number in both formats
    fraction.display()
    fraction.display_decimal()


# If this is the file being run, call our main function
if __name__ == "__main__":
    main()