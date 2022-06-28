# Hangman
This hangman game replicates the traditional "pen and paper" game, but instead within a python terminal. This game aims to allow users to be able to play games of hangman, independently, against the computer. Players can choose a difficulty (easy, medium, hard) to randomly generate a word from the corresponding list. Users can input an individual letter to guess if the word contains the letter. The user starts the game with six lives; meaning that if six incorrect guesses are provided, they lose the game. The user can win the game by guessing all of the letters in the word. Throughout the game, the user constantly receives feedback, such as updates to the word, remaining lives, input requests etc, to make the game intuitive for the user.

The target audience for this project would include fans of the traditional hangman game that perhaps want to try a virtual version of the game, or people that have no playing partner so rely on playing individually against a computer. Users can play for fun, but also have the possibility of challenging themselves with the hard difficulty.

## Features
### request_difficulty() function

- Requests the user to select a difficulty by inputting a string input. Tries to set the diffculty variable but if the wrong
input is provided, a ValueError is raised and the user can try again. Once the user inputs the correct string, the function
returns the difficulty.
    - User is requested to input 'e' for easy, 'm' for medium, or 'h' for hard diffculty. The input is assigned to the difficulty variable and .lower method is used on the input to convert any uppercase inputs.
    - Input validation is used to try and set the value of the diffculty variable from 'e', 'm' or 'h' to 'easy', 'medium', or 'hard'. The difficulty is returned if there is no exception raised.
    - If the input was an integer, a TypeError is raised and the user receives feedback to explain the error. The request_difficulty function is called again so the user has another opportunity to select a diffculty.
    - If the input isn't equal to 'e', 'm' or 'h', a ValueError is raised and the user receives feedback to explain the error. The request_difficulty function is called again so the user has another opportunity to select a diffculty.

### set_list(difficulty) function

- Uses the difficulty variable value as an argument to select a list to choose a word from.
    - Three global variables are defined outside of the function (easy_words, medium_words, hard_words). Each contain a list of 15 strings (words).
    - The difficulty argument is stored in a 'level' variable. 
    - Conditionals are used to check value of 'level' and then assign either the 'easy_words', 'medium_words', 'hard_words' list to the variable 'selected_list'.
    - The selected_list variable is returned.