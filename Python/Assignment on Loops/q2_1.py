def print_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

if __name__ == "__main__":
    rows = 5 
    print("Pattern:")
    print_pattern(rows)
