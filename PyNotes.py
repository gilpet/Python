#python 2 numbers (int, float)
3/2 # = 1
3.0/2 # = 1.5
3/2.0 # = 1.5
float(3)/2 # = 1.5
from __future__ import division #must be top top of file
3/2 # = 1.5 after import
2**3 # = 8
a = 5
a + a # = 10
a = 20
a # = 20

#Strings
'this is a string'
"this is a string"
"I'm a string" # use double quotes if single quote is in string and vise versa
print 'first line\nsecondline\ttab'
from __future__ import print_function
#in python 3, print is a function not a statement
len('peter') # = 5
s = 'hello world'
s[0] # = h
s[1:] # = ello world
s[:3] # = hel (up to but not including just like java substring)
s[:] # hello world
s[-1] # = d (loops back to last letter)
s[:-1] # = hello worl (up to that one)
s[::2] # = hlowrd -get everything, step size 2
s[::-1] # dlrow olleh reverse string
#strings are immutable like java
s[0] = 'x' # error
s + ' add this' # s = hello world add this
letter = 'z'
letter*10 # = zzzzzzzzzz
s = 'Hello'
s.upper() # = HELLO
s.lower() # = hello
s.split('e') # = ['H', 'llo']
