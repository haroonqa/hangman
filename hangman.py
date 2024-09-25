import random

# List of possible words for the game
word_list = ['python', 'java', 'kotlin', 'javascript']

# Function to get a random word from the list
def get_word():
    return random.choice(word_list)

# Function to display current progress of guessed word
def display_progress(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
def play_hangman():
    word = get_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        progress = display_progress(word, guessed_letters)
        print(f"Word: {progress}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

        if '_' not in progress:
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Sorry, you're out of attempts! The word was: {word}")

play_hangman()
