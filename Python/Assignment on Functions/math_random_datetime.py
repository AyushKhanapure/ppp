import math
import random
import datetime

def main():
    print("Math module:")
    print("Square root of 16:", math.sqrt(16))
    print("Value of pi:", math.pi)
    print("Ceiling of 3.7:", math.ceil(3.7))
    print("Floor of 3.7:", math.floor(3.7))
    print()

    print("Random module:")
    print("Random integer between 1 and 10:", random.randint(1, 10))
    print("Random choice from a list:", random.choice(["apple", "banana", "cherry"]))
    print("Random floating point number between 0 and 1:", random.random())
    print()

    print("Datetime module:")
    current_time = datetime.datetime.now()
    print("Current date and time:", current_time)
    print("Current year:", current_time.year)
    print("Current month:", current_time.month)
    print("Current day:", current_time.day)

if __name__ == "__main__":
    main()
