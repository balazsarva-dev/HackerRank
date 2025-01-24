from typing import Tuple
import logging
import sys
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def split_string(s: str) -> Tuple[str]:
    hour, minute, second = s.split(':')
    sec, am_pm = second[:2], second[2:]
    return hour, minute, sec, am_pm

def timeConversion(strings_of_a_tuple: Tuple[str]) -> str:
    hour, minute, sec, am_pm = strings_of_a_tuple
    if am_pm == 'AM':
        if hour == '12':
            hour = '00'
    elif am_pm == 'PM':
        if hour in [f'0{str(_)}' for _ in range(10)]:
            hour = int(hour[-1]) + 12
        elif hour in ['10', '11']:
            hour = int(hour) + 12     
    return f'{hour}:{minute}:{sec}'

def valid_time_input(s: str) -> bool:
    return bool(re.match(r'^[0-1][0-9]:[0-5][0-9]:[0-5][0-9][AP]M$', s))

def get_valid_time_input(prompt: str) -> str:
    while True:
        s = input(prompt)
        if valid_time_input(s):
            return s
        else:
            logger.error('Invalid input! Try again! ')
def main():
    logger.debug('Enter a time in 12-hour format: ')
    input_time = get_valid_time_input('')
    splitted_s = split_string(input_time)
    time_conversion = timeConversion(splitted_s)
    return time_conversion
    
if __name__ == '__main__':
    logger.info(main())