"""The goal of this function is to recreat wordle"""

__author__: str = "730676777"


def contains_character(guess: str, char: str) -> bool:
    """Function checks if inputted character is located anywhere in inputted word"""
    """Makes sure the length of the character is 1"""
    assert len(char) == 1, f"len('{char}) is not 1"
    """Starting Indexx to make loop"""
    index = 0
    """While loop that checks for every letter in a guess to see if the character is in it"""
    while index < len(guess):
        if guess[index] == guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """A function to display variables connected to correct, incorrect, and half correct answers"""
    result = ""
    index = 0
    """Emoji codes set as variables"""
    white_square: str = "\U00002b1c"
    yellow_square: str = "\U0001f7e8"
    green_square: str = "\U0001f7e9"

    """Loop that checks validity for character letter of the guess"""
    while index < len(guess):
        if guess[index] == secret[index]:
            """If guess is correct and in the right spot"""
            result += green_square
        elif contains_character(secret, guess[index]):
            """If guess is correct anywhere"""
            result += yellow_square
        else:
            """If guess is not correct at all"""
            result += white_square
        index += 1

    return result


def input_guess(length: int) -> str:
    """Function to retrieve the input of a users' guess"""
    guess = input(f"Enter a {length} letter guess")
    """Makes sure that the guess is the correct length """
    while len(guess) != length:
        guess = input(f"Sorry thats not {length} characters!")

    return guess


def main(secret: str) -> None:
    """Main function to compile all work together to create wordle simulation"""
    """Sets initial turn """
    total_turns = 6
    current_turn = 1
    """Loop to start round, collect input, and display results for all 6 turns """
    while current_turn <= total_turns:
        print(f"=== Turn {current_turn}/{total_turns} ===")
        guess = input_guess(len(secret))

        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {current_turn} rounds!")
            return
        current_turn += 1
    print("X/6 - Sorry, try again tomorrow!")


"""secret end portion that sets the word to be codes"""
if __name__ == "__main__":
    main(secret="codes")
