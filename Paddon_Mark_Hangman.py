import random
import os
guesses = 0
letters_used = ""
WORDLIST = 'word_list.txt'
num_words_processed = 0
the_word = None
total_words = 0
clear = lambda: os.system('clear') 

#Randomly selects a word from the text file
with open(WORDLIST, 'r') as f:
    for list_word in f:        
        total_words += 1
        if random.randint(1, total_words) == 1:
            the_word = list_word

progress = ((len(the_word))-1)*"*"

print("Hangman")
print("Progress: " + progress)
print("Letters used: " + letters_used)
print("You have seven guesses") 

# Main game loop
while guesses < 8: #keeps looping until 7 incorrect guesses are made
    if progress in the_word: break #if word is complete skip the loop
    guess = input("Please enter your next guess: ")
    if len(guess) > 1: if multiple characters entered then skip
        clear()
        print ("Try again")
        print ("Progress: " + progress)
        print ("Letters used: " + letters_used)
        print ("You have made", guesses, "incorrect guesses")
        continue
    if guess in the_word and guess not in letters_used: # checks if the guessed letter is correct
        clear()
        print ("Correct")
        letters_used += guess + ","
        progress = ""

        for letter in the_word: # shows the correctly guessed letters and a star for unknown
            if letter in letters_used:
                progress += letter
            elif letter not in letters_used:
                progress += "*"
            else:
                break
        progress = progress[:-1]
        
        print ('Progress: ' + progress)
        print ('Letter used: ' + letters_used)
        print ("You have made", guesses, "incorrect guesses")
    elif guess not in the_word and guess not in letters_used: # checks if the guessed letter is incorrect
        clear()
        guesses += 1
        print ('Incorrect')
        letters_used += guess + ","
        print ("Progress: " + progress)
        print ("Letters used: " + letters_used)
        print ("You have made", guesses, "incorrect guesses")
    else: 
        clear()
        print ("Try again")
        print ("Progress: " + progress)
        print ("Letters used: " + letters_used)
        print ("You have made", guesses, "incorrect guesses")

if progress in the_word: print('congratulations you win')
else: print('You lose the word was', the_word)


