# def start_game(play_game):
#     play_game = input("Are you ready to play Mystery Word? Please enter: y / n ")
# if letter in input = y
#     return(input("Please choose your level: (E)asy, (N)ormal, or (H)ard"))
# # else:
# #     return("See you next time!")

# *************************************************************


guess = input("Enter a letter, to see if it is in your word: ")

print("The letter you chose was:", guess)

word = "difficulty"

current_guess = [guess]

def display_letter(letter, guess):
    """
    Conditionally display a letter. If the letter is already in
    the list `guess`, then return it. Otherwise, return "_".
    """
    if letter in guess:
        return letter
    else:
        return "__"
   
#    if letter not in word, return "That letter was not in your word. You have __ tries left"

[display_letter(letter, current_guess)
 for letter in word]

def print_word(word, guess):
    output_letters = []

    for letter in word:
        output_letters.append(display_letter(letter, guess))
    print(" ".join(output_letters))

print_word(word, current_guess) 



# ******************************************
# Store letters given to list together
# how to turn return/print (into a list)
# ******************************************

# # 1. Let the user choose a level of difficulty at the beginning of the program.
# #    Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
# #    characters; hard mode only has words of 8+ characters.

# # Open to read text

# # def words_txt(file):
# #     """Read in `file` and access words in file for grouped random selection."""
# #     with open(file) as word_file:
# #         word_file = word_file.read()

# #  maybe print("Some clever instruction about the game here") ?
# #  input("Enter your mode (e = easy, n = normal, h = hard): ")
# #  print confirmation ("You are now entering ("___") mode, where you will be given a mystery word...."
# #  sort words in words.txt by length. 

# # [
# #     word                                 # collection
# #     for word in words                    # iteration
# #     if len(word) >= 6 and len(word) <= 8 # selection
# # ]

# # 2. At the start of the game, let the user know how many letters the computer's
# #    word contains.

# # 3. Ask the user to supply one guess (i.e. letter) per round. This letter can be
# #    upper or lower case and it should not matter. If a user enters more than one
# #    letter, tell them the input is invalid and let them try again.

# # 4. Let the user know if their guess appears in the computer's word.

# # 5. Display the partially guessed word, as well as letters that have not been
# #    guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
# #    and d, the screen should display:

# ```
# B _ _ B A _ D
# ```

# # A user is allowed 8 guesses. Remind the user of how many guesses they have left
# # after each round.

# # _A user loses a guess only when they guess incorrectly._ If they guess a letter
# # that is in the computer's word, they do not lose a guess.

# # If the user guesses the same letter twice, do not take away a guess. Instead,
# print a message letting them know they've already guessed that letter and ask
# them to try again.

# The game should end when the user constructs the full word or runs out of
# guesses. If the player runs out of guesses, reveal the word to the user when
# the game ends.

# When a game ends, ask the user if they want to play again. The game begins
# again if they reply positively.