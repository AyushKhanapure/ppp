class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative.")
    elif age > 120:
        raise CustomError("Invalid age: too old.")
    else:
        print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    validate_age(age)
except CustomError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input: Please enter a valid integer.")
