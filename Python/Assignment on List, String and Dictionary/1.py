def sum_list(lst):
    return sum(lst)

def get_largest_number(lst):
    return max(lst)

def remove_duplicates(lst):
    return list(set(lst))

def separate_positive_negative(lst):
    positive_numbers = [num for num in lst if num > 0]
    negative_numbers = [num for num in lst if num < 0]
    return positive_numbers, negative_numbers

def filter_even_odd(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    odd_numbers = [num for num in lst if num % 2 != 0]
    return even_numbers, odd_numbers

my_list = [3, 1, 5, 2, 5, 2, -7, -2, 4, -1, 6]
print("Original List:", my_list)

print("Sum of the list:", sum_list(my_list))

print("Largest number in the list:", get_largest_number(my_list))

print("List after removing duplicates:", remove_duplicates(my_list))

positive_numbers, negative_numbers = separate_positive_negative(my_list)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)

even_numbers, odd_numbers = filter_even_odd(my_list)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
