from collections import Counter
from typing import List
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_captain_room(room_number_list: List[int]) -> int:
    counting_numbers = Counter(room_number_list)
    for room_number, count in counting_numbers.items():
        if count == 1:
            return room_number
    raise ValueError('No captain room found! ')

def get_room_capacity(min_value: int, max_value: int) -> int:
    while True:
        try:
            K = int(input('Enter the max. number of people in each room! '))
            if K in range(min_value, max_value + 1):
                return K
        except ValueError:
            logger.error('Invalid input! Please enter an integer! ')

def is_valid_room_list(room_number_list: List[int], K: int) -> bool:
    counting_numbers = Counter(room_number_list)
    for count in counting_numbers.values():
        if count != 1 and count > K:
            return False
    return True

def get_room_numbers():
    K = get_room_capacity(2, 1000)
    while True:
        room_number_list = input("Enter room numbers separated by spaces: ").split()
        try:
            room_number_list = list(map(int, room_number_list))
            if len(room_number_list) % K == 1:
                if not all(1 <= room_number <= 1000000 for room_number in room_number_list):
                    logger.warning("Room numbers must be in the range [1, 10^6]. Please try again! ")
                    continue
                if not is_valid_room_list(room_number_list, K):
                    logger.warning("The room number list is not valid, each room number must appear K times. Please try again! ")
                    continue
            return room_number_list
        except ValueError:
            logger.error('Invalid input! Please enter integers only! ')

def get_captain_room():
    room_number_list = get_room_numbers()
    try:
        captain_room = find_captain_room(room_number_list)
        logger.info(f'The captain room number is: {captain_room} ')
        return captain_room
    except ValueError as e:
        logger.error('No captain room found! ')
        return None

def test_run():
    test_cases = [
        (['apple', '12', 'apple', '13', '12', '13', '14'], 14),
        ([1, 2, 3, 2, 1, 4, 3, 4, 5, 5, 6, 6, 7], 7),
        ([10, 20, 10, 30, 20, 30, 40], 40),
        ([5, 5, 5, 5, 1], 1),
        ([1000000, 999999, 1000000, 999998, 999999], 999998),
    ]
    for i, (room_list, expected) in enumerate(test_cases):
        try:
            result = find_captain_room(room_list)
            assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
            logger.info(f"Test case {i+1} passed! ")
        except Exception as e:
            logger.error(f"Test case {i+1} failed with exception: {e} ")

def main():
    get_captain_room()
    
if __name__ == '__main__':
    main()