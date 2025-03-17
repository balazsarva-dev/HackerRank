import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

MIN_YEAR = 1500
MAX_YEAR = 2025
MIN_TITLE_LENGTH = 3
MAX_TITLE_LENGTH = 50

def get_valid_number(prompt: str, min_value: int, max_value: int):
    """
    Prompts the user for a number within a specified range.
    """
    while True:
        try:
            number = int(input(prompt))
            if min_value <= number <= max_value:
                logger.info(f"Number entered: {number}")
                return number
            else:
                logger.warning(f"Please enter a number between {min_value} and {max_value}")

        except ValueError:
            logger.error("Invalid input. Please enter a number! ")
            
def add_painting(prompt: str, valid_key: int, result: dict) -> dict:
    """
    Adds a new painting to the result dictionary after validating the input.
    """
    while True:
        new_painting = input(prompt).split(',')
        if len(new_painting) == 2:
            title = new_painting[0].strip()
            date = new_painting[1].strip()
            
            if not (title.replace(" ", "").isalpha() and MIN_TITLE_LENGTH <= len(title) <= MAX_TITLE_LENGTH):
                logger.error('The title must be alphabetic and its length must be between %s and %s least 3 characters! Try again! ', MIN_TITLE_LENGTH, MAX_TITLE_LENGTH)
                continue
            
            try:
                date = int(new_painting[1])
                if not (MIN_YEAR <= date <= MAX_YEAR):
                    logger.error('Invalid date. Enter a date between 1500 and 2025!')
                    continue
                
                if any(title == painting[0] for painting in result.values()):
                    logger.error('The title already exists. Enter a new title!')
                    continue
                
                result[valid_key] = (title, str(date))
                logger.info(f'The new painting {result[valid_key]} has been added.')
                return result
            
            except ValueError: 
                logger.error('Invalid input. Try again.')
        else: 
            logger.error('Invalid input. Enter the title and the date of the painting! ')
            
def register_paintings(result: dict) -> dict:
    """
    Registers multiple paintings based on user input.
    """
    number_of_paintings_to_register = get_valid_number('Enter the number of paintings to register: ', 1, 10)
    for number in range(number_of_paintings_to_register):
        add_painting('Add new painting: ', number+1 if len(result) == 0 else max(result.keys()) + 1, result)
    
    logger.info('Paintings registered: ')
    return result

def sessions(iter_number: int) -> dict:
    """
    Runs multiple registration sessions.
    """
    result = dict()
    for i in range(iter_number):
        logger.info(f'Session registrations #{i+1} started')
        register_paintings(result)
        logger.info(f'Session registrations #{i+1} completed')
    return result

def main() -> None:
    """
    Main function to run the painting registration program.
    """
    registration_sessions = get_valid_number('Enter the number of sessions: ', 1, 5)
    logger.info(sessions(registration_sessions))
    
if __name__ == '__main__':
    main()