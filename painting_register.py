import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_valid_number(prompt: str, min_value: int, max_value: int):
    while True:
        try:
            number = int(input(prompt))
            if min_value <= number <= max_value:
                logger.info(f"Number entered: {number}")
                return number
            else: logger.warning(f"Please enter a number between {min_value} and {max_value}")
        except ValueError: logger.error("Invalid input. Please enter a number! ")
            
def add_painting(prompt: str, valid_key: int, result: dict) -> dict:
    while True:
        new_painting = input(prompt).split(',')
        if len(new_painting) == 2:
            title = new_painting[0]
            if not title.isalpha() and len(title) < 3:
                logger.error('The title must be alphabetic and at least 3 characters! Try again! ')
                continue
            try:
                date = int(new_painting[1])
                if date < 1500 or date > 2025:
                    logger.error('Invalid date. Enter a date between 1500 and 2025!')
                    continue
                if len(result) > 0 and title in [painting[0] for painting in result.values()]:
                    logger.error('The title already exists. Enter a new title!')
                    continue
                result[valid_key] = tuple(new_painting)
                logger.info(f'The new painting {result[valid_key]} has been added.')
                return result
            except ValueError: logger.error('Invalid input. Try again.')
        else: logger.error('Invalid input. Enter the title and the date of the painting! ')
            
def register_paintings(result: dict) -> dict:
    number_of_paintings_to_register = get_valid_number('Enter the number of paintings to register: ', 1, 10)
    for number in range(number_of_paintings_to_register):
        add_painting('Add new painting: ', number+1 if len(result) == 0 else max(result.keys()) + 1, result)
    logger.info('Paintings registered: ')
    return result

def sessions(iter_number: int) -> dict:
    result = dict()
    for i in range(iter_number):
        logger.info(f'Session registrations #{i+1} started')
        register_paintings(result)
        logger.info(f'Session registrations #{i+1} completed')
    return result

def main() -> None:
    registration_sessions = get_valid_number('Enter the number of sessions: ', 1, 5)
    logger.info(sessions(registration_sessions))
    
if __name__ == '__main__':
    main()