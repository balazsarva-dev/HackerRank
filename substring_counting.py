def count_substring(main_string: str, sub_string: str) -> int:
    return sum(1 for i in range(len(main_string)-len(sub_string)+1) if main_string[i:len(sub_string)+i] == sub_string)

if __name__ == '__main__':
    string = input('String: ')
    sub_string = input('Substring: ')
    count = count_substring(string, sub_string)
    print(f'The "{sub_string}" substring in "{string}" string appears "{count}" time(s)')