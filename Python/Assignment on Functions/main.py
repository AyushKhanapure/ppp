from module1 import greet, square
from module2 import calculate_average, cube

def main():
    print(greet("Rahul"))
    print("Square of 5:", square(5))
    
    numbers = [1, 2, 3, 4, 5]
    print("Average:", calculate_average(numbers))
    print("Cube of 3:", cube(3))

if __name__ == "__main__":
    main()
