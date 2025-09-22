from string import ascii_lowercase as chars
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f'Execution time for {func.__name__}: {end - start:.6f} seconds')
        return result
    return wrapper

@measure_time
def is_pangram_one(user_input: str) -> bool:
    return set(filter(lambda x: x in chars, user_input.lower())) == set(chars)

@measure_time
def is_pangram_two(user_input: str) -> bool:
    return {c for c in user_input if c in chars} == set(chars)

@measure_time
def is_pangram_three(user_input: str) -> bool:
    return set(chars).issubset(set(user_input.lower()))

@measure_time
def is_pangram_four(user_input: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if not user_input.lower().count(char):
            return False
    return True

def main():
    processes = [is_pangram_one, is_pangram_two, is_pangram_three, is_pangram_four]
    test = 'The quick brown fox jumps over the lazy dog.' * 100000
    for process in processes:
        logging.info(f'{process.__name__} result: {process(test)}')

if __name__ == '__main__':
    main()