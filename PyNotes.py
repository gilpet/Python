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

#Print Formatting
s = 'String'
print 'Place my variable here: %s' %(s)
#or in python 3:
print('Place my variable here: %s' %(s))
x = 13.13
print 'Floating point number: %1.2f' %(13.145) #gets cut to 13.14
print 'Floating point number: %1.8f' %(13.145) #13.14500000
print 'Floating point number: %8.2f' %(13.145) #        13.14
print 'Convert to string %r' %(123) #converts to string
print 'First: %s, Second %s, Third %s' %('hi', 2, 'three')
print 'First: {x}, Second {x}'.format(x='inserted')
print 'First: {x}, Second: {y}, Third: {x}'.format(x='inserted', y='hello')

#Lists
my_list = [1,2.0,'three',4, 5]
len(my_list) # = 3
my_list[1:] # 2,3,4,5
my_list[:3] #1,2,3
my_list = my_list + ['new item', '7'] #appends to the end
my_list*2 #= [1,2,3,4,5,1,2,3,4,5]
l = [1,2,3]
l.append(4) # makes it 1,2,3,4
l.pop() # returns the last item, and also removes it fro Lists
x = l.pop(0) #removes 0 element, assigns to x
l[99] #index error
new_list = ['a','e','A', 'G','x','b','c']
new_list.reverse() #reverse order
new_list.sort() #sorts ASCII order
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = [l_1, l_2, l_3]
matrix[0] #returns list 1
matrix[0][0] #returns first element of first list
#list comprehensions
first_col = [row[0] for row in matrix] # [1,4,7] wow!

#Dictionaries - does not retain order, like hashtable (key/value pairs)
my_dict = {'key1': 'value', 'key2': 'value2', 'k1': 3}
my_dict['key1'] #returns 'value' (associated with the key)
my_dict['key1'][0] #returns 1st char of the string
my_dict['key1'][2].upper() #returns L
my_dict['k1'] += 100 #adds 100
d = {}
d['animal'] = 'dog'
d['answer'] = 14500 #this adds key/value pairs
d = {'k1': {'nestkey': 'nestvalue'}}
d['k1']['nestkey'] #returns 'nestvalue'
d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
d.keys() # returns a list of the keys (no order)
d.values() # returns a list of the values (no order)
p = sorted(d.values()) # [1,2,3]

#Tuples
l = [1,2,3,2,2]
t = (1,2,3,2,2)
len(t) # = 3
t[0] # = 1
t.index(2) # = first index of 2
t.count(2) # = 3
t[0] = 's' # error - tuples are immutable
#only 2 methods, count and index

#Files
f = open('test.txt')
f.read() # outputs, cursor is now at append
f.seek(0) #cursor is now at beginning of File
f.readlines() #returns each line as an element in a list
f = open('test.txt', "w") # write mode
f.write("hello")
f = open("test.txt", "r")
f.read()
for line in open('test.txt'):
    print line

#Sets - unordered unique items
x = set()
x.add(1) # x = {1}
x.add(2)
x.add(1) # wont add it
l = [1,1,1,1,12,22,2,2,2,2,3,3,3,3,3,4,4,4]
set(l) # gets only unique values {1,2,3,4}

#booleans
a = True
1 > 2 # false
b = None
