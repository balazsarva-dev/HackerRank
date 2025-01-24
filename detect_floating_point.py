import re

# def valid_float_number_1(string: str) -> bool:
    
#     if string.count('.') != 1 or string[-1] == '.':
#         return False
    
#     elif string[0] == '.':
#         return bool(string[1:].isdigit())

#     elif string.startswith('+') or string.startswith('-'):
#         if string[1] == '.':
#             return bool(string[2:].isdigit())
#         else:
#             return bool(string[1:string.find('.')].isdigit() and string[string.find('.')+1:].isdigit())

#     elif string[0].isdigit():
#         return bool(string[:string.find('.')].isdigit() and string[string.find('.')+1:].isdigit())
#     else:
#         return False
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

def valid_float_number_3(string: str) -> bool:
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern, string))

if __name__ == '__main__':
    while True:
        T = int(input())
        if T in range(1, 10):
            break
    for _ in range(T):
        print(valid_float_number_2(input()))