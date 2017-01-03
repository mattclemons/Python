def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


word = raw_input('Want to see if it is a palindrome?\n')

def is_palindrome(word):
    if len(word) <= 2 and word[0] == word[-1]:
        print 'True'
    elif word[0] == word[-1]:
        is_palindrome(word[1:-1])
    else:
        print 'False'

is_palindrome(word)
