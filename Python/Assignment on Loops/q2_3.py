def print_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        for j in range(i + 1):
            if j == 0 or j == i:
                print("1", end=" ")
            else:
                print(combination(i, j), end=" ")
        print()

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    rows = 6  
    print("Pattern:")
    print_pattern(rows)
