import random

def play_hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    guessed_letters = []
    progress = ['_'] * len(word)
    attempts = 6
    print("Welcome to Hangman!")
    while attempts > 0:
        print(f"Word: {''.join(progress)}")
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("Already guessed.")
        else:
            guessed_letters.append(guess)
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        progress[i] = guess
            else:
                attempts -= 1
                print(f"Wrong! {attempts} tries left.")
            if ''.join(progress) == word:
                print(f"Congrats! The word is {word}")
                break
    if attempts == 0:
        print(f"Out of tries! The word was {word}")

play_hangman()