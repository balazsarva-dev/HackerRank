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

def get_possible_questions() -> list:
    return [
            "What is your name?",
            "What is your quest?",
            "What is the airspeed velocity of an unladen swallow?",
            "What is the meaning of life?",
            "What is your favorite color?",
            "What is your favorite food?",
            "What is your favorite movie?",
            "What is your favorite book?",
            "What is your favorite hobby?",
            "What is your dream job?"
            ]

def get_answers() -> dict:
    return {
            1: "Yes - definitely",
            2: "It is decidedly so",
            3: "Without a doubt",
            4: "Reply hazy, try again",
            5: "Ask again later",
            6: "Better not tell you now",
            7: "My sources say no",
            8: "Outlook not so good",
            9: "Very doubtful"
            }
    
def init_game() -> tuple:
    name = get_name()
    questions = get_possible_questions()
    return name, questions

def play_game(name: str, questions: list) -> None:
    logger.info(f"Hello {name}, welcome to the Magic 8 Ball game!")
    logger.info("You can ask me any question and I will give you an answer.")
    
    while True:
        answers = get_answers()
        question = input("Ask a question or enter 'exit': ")
        if question.lower() == "exit":
            logger.info("Goodbye!")
            break
        elif question not in questions:
            logger.info("I don't know the answer to that question.")
        else:
            import random
            random_answer = random.randint(4, 6)
            answer = answers[random_answer]
            logger.info(f"Magic 8 Ball says: {answer}")

def main() -> None:
    logger.info("Starting the Magic 8 Ball game...")
    settings = init_game()
    play_game(*settings)

if __name__ == "__main__":
    main()