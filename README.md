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

![Image showing request_diffculty code](./images/request_difficulty.png)

### set_list(difficulty) function

- Uses the difficulty variable value as an argument to select a list to choose a word from.
    - Three global variables are defined outside of the function (easy_words, medium_words, hard_words). Each contain a list of 15 strings (words).
    - The difficulty argument is stored in a 'level' variable. 
    - Conditionals are used to check value of 'level' and then assign either the 'easy_words', 'medium_words', 'hard_words' list to the variable 'selected_list'.
    - The selected_list variable is returned.

![Image showing set_list code](./images/set_list.png)

### generate_word(word_list) function

- Takes the selected list as a parameter and randomly selects one word from the list.
    - The selected_list variable is passed into the function.
    - The random.choice method is used to randomly select one word from the list and store it in the selected_word variable.
    - The selected_word variable is returned.

![Image showing generate_word code](./images/generate_word.png)

### show_hidden_word(selected_word) function

- Converts the randomly selected word into a string of equal length but with hidden letters.
    - The selected_word variable is passed into the function.
    - The len function is used to calculate the length of the selected_word. This is multiplied with the string "-" to create a string of dashes with equal length to the selected_word. This string is stored in the hidden_word variable.
    - The hidden_word variable is returned.
    - This hidden_word variable is important as it needs to be printed to the user so they can see the length of the word they need to guess the letters for.

![Image showing show_hidden_word code](./images/show_hidden_word.png)

### request_letter() function

- Requests the user to input a letter as a guess and validates it.
    - User is requested to input a single letter as a guess. The input is assigned to the guess variable and .lower method is used on the input to convert any uppercase inputs.
    - Conditionals are used to raise a ValueError for empty inputs, non-letters, more than 1 letter and inputs already guessed.
    - Checking for inputs already guessed was possible by the else statement appending each guess to a global list storing all of the guesses. The exception could then be raised if the input is already in the the list.
    - Users receive feedback after each input and if the exception is raised, the function is called again so that they can input again.

![Image showing request_letter code](./images/request_letter.png) 

### check_letter_in_word(letter, selected_word)

- Will check if the guessed letter is in the selected word. Will pass last item of the guessed_letters list as it is most recent.
    - The most recent letter guessed to by the user is passed into the function by accessing the last index of the guessed_letters list (e.g. guessed_letters[-1]). This value is stored in the recent_guess variable. The selected_word is also passed into the function.
    - Conditionals are used to check whether the recent_guess is in the selected_word and users receive feedback about their guess.
    - If the recent_guess is in the selected_word, the recent_guess is returned and stored in the correct guess variable when the function is called. If recent_guess isn;t in the word, the function returns None.

![Image showing check_letter_in_word code](./images/check_letter_in_word.png)

### update_hidden(correct_guess, selected_word, guess_state)

- If there is a correct guess, will search for the position of the letter in the word. Then changes the "-" value in the hidden word to the correct letter to update it.
    - Passes the correct_guess (either a letter or None), selected_word and guess_state (hidden word's current value e.g --e--).
    - Using conditionals, if the correct_guess is None, the hidden word will remain unchanged. The guess_state is stored in the hidden_word and returned.
    - Else, the correct_guess needs to be found in the word. The arguments are stored in variables. Within an infinte while loop, the .find() method is used to find the index of the correct_guess in the word and stored in the variable 'index'. The .replace() method is used to replace the letter with "-" (on the next loop iteration, the letter won't be found at that index again. Allows us to check for the same letter at another index.). The temp variable stores a list version of the hidden word. The letter value can then be assigned to temp at the correct index. The .join method joins the list to an empty string and stores in the 'hidden' variable. The loop repeats as it is possible for the letter to apear multiple times in the word. Once the letter is no longer found, the loop breaks and the hidden is returned.

![Image showing check_letter_in_word code](./images/update_hidden.png)

### check_finished(guess_state)

- Checks if there are any more missing letter left in the hidden word. If there are no missing letters, congratulates the user 
    and returns True.
    - Passes the hidden_word as an argument and stores in hidden variable.
    - If the "-" string is not in the hidden variable, the user receives feedback to congratulate them and inform that the word has been guessed.
    - Function returns True.

![Image showing check_finished code](./images/check_finished.png)

### play_again()

- Once a game is over, asks the user if they want to restart the game or finish playing.
    - Asks the user if they want to play again and to type 'y' for 'yes' and 'n' for 'no'. Input stored in response variable.
    - Input validation tries conditionals.
    - If the response.lower() equals 'y', the user receives feedback and the start_game function is called to restart the game. 
    - If the response.lower() equals 'n', the user receives feedback and the game ends.
    - Empty inputs raise a ValueError. The user receives feedback to explain the error and the play_again function is called again to ask the user for another input. 
    - Integer inputs raise a TypeError. The user receives feedback to explain the error and the play_again function is called again to ask the user for another input.

![Image showing play_again code](./images/play_again.png)

### start_game()

- Calls the individual functions in the correct sequence to initiate and control the flow of the game.
    - Initiates variables guessed_letters and remainining_lives by assigning values directly.
    - Initiates variables difficulty, selected_list, selected_word, hidden_word by calling their appropriate functions so they are assigned the returned values.
    - An infinite while loop is used for the remaining functions. 
    - Conditionals are used to check if the correct_guess is None. If True, remaining lives decrease by 1 and the user receives feedback. A deeper condition checks for if the remaining_lives are equal to zero. If true, the user receives feedback and the loop breaks.
    - If the correct_guess isn't None, a condition checks if the check_finished function is equal to True. If True, the user receives feedback and the loop exits.
    - Outside the loop, the play_again function is called so that user has the option to restart the game.

![Image showing start_game code](./images/start_game.png)
