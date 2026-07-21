integerx = 10
stringx = "Rishi"
type(integerx)
type(stringx)


#after creating a variable in python you can check all of the things
#that are contained in that variable using the .dot in vscode
#after you press the dot you will reveal a list of things contained
# in the object. These things come in two flavors
#Properties: signaled by the wrench icon contains information. data.
#Methods: described by the purple box. describes all the actions that 
#can be performed by the object.
print(integerx.numerator)
print(integerx.denominator)
#properties are describing the state of the object that we created.
integerm = 5
print(integerm.numerator)
#Checking properties of the string
print(stringx) # no properties in there 

# what is really useful are methods.
#methods allow us to DO stuff with the objects that we have created.
#They are like a function in that they can do things
# but they are specifically attached (we say bound) to the object

#Lets check out some methods of this is a string: 
stringx.upper() # a method requires paranthesis because they 
#are actions, theyre like a function so you need to call them
# All strings will have this method, all objects of a given type will 
# share the same methods
stringx.lower()
print(stringx)
# we can store the result of that somewhere if we wanted 

sentencex = "hello my name is rishi"
sentencex.title()
white_space = "                 rishi"
white_space.strip()
email = "         ribh1293@colorado.edu     "
# imagine this was something someone entered into a form
# i want to check if this person has a dot edu email address
is_it_edu = email.endswith("edu")
is_it_edu
# False because there is white space after the entry
stripped_email = email.strip()
real_edu = stripped_email.endswith("edu")
real_edu
# we could write this simpler
Real_real_edu = email.strip().endswith("edu")
# email.strip returns a string so you can use endswith right after to check.
# this is called chaining you call methods on an object that is returned by another method

# common errors with methods and properties
email.shout() # attribute error: no attribute shout
# you try to call a method that does not exist on the object 
price = 12
price.numerator()
# an integer does not do anything. It is not a function or a method.
# You cannot call it. That's what the 'Not callable' is telling you.
# The error: Attempting to call a property. You can oly call a method inside an object

# more explorations
price.is_integer # this is a method: purple box and it is an action that we are doing
# nothing happens because you need paranthesis to call the method.
price.is_integer()


# in python you are often going to create other objects

from decimal import Decimal
# what is decimal? it is a factory for manufacturing a new kind of object: decimal objects.

a = Decimal(".1")
type(a)
b = Decimal(".2")
type(b)
print(.1 + .2) # floating point error
# this is because by default python represents floats with a limited number of zeros
print(a + b)
# if you rpint the sum of two decimal objects you get an exact representation
# decimal objects come with many new properties and methods
a.
