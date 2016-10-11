"""
File: check05b.py
Author: Br. Burton

Use this file to practice debugging in PyCharm.
"""

class Money:
    """
    Holds a dollars and cents value.
    """
    def __init__(self, dollars = 0, cents = 0):
        self.dollars = dollars
        self.cents = cents

    def add_cents(self, cents):
        self.cents += cents
        self.check_overflow()

    def check_overflow(self):
        if self.cents > 100:
            self.cents %= 100
            self.dollars += self.cents // 100

    def display(self):
        print("${}.{:02d}".format(self.dollars, self.cents))


def main():
    """
    The main function tests the Money class
    """
    account1 = Money(87, 15)
    account2 = Money(5, 5)
    account3 = Money(99, 99)

    # Display each account balance
    account1.display()
    account2.display()
    account3.display()

    # Now add 20 cents to each
    account1.add_cents(20)
    account2.add_cents(20)
    account3.add_cents(20)

    # Display each account balance again
    print()
    account1.display()
    account2.display()
    account3.display()


if __name__ == "__main__":
    main()