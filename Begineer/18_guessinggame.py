# guessing game

secret_word = "soccer"
user_guess = ""
number_guessed = 0
guess_limit = 3
out_of_guessed = False

while (user_guess != secret_word and not(out_of_guessed)):
    if number_guessed < guess_limit:
        user_guess = input("Guess the sport: ")
        number_guessed += 1
    else:
        out_of_guessed = True
        
if out_of_guessed:
    print("You're out of guesses!")
else:
    print("Congrats, you did it!")