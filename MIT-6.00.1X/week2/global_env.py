x = 5
p = 10 # iterations
result = 1

for turn in range(p):
    print(' iteration: ' + str(turn) + ' current result: ' + str(result))
    result = result * x
