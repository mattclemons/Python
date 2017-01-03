# three sticks with different lengths
# can the lengths make a triangle?
# for example, if stick 1 is 12 ans stick 2 and 3 are 1, 
# it cannot make a triangle.  But if stick 1,2 and 3 are 5
# they can make a triangle.

triangle =  [int(raw_input(x)) for x in ['a = ', 'b = ', 'c = ']]
triangle.sort()


def is_triangle():
	if triangle[0] + triangle[1] <= triangle[2]:
		print 'No'
	else:
		print 'Yes'

is_triangle()

