"""
File: ta08-solution.py
Author: Br. Burton

Demonstrates inheritance and polymorphism.
"""
class Time:
    """
    Represents a time of day (hours, minutes, seconds).
    """

    def __init__(self):
        """
        Initializes the time to be 0:00:00
        """
        self._hours = 0
        self._minutes = 0
        self._seconds = 0

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def set_hours(self, hours):
        if hours > 23:
            hours = 23
        elif hours < 0:
            hours = 0

        self._hours = hours

    def set_minutes(self, minutes):
        if minutes > 59:
            minutes = 59
        elif minutes < 0:
            minutes = 0

        self._minutes = minutes

    def set_seconds(self, seconds):
        if seconds > 59:
            seconds = 59
        elif seconds < 0:
            seconds = 0

        self._seconds = seconds

    hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)


def main():
    """
    Tests the time class.
    """
    time = Time()

    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    time.hours = hours
    time.minutes = minutes
    time.seconds = seconds

    print("The time is:")
    print("Hours: {}".format(time.hours))
    print("Minutes: {}".format(time.minutes))
    print("Seconds: {}".format(time.seconds))

if __name__ == "__main__":
    main()