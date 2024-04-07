def print_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

if __name__ == "__main__":
    rows = 5  
    print("Pattern:")
    print_pattern(rows)
