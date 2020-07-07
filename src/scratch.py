import random

is_playing = True

while is_playing:
    print("Welcome to GUESS THE NUMBER! Have Fun!")
    number_to_guess = random.randint(1, 100)

    user_has_won = False
    # need a guessing loop that runs until user guesses correctly (while loop)
    while not user_has_won:
        # prompt user to input guess
        user_guess = int(input("I'm thinking of a number between 1 & 100... :"))
        # TODO: provide data to the user about the game (# of guesses?)
        # TODO: do some error checking on the user input

        # if user is right
        if user_guess == number_to_guess:
            user_has_won = True
            # alert user they won and ask if they want to play again
            print("You guessed it!!")

            play_again = input("Would you like to play again? Y or N")
            if play_again.lower() == "n":
                is_playing = False

        # if user is wrong
        elif user_guess < number_to_guess:
            print("Too LOW...try again!")
        else:
            print("Too HIGH...try again!")