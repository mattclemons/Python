x = 25  # number to start with
epsilon = 0.01  # how close I am
numGuesses = 0  # keep track of guesses
low = 0.0   # range
high = x    # range
ans = (high + low)/2.0  # midpoint. halfway between low and high

while abs(ans**2 - x) >= epsilon:   # if this is true, the numbers are too far apart
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1 # change the number of guesses
    if ans**2 < x:
        low = ans   # if it's too small, change the lower end
    else:
        high = ans  # if too big, reduce

    ans = (high + low) / 2.0    # change the answer to again be the midpoint
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))

