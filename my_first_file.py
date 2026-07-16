print("hello world")
print(2+2)
#here nothing gets executed when i press enter
# two ways to run code
# 1. you can put the caret on a line and press shift + enter
# it is going to send the line to a repl and run it

# 2. is to run the file
# send the entire content of the file to python and all the lines will be executed in sequence
# you will want to do this once you have finished writing the script, press the play button on the top right
my_name = "Rishi Bhargava"
print(my_name)
#lets send line 12 (print) to the repl

# four big types of data in python
this_is_an_integer = 10
type(this_is_an_integer)
this_is_a_float = 10.1
type(this_is_a_float)
this_is_a_string = "Hello World"
type(this_is_a_string)
this_is_a_boolean = True
type(this_is_a_boolean)
# print and type are called functions. A function is something that takes between 0
#and many arguments and that has a specific behavior. It is an action.
# skill: when reading coe try to always understand what is going to happen and in what order
print(this_is_an_integer + 5)
what_is_this = type(this_is_an_integer)
print(what_is_this)
what_is_this = type(3.12)
print(what_is_this)

print((1+2)==3)
# Logical comparisons always return a boolean true or false
print(0.1+0.2)
print((0.1+0.2)==0.3)
#floating point error is when floats that should have one outcome are corrupted
# do not expect float operations to be exact
# what can you do?
my_rounded_addition = round((0.1+0.2), 1)
print(my_rounded_addition)
print(my_rounded_addition == 0.3)
round(3.12) #functions can have non-compulsory arguments sometimes called default arguments

#logical comparisons
print(3 == 5)
print(3<5)
print(3>3)
print(3 != 5)
print( 3 >= 3)
print( 5 <= 3)

# you can combine logical comparisons using and or or

condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2)
print(condition_1 and condition_3)
print(condition_1 or condition_3)
print(condition_3 and condition_4)
print(condition_3 and condition_2 or condition_4)
print(True + True)
print(True == 1)
print(False == 0)
print(True * 5)
# True is 1 and False is 0 in python.
print(10/ False)

# Calculations with strings

Greeting = "Hello " + "World"
print(Greeting)
# when adding strings + is interpreted as a concatenation operator, technical world for putting things
laugh = "ha" * 3
print(laugh)

weird_laugh = "ha" * 3.12
# needs to be an integer to repeat strings. Be careful when mixing up different types
# python will sometimes accept but often reject, always confusing to read

very_complicated_laugh = "ha" * ('Hello' == 'Hello')*3
print(very_complicated_laugh)
#Keep things simple stupid
# make sure to convert variables before working with them

number = 42
type(number)
is_this_a_number = "42" 
type(is_this_a_number)
print(number + 10)
print(is_this_a_number + 10)

#solution
now_this_number = int(is_this_a_number)
# str turns something that is not a string into a string, int turns it into an integer
int("fifteen")
int("fifteen" == "fifteen")

# one more example

my_age = 21
my_intro = "Hello my name is rishi and I am " + str(my_age)
print(my_intro)