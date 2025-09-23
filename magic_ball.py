import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_name() -> str:
    while True:
        name = input("Enter your name: ")
        if len(name) < 3:
            logger.warning("Name must be longer than 3 characters.")
        elif name.isalpha() is False:
            logger.warning("Name must contain only letters.")
        else:
            return name.title()

def get_questions_answers() -> dict:
    return {
            "What is your name?": ["You already know my name!", "I don't know, you tell me!", "Why do you ask?"],
            "What is your quest?": ["To seek the Holy Grail!", "To find the meaning of life.", "To learn Python."],
            "What is the airspeed velocity of an unladen swallow?": ["African or European?", "I have no idea.", "About 24 miles per hour."],
            "What is the meaning of life?": ["Reply hazy, try again", "42", "Life is what you make of it."],
            "What is your favorite color?": ["Blue", "Red", "Green"],
            "What is your favorite food?": ["Pizza", "Sushi", "Ice Cream"],
            "What is your favorite movie?": ["The Matrix", "Inception", "Interstellar"],
            "What is your favorite book?": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
            "What is your favorite hobby?": ["Reading", "Traveling", "Gaming"],
            "What is your dream job?": ["Professional Gamer", "Astronaut", "Chef"],
            }

def init_game() -> tuple:
    name = get_name()
    questions_answers = get_questions_answers()
    return name, questions_answers

def play_game(name: str, questions_answers: dict) -> None:
    logger.info(f"Hello {name}, welcome to the Magic 8 Ball game!")
    logger.info("You can ask me any question and I will give you an answer.")
    
    while True:
        question = input("Ask a question or enter 'exit': ")
        if question.lower() == "exit":
            logger.info("Goodbye!")
            break
        elif not question or question not in questions_answers:
            logger.info("I don't know the answer to that question.")
        else:
            import random
            random_choice = random.randint(0, len(questions_answers[question]) - 1)
            answer = questions_answers[question][random_choice]
            logger.info(f"Magic 8 Ball says: {answer}")

def main() -> None:
    logger.info("Starting the Magic 8 Ball game...")
    settings = init_game()
    play_game(*settings)

if __name__ == "__main__":
    main()