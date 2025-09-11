from collections import Counter
from typing import List
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_captain_room(room_number_list: List[int]) -> int:
    """Finds the captain's room number from a list of room numbers.
    Args:
        room_number_list (List[int]): A list of room numbers.
    Raises:
        ValueError: If no captain room is found.
    Returns:
        int: The captain's room number.
    """
    counting_numbers = Counter(room_number_list)
    for room_number, count in counting_numbers.items():
        if count == 1:
            return room_number
    raise ValueError('No captain room found! ')

def get_room_capacity(min_value: int, max_value: int) -> int:
    """Gets the maximum number of guests allowed in each room from user input.
    Args:
        min_value (int): The minimum allowed value.
        max_value (int): The maximum allowed value.
    """
    while True:
        try:
            K = int(input('Enter the max. number of people in each room! '))
            if K in range(min_value, max_value + 1):
                return K
        except ValueError:
            logger.error('Invalid input! Please enter an integer! ')

def _is_valid_room_list(room_number_list: List[int], K: int) -> bool:
    """Checks if the room number list is valid based on the given conditions.
    Args:
        room_number_list (List[int]): A list of room numbers.
        K (int): The maximum number of guests allowed in each room.
    Returns:
        bool: True if the list is valid, False otherwise.
    """
    counting_numbers = Counter(room_number_list)
    for count in counting_numbers.values():
        if count != 1 and count > K:
            return False
    return True

def main():
    """Main function to execute the program logic.
    Returns:
        int: The captain's room number.
    """
    K = get_room_capacity(2, 1000)
    while True:
        room_number_list = list(map(int, input("Enter room numbers separated by spaces: ").split()))
        if len(room_number_list) % K == 1:
            if not all(1 <= room_number <= 1000000 for room_number in room_number_list):
                logger.warning("Room numbers must be in the range [1, 10^6]. Please try again! ")
                continue
            if not _is_valid_room_list(room_number_list, K):
                logger.warning("The room number list is not valid, each room number must appear K times. Please try again! ")
                continue
            try:
                captain_room = find_captain_room(room_number_list)
                logger.info(f"{captain_room} ")
                return captain_room
            except ValueError as e:
                logger.error('The given room number list is not valid! Please try again! ')
        else:
            logger.warning("The list length is invalid. Every room must be filled with K guests except one. Please try again! ")
            continue

if __name__ == '__main__':
    main()