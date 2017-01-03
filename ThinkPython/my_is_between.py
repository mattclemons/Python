# Exercise 6.3. Write a function is_between(x, y, z)
# that returns True if x < y < z or False otherwise.

x = int(raw_input("enter x: "))
y = int(raw_input("enter y: "))
z = int(raw_input("enter z: "))

def is_between(x, y, z):
    return x <= y <= z

a = is_between(x, y, z)
if a:
    print 'y is between x and z!'
else:
    print 'y is not between x and z!'
    
        
