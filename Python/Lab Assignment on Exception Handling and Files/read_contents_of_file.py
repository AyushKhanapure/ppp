def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_characters(file_content):
    return len(file_content)

def count_vowels(file_content):
    vowels = "aeiouAEIOU"
    return sum(1 for char in file_content if char in vowels)

def count_lines(file_content):
    return file_content.count('\n') + 1

def reverse_words(file_content):
    words = file_content.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def main():
    
    try:
        with open("test.txt", 'r') as file:
            content = file.read()
            
            # a) display number of words
            num_words = count_words(content)
            print("Number of words:", num_words)
            
            # b) display number of characters
            num_chars = count_characters(content)
            print("Number of characters:", num_chars)
            
            # c) display number of vowels
            num_vowels = count_vowels(content)
            print("Number of vowels:", num_vowels)
            
            # d) display number of lines
            num_lines = count_lines(content)
            print("Number of lines:", num_lines)
            
            # e) reverse each word and display it
            reversed_content = reverse_words(content)
            print("Reversed words:", reversed_content)
    
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()
