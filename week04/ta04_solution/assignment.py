"""
File: assignment.py
Author: Br. Burton

Defines a simple assignment class with a name and three dates.
"""

from date import Date

class Assignment:
    def __init__(self):
        self.name = ""
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()

    def prompt(self):
        self.name = input("Name: ")
        
        print("\nStart Date:")
        self.start_date.prompt()

        print("\nDue Date:")
        self.due_date.prompt()

        print("\nEnd Date:")
        self.end_date.prompt()

    def display(self):
        print("Assignment: {}".format(self.name))

        print("Start Date:")
        self.start_date.display()

        print("Due Date:")
        self.due_date.display()

        print("End Date:")
        self.end_date.display()


