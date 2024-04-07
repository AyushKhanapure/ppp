def print_first_10_natural_numbers():
    print("First 10 natural numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

def print_first_10_even_numbers_reverse():
    print("First 10 even numbers in reverse order:")
    for i in range(20, 0, -2):
        print(i, end=" ")
    print()

def print_table_of_number():
    num = int(input("Enter a number to print its table: "))
    print("Table of", num, ":")
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_10_prime_numbers():
    print("First 10 prime numbers:")
    count = 0
    num = 2
    while count < 10:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()

def sum_of_digits_in_range():
    print("Sum of digits of numbers from 101 to 130:")
    total_sum = 0
    for num in range(101, 131):
        total_sum += sum(int(digit) for digit in str(num))
    print(total_sum)

if __name__ == "__main__":
    print_first_10_natural_numbers()
    print_first_10_even_numbers_reverse()
    print_table_of_number()
    print_first_10_prime_numbers()
    sum_of_digits_in_range()
