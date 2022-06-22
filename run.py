import random
from pprint import pprint



guessed_letters = []

easy_words = ["cat", "sun", "cup", "ghost", "flower", "pie", "cow", "banana", "snowflake", "bug", "book", "jar", "snake", "light", "tree"]
medium_words = ["backbone", "whistle", "palace", "baseball", "computer", "password", "spring", "toast", "outside", "photograph", "circus", "battery", "bicycle", "music", "pirate"]
hard_words = ["avenue", "buffalo", "dwarves", "espionage", "galvanise", "injury", "jukebox", "kiosk", "luxury", "matrix", "oxygen", "queue", "rhythm", "transcript", "xylophone"]


six_lives = ("""
        ________________
        |       |
        |       
        |     
        |       
        |      
        |_______________
        """)


five_lives = ("""
        ________________
        |       |
        |       O
        |      
        |       
        |      
        |_______________
        """)


four_lives = ("""
        ________________
        |       |
        |       O
        |       | 
        |       |
        |      
        |_______________
        """)


three_lives = ("""
        ________________
        |       |
        |       O
        |     / | 
        |       |
        |       
        |_______________
        """)


two_lives = ("""
        ________________
        |       |
        |       O
        |     / | \\
        |       |
        |      
        |_______________
        """)


one_life = ("""
        ________________
        |       |
        |       O
        |     / | \\
        |       |
        |      / 
        |_______________
        """)

no_lives = ("""
        ________________
        |       |
        |       O
        |     / | \\
        |       |
        |      / \\
        |_______________
        """)

hangman = [six_lives, five_lives, four_lives, three_lives, two_lives, one_life, no_lives]

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
            print("\nYou selected 'Easy' difficulty.")
        elif difficulty == "m" or difficulty == "M":
            difficulty = "medium"
            print("\nYou selected 'Medium' difficulty.")
        elif difficulty == "h" or difficulty == "H":
            difficulty = "hard"
            print("\nYou selected 'Hard' difficulty.")
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
        guess = input("Guess one letter: ").lower()
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
        print("")
        print(f"{recent_guess} is correct!")
        return recent_guess
    else:
        print("\nAhh... it's not in the word.")
    

# Decrement lives function
    

# Show current guess function

# update_hidden function adapts on code from following link
# https://tutorial.eyehunts.com/python/python-replace-character-in-a-string-by-index-example-code/#:~:text=Replace%20Character%20at%20a%20given,list%20items%20to%20the%20string.
def update_hidden(correct_guess, selected_word, guess_state):
    """
    If correct guess == None, it means the letter isn't in the word.

    Else finds the first occurence index of the letter in the selected word. Then replaces the letter so it can't be found again
    on the next loop. Hidden word converted into list and letter replaces '-' and finally converted back to a string. Loop
    continues until there are no more occurrences of the letter in the word.
    """
    if correct_guess == None:
        hidden_word = guess_state
        return hidden_word
    else:
        letter = correct_guess
        word = selected_word
        hidden = guess_state
        while True:
            if letter in word:
                index = word.find(correct_guess)

                word = word.replace(correct_guess, "-", 1)
                # print(f'inside function: {hidden}')
                temp = list(hidden)
                temp[index] = letter
                hidden = "".join(temp)

                print(hidden)    
            else:
                break
                print(hidden)
                return hidden
        return hidden

def check_finished(guess_state):
    """
    Checks if there are any more missing letter left in the hidden word. If there are no missing letters, congratulates the user 
    and returns True.
    """
    hidden = guess_state
    if "-" not in hidden:
        print("Well done you guessed the word!")
        return True

def play_again():
    """
    Once a game is over, asks the user if they want to restart the game or finish playing.
    """
    try:
        response = input("Do you want to play again? Type'y' for 'yes' or 'n' for 'no'.")
        if response.lower() == 'y':
            print("\nLet's play again!")
            start_game()
        elif response.lower() == "n":
            print("Exiting game...")
    except ValueError:
        print("Incorrect value. Please try again.")

# def reset_game(guesses):
#     """
#     Resets variables for the next game.
#     """
#     letters = []
#     return

def start_game():
    global guessed_letters 
    guessed_letters = []
    difficulty = request_difficulty()
    selected_list = (set_list(difficulty))
    selected_word = generate_word(selected_list)
    # print(selected_word)
    hidden_word = (show_hidden_word(selected_word))
    print("")
    print(hidden_word)
    remaining_lives = 6

    while True:
        request_letter()
        correct_guess = check_letter_in_word(guessed_letters[-1], selected_word)
        # print(hidden_word)
        updated_hidden = update_hidden(correct_guess, selected_word, hidden_word)
        hidden_word = updated_hidden
        
        if correct_guess == None:
            remaining_lives -= 1
            print(f"Remaining lives = {remaining_lives}")
            print(hangman[6 - remaining_lives])
            print(hidden_word)
            if remaining_lives == 0:
                print("\nNo more lives")
                print(f"The word was '{selected_word}'.")
                break

        elif check_finished(hidden_word) == True:
            break
        
    play_again()

print("Welcome to Hangman!\n\nTry to guess the word by guessing individual letters inside!\n")
start_game()