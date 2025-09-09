import operator
from typing import List, Optional
import sys 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class Valid:
    number_of_instances = 0
    
    def set_a_number(self, prompt: str, min_value: int, max_value: int, input_value: Optional[str] = None) -> None:
        """
        Request a valid integer input within a specified range.
        :param prompt: The message to display to the user.
        :param min_value: The minimum acceptable integer (inclusive).
        :param max_value: The maximum acceptable integer (inclusive).
        :param input_value: Optional string input for testing purposes.
        """
        Valid.number_of_instances += 1
        while True:
            try:
                valid_number = int(input_value if input_value is not None else input(prompt))
                if valid_number in range(min_value, max_value+1):
                    self._number = valid_number
                    return
                logger.error(f'Out of range! Enter a number from {min_value} to {max_value}! ')
            except ValueError:
                logger.critical('Missing or invalid input! Only integer is allowed! ')
    
    def get_a_number(self) -> int:
        return self._number
    
    def set_a_list(self, prompt: str, length: int, min_value: int, max_value: int, input_values: Optional[str] = None) -> None:
        """
        Request a list of integers of specified length within a given range.
        :param prompt: The message to display to the user.
        :param length: The required length of the list.
        :param min_value: The minimum acceptable integer (inclusive).
        :param max_value: The maximum acceptable integer (inclusive).
        :param input_values: Optional string input for testing purposes.
        """
        Valid.number_of_instances += 1
        while True:
            values = (input_values if input_values is not None else input(prompt)).split()
            try:
                result = list(map(int, values))
                if len(result) == length and all(min_value <= value <= max_value for value in result):
                    self._final = result
                    return
                elif len(result) != length:
                    logger.error(f'Invalid number of elements! It must contain {length} values! Try again! ')
                else:
                    logger.error(f'Values are out of range! They must be between {min_value} and {max_value}')
            except ValueError:
                logger.critical('Invalid or missing input! Only integer is allowed! Try again! ')

    def get_a_list(self) -> List[int]:
        return self._final

    def set_a_string(self, prompt, *args) -> None:
        """Request a string input from the user, ensuring it is one of the allowed values.
        :param prompt: The message to display to the user.
        :param args: The acceptable string values."""
        while True:
            value = input(prompt)
            if value in args:
                self._string = value
                return
            
    def get_a_string(self) -> str:
        return self._string

class Process:
    def __init__(self) -> None:
        self.valid = Valid()
    
    def ask_to_play(self) -> bool:
        self.valid.set_a_string('Do you want to play? (yes/no) ', 'yes', 'no')
        return self.valid.get_a_string() == 'yes'
    
    def settings(self) -> None:
        """
        Set up the number of athletes, attributes, and the sorting attribute index.
        """
        self.valid.set_a_number('Enter the number of athletes (2-1000): ', 1, 1000)
        self.athletes = self.valid.get_a_number()
        self.valid.set_a_number('Enter the number of attributes (0-1000): ', 1, 1000)
        self.attributes = self.valid.get_a_number()
        self.arr = []
        for _ in range(self.athletes):
            self.valid.set_a_list('Enter the attributes! ', self.attributes, 0, 1000)
            self.arr.append(self.valid.get_a_list())
        self.valid.set_a_number('Enter the attribute to sort by! ', 0, self.attributes-1)
        self.k = self.valid.get_a_number()
        
    def main(self) -> None:
        self.settings()
        sorted_athletes = sorted(self.arr, key=operator.itemgetter(self.k))
        return sorted_athletes

if __name__ == '__main__':
    process = Process()
    if process.ask_to_play():
        sorted_athletes = process.main()
        for athlete in sorted_athletes:
            logger.info(' '.join(map(str, athlete)))