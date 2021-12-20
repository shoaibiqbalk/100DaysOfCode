#Step 2

import random
import os
# import hangman_words 
# import hangman_art
from hangman_art import logo, stages
from hangman_words import word_list

# logo = hangman_art.logo
print(logo)

#function for clear screen
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

# word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
# stages = hangman_art.stages
print("You have total of 6 lives")



#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for letter in chosen_word:
    display.append("_")

print(display)


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()

    screen_clear()

    if guess in display:
      print("You have already guessed this letter.")

    for position in range(word_length):
        letter = chosen_word[position]
      # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    # print(display)

    
    if guess not in chosen_word:
        print(f"You guessed {guess}, which is not in Word. You lose a life")
        lives -= 1
        print(f"Remaining Lives: {lives}")
        print(stages[lives])

        if lives == 0:
            print("Game Over!!!!")
            break

    guessed_word = ' '.join(display)
    # print(f"{' '.join(display)}") 

    print(f"{guessed_word}\n")

if guessed_word == chosen_word:
    print("You Win!")