def print_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print(chr(65 + i), end="")
        if i > 0:
            print(" " * (2 * i - 1), end="")
            print(chr(65 + i), end="")
        print()

    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1), end="")
        print(chr(65 + i), end="")
        if i > 0:
            print(" " * (2 * i - 1), end="")
            print(chr(65 + i), end="")
        print()

if __name__ == "__main__":
    rows = 5  
    print("Pattern:")
    print_pattern(rows)
