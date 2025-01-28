from itertools import product
from typing import Callable, Generator

def get_valid_input(prompt: str, condition: Callable | None) -> Generator[int, None, None]:
    """Get validated integer input from user.

    Args:
        prompt (str): Message to display for user input
        condition (Callable | None): Validation function or None for no validation

    Yields:
        int: Valid integer values from user input

    Example:
        >>> condition = lambda x: all([len(x) == 2, 1 <= x[0] <= 7])
        >>> values = list(get_valid_input("Enter two numbers: ", condition))
    """
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if condition is None or condition(values):
                yield from values
                return
            print("Invalid input. Try again!")
        except ValueError: print("Only integers are allowed! Try again!")

def process_list(K: int, M: int) -> Generator[int, None, None]:
    """Process K lists of integers and generate modulo M results.

    Args:
        K (int): Number of lists to process (1-7)
        M (int): Modulo value for calculations (1-1000)

    Yields:
        int: Sum of squares modulo M for each combination

    Example:
        >>> max_value = max(process_list(2, 1000))
    """
    result = []
    for i in range(K):
        condition = lambda x: all([len(x) == 1 + x[0], 1 <= x[0] <= 7, all(1 <= v <= 10**9 for v in x[1:])])
        prompt = f"Integers (length of the list (1-7), then the values (1-10**9)) for list {i+1} : "
        values = list(get_valid_input(prompt, condition))
        result.append(values[1:])
    for combo in product(*result):
        yield sum(x**2 for x in combo) % M

def main() -> None:
    """Main function for running the program."""
    condition = lambda x: all([len(x) == 2, 1 <= x[0] <= 7, 1 <= x[1] <= 1000])
    prompt = "Enter the values of K (1-7) and M (1-1000): "
    K, M = list(get_valid_input(prompt, condition))
    max_value = max(process_list(K, M))
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()