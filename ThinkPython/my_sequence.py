def sequence(n):
    while n != 1:
        print n,
        if n % 2 == 0:  # n is even
            n = n / 2
        else:           # n is odd
            n = n * 3 + 1

input=int(raw_input("Pick a number: "))
sequence(input)
