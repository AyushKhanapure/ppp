def key_exists(dictionary, key):
    return key in dictionary

def iterate_dictionary(dictionary):
    for key, value in dictionary.items():
        print("Key:", key, ", Value:", value)

def concatenate_dictionaries(dict1, dict2):
    concatenated_dict = dict1.copy()
    concatenated_dict.update(dict2)
    return concatenated_dict

def sum_dictionary_values(dictionary):
    return sum(dictionary.values())

def max_min_values(dictionary):
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    return max_value, min_value

my_dict = {'a': 10, 'b': 20, 'c': 30}
print("Original Dictionary:", my_dict)

key_to_check = 'b'
print("Does key '{}' exist in the dictionary? {}".format(key_to_check, key_exists(my_dict, key_to_check)))

print("Iterating over dictionary items:")
iterate_dictionary(my_dict)

dict2 = {'d': 40, 'e': 50}
concatenated_dict = concatenate_dictionaries(my_dict, dict2)
print("Concatenated Dictionary:", concatenated_dict)

sum_values = sum_dictionary_values(my_dict)
print("Sum of dictionary values:", sum_values)

max_value, min_value = max_min_values(my_dict)
print("Maximum value in the dictionary:", max_value)
print("Minimum value in the dictionary:", min_value)
