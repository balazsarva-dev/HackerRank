from collections import Counter
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def migratoryBirds(arr):
    count_types_of_birds = Counter(arr)
    max_value = max(count_types_of_birds.values())
    result = min(key for key in count_types_of_birds if count_types_of_birds[key] == max_value)
    logger.info(f'Most common bird type: {result}')
    return result

def get_bird_sightings(min_val=1, max_val=99):
    while True:
        try:
            arr_count = int(input("Enter the number of bird sightings: ").strip())
            if min_val <= arr_count <= max_val:
                return arr_count
            logger.warning(f"RangeWarning: Please enter an integer between {min_val} and {max_val}.")
        except ValueError:
            logger.error(f"Invalid input! Please enter an integer.")

def main():
    number_of_observations = get_bird_sightings()
    bird_types = get_bird_types(number_of_observations)
    migratoryBirds(bird_types)

def get_bird_types(expected_length):
    while True:
        try:
            arr = list(map(int, input("Enter the bird types: ").rstrip().split()))
            if len(arr) == expected_length:
                return arr
            logger.warning(f"Invalid input! Please enter exactly {expected_length} integers.")
        except ValueError:
            logger.error("Invalid input! Please enter integers only.")

if __name__ == '__main__':
    main()