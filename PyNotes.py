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

#input raw_input

#python 2:
#raw_input() takes user input as string
#input() takes user input then performs eval() on it

#python 3:
#input() takes user input as string
#eval(input()) evals their input

#booleans
a = True
1 > 2 # false
b = None

#Comparison Operators
a == b
a != b # same as a <> b
1 < 2 < 3 # True
1 < 2 and 2 < 3 # True
1 < 3 > 2 # True
1 < 2 or 2 < 3 #short circuit evaluation

#if else statements
x = True
if not x:
    print "false"
else:
    print "true"

loc = 'Mall'
if loc == "not mall":
    print "nope"
elif loc == 'bank':
    print "still nope"
elif loc == 'Mall':
    print "mall"
else:
    print "nothing"

#modulo modulus
10 % 3 # = 1
18 % 7 # = 4
num % 2 == 0 # even
num % 2 == 1 # odd

#for loops
l = [1,2,3,4,5]
for element in l:
    print element

for num in l:
    if num % 2 == 0:
        print num
    else:
        print "odd!"

l = [1,2,3,4,5]
list_sum = 0
for num in l:
    list_sum += num

print list_sum

s = 'this is a string!'
for item in s:
    print item
#prints 1 letter on each line

tup = (1,2,3,4,5)
for item in tup:
    print item

l = [(2,4),(6,8),(10,12)]
for tup in l:
    print tup
    #prints all 3 tups

for (t1,t2) in l:
    print t1+t2
#prints totals
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print item
#prints the keys

#Python 3 use d.items()
#Python 2 use d.ieritems()

for k,d in d.iteritems():
    print k
    print d
#k3
#3
#k2
#2
#k1
#1

x = 0
while x < 10:
    print 'x is currently: ',x
    x += 1
#prints 0 to 9
else:
    print "while is done"

#break continue pass
x = 0
while x < 10:
    print 'x is currently', x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    if x == 3:
        print 'x is 3'
    else:
        print 'continuing' # next iteration
        continue
while x < 10:
    print 'x is currently', x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    if x == 3:
        print 'breaking'
        break
    else:
        print 'continuing'
#ends entire loop at x == 3

#range function range()
range(0,10) #0-9
range(10) # same as 0,10
x = range(0,10)
type(x) # list
start = 5
stop = 20
range(start,stop)#5-19
range(start,stop,2)#5,7,9,11,13,15,17,19
range(start,stop,4)#5 9 13 17

for num in range(1,7):
    print num#1-6
#xrange does not waste memory in python 2, in python 3 xrange is just range
for num in xrange(1,6):
    print num

#comprehensions
l = []
for letter in 'word':
    l.append(letter)

print l
#['w','o','r','d']
#BETTER WAY
l2 = [letter for letter in 'word']
l2 # = ['w','o','r','d']
l3 = [x**2 for x in xrange(0,11)]
l3 # = [0,1,4,9,16,25,36,49,64,81,100]
l4 = [number for number in range(11) if number %2 == 0]
l4 # = [0,2,4,6,8,10]
#for loop way:
l4 = []
for number in range(11):
    if number % 2 == 0:
        l4.append(number)

celsius = [0,10,20.1,34.5]
fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]
l5 = [x**2 for x in [x**2 for x in range(11)]]
#nested list comprehensions gave power of 4


#sample problems
st = 'print only words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print word

#even numbers from 1 to 10
range(0,11,2)

#use list comprehensions to create a list of all numbers between 1 and 50 that
#are divisable by 3
l50 = [num for num in range(1,50) if num%3==0]

st = 'print every word in this sentence that has an even number of letters'
for word in s.split():
    if len(word)%2==0:
        print word+" is even!"

#program that prints the integers 1 to 100 but multiples of 3 print fizz, and
#multiples of 5 print buzz. fizzbuzz for both
for num in xrange(1,100):
    if num%3==0 and num%5==0:
        print "FizzBuzz"
    elif num%3==0:
        print "Fizz"
    elif num%5==0:
        print "Buzz"
    else:
        print num

st = "create a list of the first letters of every word in this string"
l1 = [word[0] for word in st.split()]

#check if num is in range
if 7 in range(0,12) # = True

#count upper and lowercase letters
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print "Original String : ", s
    print "No. of Upper case characters : ", d["upper"]
    print "No. of Lower case Characters : ", d["lower"]

#multiply all nums in list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

#Palindrome
def palindrome(s):
    s = s.replace(' ','') # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]

#pangram
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

l = [1,2,3]
help(l.count)

def add(arg1, arg2):
    return arg1+arg2

x = add(7,5) #12
y = add('hi','hello') #hihello
def greeting(name):
    print 'hello '+name

def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for num in range (3,n,2):
        if n%num==0:
            return False
    return True

#Lambda expressions
def square(num):
    return num**2

sq = lambda num: num**2
sq(10) #= 100
even = lambda num: num%2==0
first = lambda s: s[0]
first('hello') # = 'h'
rev = lambda s: s[::-1]
rev('hello') # = 'olleh'

def adder(x,y):
    return x+y
#as lambda:
adder = lambda x,y: x+y
adder(30,20) # = 50

#Classes
class Dog(object):
    #class object attribute
    species = 'mammal' #all objects will get this when initialized
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog(breed='lab',name='Peter')
sam.breed # 'lab'

class Circle(object):
    #class attributes
    pi = 3.14
    def __init__(self,radius=1): # make radius 1 unless otherwise given
        self.radius = radius
    def area(self):
        return self.radius**2*Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def perimeter(self):
        return 2*Circle.pi*self.get_radius()

#Inheritance
class Animal(object):
    def __init__(self):
        print "Animal Created"

    def whoAmI(self):
        print "animal"

    def eat(self):
        print "eating"

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "dog"

    def bark(self):
        print "woof"
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

class Book(object):
    def __init__(self,title,author,pages):
        print "book created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): #toString()
        return "Title: %s, Author: %s, Pages: %s " %(self.title,self.author,self.pages)
    def __len__(self): #len override
        return self.pages
    def __del__(self):
        print "book is gone!"

#try Catch except Exception
try:
    2 + 's'
except TypeError:
    print "There was a type error"
finally:
    print "finally block accessed"
#OR don't specify the error
try:
    2 + 's'
except:
    print "There was a type error"
finally: #runs regardless
    print "finally block accessed"

try:
    f = open('testfile', 'w')
    f.write('Test write this')
except:
    print 'error writing to the file'
else: #else no exception
    print "file write was a success"

#try to read file that isn't there
try:
    f = open('testfile', "r")
    f.write('Test write this')
except:
    print 'error writing to the file'
else: #else no exception
    print "file write was a success"


def askint():
    while True:
        try:
            val = int(raw_input("please enter an int: "))
        except:
            print "looks like that was not an int"
            continue
        print "great job, it is an int"
        break
        print val

#modules imports
import math
math.#then see all the functions
math.sqrt(4) # = 2.0
math.factorial(6)
math.pow(2,3) # = 8.0
math.gcd(x,y) # look into this for algorithms
from math import sqrt
#then you can do
sqrt(4)


#map()
def fahrenheit(T):
    return (9.0/5)*T + 32
temp = [0,22.5,40,100]
map(fahrenheit, temp) #applies function to all temp elements
map(lambda T: (9.0/5)*T + 32, temp) # or Lambda
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
map(lambda x,y: x+y,a,b) #[5,7,9]
map(lambda x,y,z: x+y+z,a,b,c) #[12,15,18]
map(lambda num: num*-1, a) #makes all negative

#reduce()
lis = [47,11,42,13]
reduce(lambda x,y: x+y, lis)# (((47+11)+42)+13)
max(lis) # 47
max_find = lambda a,b: a if a>b else b
reduce(max_find,lis)
