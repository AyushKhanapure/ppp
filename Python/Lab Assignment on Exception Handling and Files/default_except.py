def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError:
        print("Error: Invalid input!")
    except:
        print("An unexpected error occurred!") 
    else:
        print("Result:", result)
    finally:
        print("Finally block executed.")

print("Test Case 1:")
divide(10, 2)

print("\nTest Case 2:")
divide(10, 0)

print("\nTest Case 3:")
divide(10, 'a')
