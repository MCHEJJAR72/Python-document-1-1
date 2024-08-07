(variable assignment, loops, lists)
Tasks Today:
1-Int & Float assignments
     a) Assigning int
     b) Assigning float
     c) Performing Calculations on ints and floats
         - Addition
         - Subtraction
         - Multiplication
         - Division
         - Floor Division
         - Modulo
         - Exponential
2.String Input-Output
     a) String Assignment
     b) print()
     c) String Concatenation
     d) Type Conversion
     e) input()
     f) format()
     g) Old Way (python 2)
3.In-Class Exercise #1
If Statements
     a) 'is' keyword
     b) 'in' keyword
     c) 'not in' keyword
In-Class Exercise #2
Elif Statements
Else Statements
In-Class Exercise #3
For Loops
     a) Using 'in' keyword
     b) Continue Statement
     c) Break Statement
     d) Pass Statement
     e) Double For Loops
While Loops
     a) Looping 'While True'
     b) While and For Loops Used Together
Built-In Functions
     a) range()
     b) len()
     c) help()
     d) isinstance()
     e) abs()
Try and Except
Lists
     a) Declaring Lists
     b) Indexing a List
     c) .append()
     d) .insert()
     e) .pop()
     f) .remove()
     g) del()
     h) Concatenating Two Lists
     i) Lists Within Lists
     j) Looping Through Lists
Int & Float Assignments
Assigning int
number = 6

print(number)
6
Assinging float
number_float = 2.3
print(number_float)
number_float = 7.2
print(number_float)
2.3
7.2
Performing Calculations on ints and floats
Addition
num1 = 2
num2 = 5.4

result = num1 + num2

print(result)

# result += 2
print(result + 2)
7.4
9.4
Subtraction
result_diff = num2 - num1
print(result_diff)

result_diff -= 1
print(result_diff -1)
3.4000000000000004
1.4000000000000004
Multiplication
result_mul = num1 * num2
print(result_mul)

result_mul *= 2
print(result_mul)
10.8
21.6
Division
result_div = num2 / num1
print(result_div)

result_div /= 3
print(result_div)
2.7
0.9
Floor Division
result_floor = num2 // num1
print(result_floor)

result_floor //= 2
print(result_floor)
2.0
1.0
Modulo
result_mod = 13 % 2
print(result_mod)

result_mod %= 2
print(result_mod)
1
1
Exponential
square = 5 ** 2
print(square)

square **= 2
print(square)
25
625
String Input-Output
String Assignment
name = 'Josie'
print(name)
Josie
print()
Don't forget about end=' '

print('This is my first name: ', name)

print('This is my first name: ', name, end=' Worner')
This is my first name:  Josie
This is my first name:  Josie Worner
String Concatenation
first_name = 'John'
last_name = 'Smith'

full_name = first_name + ' ' + last_name
print(full_name)

full_name += ', Jr'
print(full_name)
John Smith
John Smith, Jr
Type Conversion
number = '32'

change_type_num = int(number)
print(number)
print(change_type_num)
32
32
input()
# input will always return a string
name = input("What is your name? ")
print("Nice to meet you, ", name)

age = int(input('What is your age?: '))
add_age = age + 5
print(add_age)
What is your name? Josie
Nice to meet you,  Josie
What is your age?: 29
34
format()
age = int(input("What is your age? "))

result_string = "You are {} {} and you are getting wiser!".format(age, name)
print(result_string)

result_again = f"{age} is a great time in life!"
print(result_again)
Old Way (python 2)
result_string2 = "You are %s and you look great for your age!" %age
print(result_string2)
In-Class Exercise 1
Create a format statement that asks for color, year, make, model and prints out the results

year = input("What year was your car made? ")
make = input("What is the make of your car?")
model = input("What is the model?")
color = input("What color is it?")

print(f"You have a {color} {year} {make.title()} {model.title()}.")
What year was your car made? 2017
What is the make of your car?honda
What is the model?civic
What color is it?blue
You have a blue 2017 Honda Civic.
If Statements
# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1 = 5
num2 = 10
num3 = 0

# if num1 == num2:
#     print("Equal values.")
# else:
#     print("Not equal")
    
if num2 > num1 or num3 > 0:
    print("Num2 is greater")
elif num1 > num2:
    print('Num1 is greater.')
else:
    print("Equal values.")
    Num2 is greater

'in' keyword
# Check if a character is in a string

char_name = 'Frodo Baggins'

if 'Frodo' in char_name:
    print('The ring bearer')
The ring bearer
'not in' keyword'
sega_char = 'Sonic'

if 'a' not in sega_char:
    print('a is NOT here...')
a is NOT here...

In-Class Exercise 2
Ask user for input, check to see if the letter 'p' is in the input

name = input('What is your name? ')

if 'p' in name.lower():
    print('The letter "P" is in your name!')
else:
    print('There is no letter "P" in your name.')
What is your name? Josie
There is no letter "P" in your name.
Using 'and'/'or' with If Statements
num_11 = 15
num_12 = 3
num_13 = 10
num_14 = 3

# If with 'and' statement
if num_11 / 5 == num_12 and num_13 - 7 == num_14:
    print("True and True")
    
# If with 'or' statement
if num_11 > num_12 or num_13 == num_14:
    print('True and False')
True and True
True and False
Elif Statements
first_name = input('What is your name? ')

if first_name == "Smith":
    print('The name is Smith.')
elif first_name == 'Brandon':
    print('The name is Brandon.')
elif first_name != 'Max':
    print('The name is not Max.')
else:
    print('The name is Max.')
What is your name? Josie
The name is not Max.
Else Statements
# syntax:
# for counter in condition:

name = 'Josie Worner'

for letter in name:
    print(letter)
J
o
s
i
e
 
W
o
r
n
e
r

J
o
s
i
e
 
W
o
r
n
e
r
For Loops
#continue statement will continue to the next iteration

for i in range(1,21):
    if i == 5:
        continue
    else:
        print(i)
        1
2
3
4
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Using 'in' keyword
# see above
Continue Statement
# will continue to next iteration
for i in range(20):
    if i == 5:
        continue
    print(i)
    0
1
2
3
4
6
7
8
9
10
11
12
13
14
15
16
17
18
19
Break Statement
# will break out of current loop
for i in range(1,21):
    if i == 5:
        break
    else:
        print(i)
1
2
3
4
Pass Statement
# mostly used as a placeholder, and will continue on same iteration
for i in name:
    pass
Double For Loops
for i in range(5):
    for j in range(5):
        print('i = ', i, 'j = ', j)
        i =  0 j =  0
i =  0 j =  1
i =  0 j =  2
i =  0 j =  3
i =  0 j =  4
i =  1 j =  0
i =  1 j =  1
i =  1 j =  2
i =  1 j =  3
i =  1 j =  4
i =  2 j =  0
i =  2 j =  1
i =  2 j =  2
i =  2 j =  3
i =  2 j =  4
i =  3 j =  0
i =  3 j =  1
i =  3 j =  2
i =  3 j =  3
i =  3 j =  4
i =  4 j =  0
i =  4 j =  1
i =  4 j =  2
i =  4 j =  3
i =  4 j =  4
While Loops
num = 0

while num < 10:
    print(num)
    num += 1
0
1
2
3
4
5
6
7
8
9
Looping 'While True'
#bad practice

game_over = True

while game_over:
    print('Infinite Loop')
    user_input = input('Would you like to stop? ')
    if user_input == 'Yes':
        game_over = False
Infinite Loop
Would you like to stop? no
Infinite Loop
Would you like to stop? no
Infinite Loop
Would you like to stop? yes
Infinite Loop
Would you like to stop? Yes
While & For Loops Used Together
num = 0

while num < 5:
    print('\nWhile loop iteration: ' + str(num))
    
    for i in range(2):
        print('For loop iteration: ' + str(i))
        
    num += 1
    While loop iteration: 0
For loop iteration: 0
For loop iteration: 1

While loop iteration: 1
For loop iteration: 0
For loop iteration: 1

While loop iteration: 2
For loop iteration: 0
For loop iteration: 1

While loop iteration: 3
For loop iteration: 0
For loop iteration: 1

While loop iteration: 4
For loop iteration: 0
For loop iteration: 1
Built-In Functions
range()
# range(start, stop, step)

for i in range(0, 21, 2):
    print(i)
0
2
4
6
8
10
12
14
16
18
20
len()
# len()

name = "max"

length = len(name)
print(length)

name = input('Give me the name of your favorite book. ')
length = len(name)
print(length)
3
Give me the name of your favorite book. Book
4
help()
# help()
# use this function to view more info a bout a python function

help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
  Methods defined here:
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop
isinstance()
#check a veriable to find out what object family or data type it belongs to
# isinstance(var, type)

num = input('Pick a number: ')

print(isinstance(4.5, int))

if isinstance(4.5, float):
    print('This number is a float type.')

num = int(num)
    
if isinstance(num, int):
    print(f'{num} is an int.')
else:
    print(f'{num} is a float!')
Pick a number: 7
False
This number is a float type.
7 is an int.
abs()
# abs()
# |-5| = 5 (absolute value)

print(abs(-5))
5
Try and Except
# use this to log out graceful and useful error messages
# does not stop the program

try:
    input_num = int(input('Guess a number: '))
    print('Your number is: ' + str(input_num))
except:
    print('That didn\'t work! Change your input to a number!')
Guess a number: four
That didn't work! Change your input to a number!
Lists
Declaring Lists
list_1 = []

names = ['max', 'cindy', 'kathy', 'bob', 'nate']
print(names)
['max', 'cindy', 'kathy', 'bob', 'nate']
Indexing a List
# list_name[start: stop: step]

# Single Index
print(names[0])

print(names[3])

# print starting at index 1 going to the end
print(names[1:])

# print starting at the beginning of a list up until a number
print(names[:2])

# print starting at index 1 and going up by 2 in each iteration
print(names[1::2])

# print starting at the back and present in reverse order
print(names[::-1])
max
bob
['cindy', 'kathy', 'bob', 'nate']
['max', 'cindy']
['cindy', 'bob']
['nate', 'bob', 'kathy', 'cindy', 'max']
.append()
names.append('brandon')
print(names)
['max', 'cindy', 'kathy', 'bob', 'nate', 'brandon']
.insert()
names.insert(3, 'devin')
print(names)
['max', 'cindy', 'kathy', 'devin', 'bob', 'nate', 'brandon']
.pop()
#defaults to the last value if no parameter is given
#pop returns the element that was removed in case you want to assign it to a variable
my_name = names.pop(2)
print(my_name)
print(names)
kathy
['max', 'cindy', 'devin', 'bob', 'nate', 'brandon']
.remove()
# value to be removed rather than index
print(names)

# names.remove('bob')
# print(names)

#remove multiple values
while 'brandon' in names:
    names.remove('brandon')
print(names)
['max', 'cindy', 'devin', 'bob', 'nate', 'brandon']
['max', 'cindy', 'devin', 'bob', 'nate']
del()
# goes by index rather than value
# be careful with del, it can cause indexing errors

del(names[1])
print(names)
['max', 'devin', 'bob', 'nate']
Concatenating Two Lists
# will append two lists together
# will not add the values

list_2 = [0, 1, 2]
list_3 = [3, 4, 5]

large_list = list_2 + list_3
print(large_list)
[0, 1, 2, 3, 4, 5]
Lists Within Lists
## lists can hold any type of other element, including other lists
# they can go as deep as you want. This is called nested lists

names = ['max', 'sam', 'josh', ['sally', 'sue', 'tameka']]
print(names)
print(names[3])
print(names[3][1])
['max', 'sam', 'josh', ['sally', 'sue', 'tameka']]
['sally', 'sue', 'tameka']
sue
Looping Through Lists
# two ways to loop through lists
#by index, or by 'in' keyword

# by index
for i in range(len(names)):
    print(names[i])
    
# with 'in'
for i in names:
    print(i)
max
sam
josh
['sally', 'sue', 'tameka']
max
sam
josh
['sally', 'sue', 'tameka']
Exercise #1
Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

number = 1
cubed = []

while 1000 not in cubed:
    cubed.append(number ** 3)
    number += 1
    
print(cubed)
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
Exercise #2
Get first prime numbers up to 100

prime_numbers = []

for number in range(2, 101):
    if number == 2 or number == 3 or number == 5 or number == 7:
        prime_numbers.append(number)
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        continue
    else:
        prime_numbers.append(number)
            
print(prime_numbers)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Exercise 3
Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input('What is your age? '))

if age < 18:
    print('Kids')
elif age >= 18 and age <= 65:
    print('Adults')
else:
    print('Seniors')
What is your age? 14
Kids