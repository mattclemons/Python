n = raw_input('Square root of what?\n')

def square_root(n):
    n = float(n)
    x = n / 2
    i = 0
    while i < 10:
        y = (x + n / x) / 2
        x = y
        i += 1
    return x

print square_root(n)

