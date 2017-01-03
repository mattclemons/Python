x = int(raw_input('Enter an integer: '))

if x%2 == 0:
    if x%3 == 0:
        print('\nDivisible by 2 and 3')
    else:
        print('\nDivisible by 2 and not by 3')
elif x%3 == 0:
    print('\nDivisible by 3 and not by 2')
else:
    print('\nNot divisible by 2 or 3')
