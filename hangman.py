# Diego Hangman, Help from kying18
import random
from words import words


# function used to find word that doesn't have dash or a space between random word
def get_good_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    # returns word in all uppercase 
    return word.upper()

def hangman():
    gamesWon = 0
    # keeps going until user wants to leave 
    while True:
        word = get_good_word(words)
        word_letters = set(word)
        guessed_letters = set()

        # lives given to the user
        lives = 7
        times_guessed = 0

        # gets users input 
        while len(word_letters) > 0 and lives > 0:
            # prints out how many lives the user has
            print("You have " , lives, " lives remaining. Letters used: ", " ".join(guessed_letters))

            # prints out the letters that are in the world that have been guessed
            # else it prints out '-' for the letters that have not been guessed
            word_list = [letter if letter in guessed_letters else "-" for letter in word]
            print("Current word: ", " ".join(word_list))
            
            # checks if they guessed at least once 
            if times_guessed > 0:
                print("Type 1: If you want to guess the whole word (You only get one try!)")

            # asks for user guess
            user_letter = input("Guess a letter: ").upper()
            times_guessed += 1

            # user decides to guess the whole word
            if user_letter == "1":
                user_guess_letter = input("Guess Word: ").upper()
                print()
                if user_guess_letter == word:
                    break
                else:
                    lives = 0
                    break

            # checks if letter is not in the guessed_letter set()
            # if so it adds it to the set()
            if user_letter not in guessed_letters:
                guessed_letters.add(user_letter)
                # then it checks if user letter is in word_letter set()
                # if so if removes it from the word_letter set(), meaning that the letter has been guessed
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print()
                
                # else it takes away a life
                else:
                    lives -= 1
                    print("Letter is not in the word. Try again!")
                    print()
            
            # if the user letter is in the guessed_letter set() it prints out this 
            elif user_letter in guessed_letters:
                print("You already used guessed that letter. Try again")
                print()
            # if anything else is inputted that's not a letter it prints this out
            else:
                print("Invalid guess. Try again you bot!")
                print()
        
        # checks to see if user won or lost
        if lives == 0:
            print("You lose you bot! The word was", word)
        else:
            print("You guessed the word!:", word)
            gamesWon += 1
        
        # ask user if they want to keep playing
        print()
        user_Choice = input("Want to keep playing (Y/N)? ").upper()
        print()
        # checks user choice to replay or not
        if user_Choice == "Y":
            continue
        elif user_Choice == "N":
            print("Thanks for playing! :D")
            if gamesWon > 1:
                print("You won a total of" , gamesWon, "games!")
            else:
                print("You won a total of", gamesWon, "game!")
            break


hangman()
