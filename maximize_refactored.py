from itertools import product
from typing import Callable, Generator
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_valid_input(prompt: str, condition: Callable = None) -> Generator[int, None, None]:
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if condition is None or condition(values):
                yield from values
                return
            logger.warning("Invalid input. Try again!")
        except ValueError:
            logger.error("Only integers are allowed! Try again!")

def process_list(K: int, M: int) -> Generator[int, None, None]:
    result = []
    for i in range(K):
        condition = lambda x: all([len(x) == 1 + x[0], 1 <= x[0] <= 7, all(1 <= v <= 10**9 for v in x[1:])])
        prompt = f"Integers (length of the list (1-7), then the values (1-10**9)) for list {i+1} : "
        values = list(get_valid_input(prompt, condition))
        result.append(values[1:])
    for combo in product(*result):
        yield sum((x**2) % M for x in combo) % M

def main() -> None:
    condition = lambda x: all([len(x) == 2, 1 <= x[0] <= 7, 1 <= x[1] <= 1000])
    prompt = "Enter the values of K (1-7) and M (1-1000): "
    K, M = list(get_valid_input(prompt, condition))
    max_value = max(process_list(K, M))
    logger.info(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()
    
# from itertools import product
# from typing import Callable, Generator


# def get_valid_input(prompt: str | None, condition: Callable = None) -> Generator[int, None, None]:
#     while True:
#         try:
#             values = list(map(int, input(prompt).split() if prompt else input().split()))
#             if condition is None or condition(values):
#                 yield from values
#                 return
#             print("Invalid input. Try again!")
#         except ValueError:
#             print("Only integers are allowed! Try again!")

# def process_list(K: int, M: int) -> Generator[int, None, None]:
#     result = []
#     for i in range(K):
#         condition = lambda x: all([len(x) == 1 + x[0], 1 <= x[0] <= 7, all(1 <= v <= 10**9 for v in x[1:])])
#         values = list(get_valid_input(prompt=None, condition=condition))
#         result.append(values[1:])
#     for combo in product(*result):
#         yield sum((x**2) % M for x in combo) % M

# def main() -> None:
#     condition = lambda x: all([len(x) == 2, 1 <= x[0] <= 7, 1 <= x[1] <= 1000])
#     K, M = list(get_valid_input(prompt=None, condition=condition))
#     max_value = max(process_list(K, M))
#     print(max_value)
    

# if __name__ == "__main__":
#     main()
