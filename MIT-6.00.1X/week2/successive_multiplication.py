
x = float(raw_input('Enter a number: '))
p = int(raw_input('Enter an integer power: '))

result = 1

for turn in range(p):
    print('iteration: ' + str(turn) + ' current result: ' + str(result))
    result = result * x


# define a procedure with two arguments

def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

print('Final result ' + str(iterativePower(x,p)))
