# weve been using functions from day 1
# print, type, round, str, float, int. bool, len
# a function is like a machine, it does something. 
# it usually takes one or more inputs and usually returns a result. 

# print takes any expression and turns it into a strings and returns it.
print("1234")
my_content = print("1234")
type(m)
# m is empty print("1234") did not store anything in it. 
my_content
# print does not return anything and thus cannot be stored into a variable.
# there are some functions (most) return something. think of them as a converyor belt.
# they are going to take an object on one side, do things to it, and then return
# the result of what it did on the other side of the machine.

# other functions are just doing stuff. Think of them as an engine.

# You are going to put some gas into them, they are going to do something.
# But they are not going to hand you back anything. 

# this is a function that takes a price, a rate, and returns the price updated with the rate
def print_total(price, rate): # def followed by function name, parenthesis agruments 
    # you will see that your cursor moved to the right:
    # this defines the body of the function. every code inside will define what the function will do
    total = price * (1+rate)
    print(total)

# function created 
print_total(100,.03)
# to store the total for later use
my_total = print_total(10,.1)
my_total
# Nothing there because the function is just print which is a non-storing function
# another function will solve this issue
def calc_total(price,rate):
    total = (price * (1+rate))
    return total

my_total = calc_total(10, .1)
my_total 
# because return instead of print was used, this function can be stored inside of a variable.
# if you don't store it 
calc_total(300,.1)
# still prints to the terminal because it was unassigned and then fell into the terminal
# more vocabulary: the inputs of a function are called the arguments.
# they come in two flavors:
# the first is positional arguments, defined by the order in which you enter them.
round(3.14, 1) # rounds the first number ot the number of digits in the second number 
round(1, 3.14) # 
# position arguments are expected in a certain order and given into a certain order

# some functions take a variable number of argments.
round(3.14) # here the second argument is non-compulsary, it has a defualt of zero.
# print is a similar function
print('abc', 'def')
# print takes an arbitrary number of arguments without changing the function

# second flavor of arguments: named arguments or keyword arguments.
# these are arguments that yare added by specifiying their name.
print('abc', 'def', sep = "*") # here sep is a named argument and i give it the value * 

# named arguments are not compulsory and have a default value
print('abc', 'def', sep = "*", end = "!")

def add_excitement(string): 
    excited_string = string + "!!!!!!!!!!!!"
    return excited_string
    print("The function ran successfully ")
    # anything added after a return will not do anything. 


x = add_excitement("boo")
x