from itertools import combinations

def validate_input(prompt: str, min_value: int, max_value: int) -> int:
    """Validates and returns an integer input within a specified range."""
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Value must be between {min_value} and {max_value}. Please try again.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

def generate_combinations(S: str, k: int):
    """Generates and prints combinations for all lengths up to k."""
    for i in range(1, k + 1):
        for combination in combinations(sorted(S), i):
            print(''.join(combination))

def main():
    S = input("Enter a string: ").upper()
    k = validate_input(f"Enter the maximum size of combinations (1-{len(S)}): ", 1, len(S))
    generate_combinations(S, k)

if __name__ == '__main__':
    main()