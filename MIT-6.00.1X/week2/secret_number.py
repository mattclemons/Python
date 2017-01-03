import time

print("Please think of a number between 0 and 100!")
time.sleep(2)

# At the start the highest the number could be is 100 and lowest is 0
high = 100
low = 0
guessed = False

# loop until we guess correctly
while not guessed:
    # bisection search: guess the midpoint between current high and low
    guess = (high + low) / 2
    print("Is your secret number " + str(guess) + "?")
    user_input = raw_input("     Enter 'h' to indicate the guess is too high.\n \
    Enter 'l' to indicate the guess is too low.\n \
    Enter 'c' to indicate I guessed correctly: ")

    if user_input == 'c':
        # correct
        guessed = True
    elif user_input == 'h':
        # too high
        high = guess
    elif user_input == 'l':
        # too low
        low = guess
    else:
        print("Sorry, I didn't understand your input.")

print('Game over. Your secret number was: ' + str(guess))

