def reverse_string(s):
    return s[::-1]

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = len(s) - vowel_count
    return vowel_count, consonant_count

def count_letters_in_word(word):
    return len(word)

def convert_case(s):
    return s.swapcase()

def count_character_types(s):
    lower_count = sum(1 for char in s if char.islower())
    upper_count = sum(1 for char in s if char.isupper())
    numeric_count = sum(1 for char in s if char.isnumeric())
    special_count = len(s) - (lower_count + upper_count + numeric_count)
    return lower_count, upper_count, numeric_count, special_count

my_string = "Hello, World! 123"
print("Original String:", my_string)

print("Reversed String:", reverse_string(my_string))

vowel_count, consonant_count = count_vowels_consonants(my_string)
print("Vowel count:", vowel_count)
print("Consonant count:", consonant_count)

word = "Hello"
print("Number of letters in the word '{}': {}".format(word, count_letters_in_word(word)))

print("String after case conversion:", convert_case(my_string))

lower_count, upper_count, numeric_count, special_count = count_character_types(my_string)
print("Lowercase characters count:", lower_count)
print("Uppercase characters count:", upper_count)
print("Numeric characters count:", numeric_count)
print("Special characters count:", special_count)
