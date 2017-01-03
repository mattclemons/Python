a = int(raw_input('What is a?\n'))
b = int(raw_input('What is b?\n'))
c = int(raw_input('What is c?\n'))
n = int(raw_input('What is n?\n'))

def check_fermat(a,b,c,n):
	if n ==2:
		return 'Pythagoras got that one already.'
	elif a**n + b**n == c**n:
		return 'Holy Smokes, Fermat was wrong!'
	return "No that doesn't work."

print check_fermat(a,b,c,n)
