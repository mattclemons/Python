import math

def eval_loop():
    while True:
        n = int(raw_input('Input?\n:: '))
        if n == 0:
            print "Done!"
            break
        else:
            result = eval('math.sqrt(n)')
        print result

eval_loop()
