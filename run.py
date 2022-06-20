print("Welcome to Hangman!\nTry to guess the word by guessing individual letters inside!\n")

easy_words = ["cat", "sun", "cup", "ghost", "flower", "pie", "cow", "banana", "snowflake", "bug" "book", "jar", "snake", "light", "tree"]
medium_words = ["backbone", "whistle", "palace", "baseball", "computer", "password", "spring", "toast", "outside", "photograph", "circus", "battery", "bicycle", "music", "pirate"]
hard_words = ["avenue", "buffalo", "dwarves", "espionage", "galvanise", "injury", "jukebox", "kiosk", "luxury", "matrix", "oxygen", "queue", "rhythm", "transcript", "xylophone"]

# Request diffculty function adapts from the validate_data function used in Code Institute's Love Sandwiches project
def request_difficulty():
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
        print(f"{difficulty} is invalid difficulty. Please try again.\n")
        request_difficulty()
        return False

    return True
        

# Validate difficulty function

# Generate word function

# def generate_word():



# Request letter function

# Validate letter function

# Check letter in word function

# Decrement lives function

# Show current guess function

request_difficulty()