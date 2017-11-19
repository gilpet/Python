#number up to n python 3
[print(i**2) for i in range(n)]

#leap year
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

#print 1 to n separated by spaces
print(*range(1, int(input())+1), sep='')

#multiplying fractions
import operator
def product(fracs):
    t =  reduce(operator.mul , fracs)
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

#list to string and change 1 character
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

#count occurnces of substring in a string
def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if string[i:(i + sub_len)] == sub_string:
                counter = counter + 1
    return counter

#take string commands and perform eval on them
if __name__ == '__main__':
    n = input()
    l = []
    for i in range(int(n)):
        x = input()
        if x=='print':
            print(l)
        else:
            y = x.split()
            if len(y)==3:
                eval("l."+y[0]+'('+y[1]+','+y[2]+')')
            elif len(y)==2:
                eval("l."+y[0]+'('+y[1]+')')
            elif len(y)==1:
                eval("l."+y[0]+"()")

#convert string input to list of ints, then to tuple, then print hash(tuple)
if __name__ == '__main__':
    n = int(input())
    input_list = input().split()
    input_list = [int(x) for x in input_list]
    t = tuple(input_list)
    print(hash(t))

#find 2nd largest unique number (conver to set to remove dupes, sort, then [-2])
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = set(arr)
    y = list(x)
    y.sort()
    print(y[-2])
