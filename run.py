import random

print("Welcome to Hangman!\nTry to guess the word by guessing individual letters inside!\n")

easy_words = ["cat", "sun", "cup", "ghost", "flower", "pie", "cow", "banana", "snowflake", "bug", "book", "jar", "snake", "light", "tree"]
medium_words = ["backbone", "whistle", "palace", "baseball", "computer", "password", "spring", "toast", "outside", "photograph", "circus", "battery", "bicycle", "music", "pirate"]
hard_words = ["avenue", "buffalo", "dwarves", "espionage", "galvanise", "injury", "jukebox", "kiosk", "luxury", "matrix", "oxygen", "queue", "rhythm", "transcript", "xylophone"]

guessed_letters = []

# Request diffculty function adapts from the validate_data function used in Code Institute's Love Sandwiches project
def request_difficulty():
    """
    Requests the user to select a difficulty by inputting a string input. Try to set the diffculty variable but if the wrong
    input is provided, a ValueError is raised and the user can try again. Once the user inputs the correct string, the function
    returns the difficulty.
    """
    try:
        difficulty = input("Select difficulty...\nType 'e' for easy\nType 'm' for Medium\nType 'h' for Hard\n")
        if difficulty == "e" or difficulty == "E":
            difficulty = "easy"
            print("You selected 'Easy' difficulty.")
        elif difficulty == "m" or difficulty == "M":
            difficulty = "medium"
            print("You selected 'Medium' difficulty.")
        elif difficulty == "h" or difficulty == "H":
            difficulty = "hard"
            print("You selected 'Hard' difficulty")
        else:
            raise ValueError(
                f"Invalid difficulty provided"
            )
    except ValueError as e:
        print(f"{difficulty} is an invalid difficulty. Please try again.\n")
        request_difficulty()

    return difficulty
        

# Generate word function

def set_list(difficulty):
    """
    Uses the difficulty variable value to select a list to choose a word from.
    """
    level = difficulty

    if level == "easy":
        selected_list = easy_words
    elif level == "medium":
        selected_list = medium_words
    else:
        selected_list = hard_words

    return selected_list
    
def generate_word(word_list):
    """
    Takes the selected list as a parameter and randomly selects one word from the list.
    """
    selected_word = random.choice(word_list)

    return selected_word
    
def show_hidden_word(selected_word):
    """
    Converts the randomly selected word into a string of equal length but with hidden letters.
    """
    hidden_word = '-' * (len(selected_word))
    
    return hidden_word

def request_letter():
    """
    Requests the user to input a letter as a guess and validates it.
    """
    try:
        guess = input("Guess one letter: ")
        if guess == "":
            raise ValueError(
                print("You didn't guess a letter")
            )
        elif guess.isalpha() == False:
            raise ValueError(
                print(f"{guess} is not a letter")
            )
        elif len(guess) > 1:
            raise ValueError(
                print(f"{guess} is more than one letter")
            )
        elif guess in guessed_letters:
            raise ValueError(
                print(f"{guess} has already been guessed")
            )
    except ValueError: 
        print("Error. PLease try again.")
        request_letter()
    else:
        guessed_letters.append(guess)

def check_letter_in_word(letter, selected_word):
    """
    Will check if the guessed letter is in the selected word. Will pass last item of the guessed_letters list it is most recent.
    """
    recent_guess = letter

    if recent_guess in selected_word:
        print(f"{recent_guess} is correct!")
    else:
        print("Ahh... it's not in the word.")
    

# Decrement lives function

# Show current guess function


difficulty = request_difficulty()
selected_list = (set_list(difficulty))
selected_word = generate_word(selected_list)
print(selected_word)
print(show_hidden_word(selected_word))
request_letter()
print(guessed_letters)
check_letter_in_word(guessed_letters[-1], selected_word)

