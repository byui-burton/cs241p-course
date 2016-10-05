"""
File: main.py
Author: Br. Burton

Tests the assignment and date classes.
"""

from assignment import Assignment

def main():
    a = Assignment()
    a.prompt()
    
    print()
    
    a.display()

if __name__ == "__main__":
    main()

