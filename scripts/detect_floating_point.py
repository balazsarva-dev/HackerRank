import re

def valid_float_number_2(string: str) -> bool:
    # Basic validation
    if not string or string.count('.') != 1:
        return False
    # Split into parts
    left, right = string.split('.')
    # Empty decimal part or just a dot
    if not right:
        return False
    # Handle signs
    if left and left[0] in '+-':
        left = left[1:]
    # Validate both parts are digits
    return (not left or left.isdigit()) and right.isdigit()

def valid_float_number(string: str) -> bool:
    """
    Validates if the given string is a valid floating-point number.

    :param string: The string to validate.
    :return: True if the string is a valid floating-point number, False otherwise.
    """
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern, string))

def main():
    """
    Main function to validate multiple floating-point numbers.
    """
    T = int(input("Enter the number of test cases (1-9): "))
    if not (1 <= T <= 9):
        raise ValueError("The number of test cases must be between 1 and 9.")
    
    for _ in range(T):
        test_string = input("Enter a string to validate: ")
        print(valid_float_number(test_string))

if __name__ == '__main__':
    main()