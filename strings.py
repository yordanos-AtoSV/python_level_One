#Strings
#1-> Basics
'hello'
"hello"
#print('I'm the best') # I am the best
print("I'm the best ") # I'm the best

# 2-> Indexing
# Indexing and grabbing up values or elements from the given list
mystring = 'kill him not, leave him'
print(mystring)
# grab a single element
print(mystring[0]) # indexing starts from 0 in python
print(mystring[4]) # nothing will be displayed
print(mystring[-1]) # accessing or grabbing element from the last
numbers_value ='678983'

#3-> Slicing
str ='generations'
print(str[2:]) # displays nerations
print(str[:]) # display the whole values
print(str[:2]) # display 'ge' excluding the index itself
print(str[:-2]) # displays generatio
print(str[-2:]) # output?
print(str[2:4]) # ne
print(str[::]) # display the whole evalues
print(str[::2]) # output? gnrtos


# Note -> Strings are immutable -> can not  change values

no_string ='authentication'
#no_string[0] = 'd' # immutable
#print(no_string)


# 4-> Basic Methods
# let's us see couple methods built into strings
me_string ='transportation'
r = me_string.upper()
print(r) # TRANSPORTASTION
r1 = me_string.lower()
print(r1) # transportation
r2 = me_string.capitalize()
print(r2) # Transportation
we_string = 'srvicee based architecure'
print(we_string) # ['srvicee based architecure']
r3 = we_string.split() # allows us to split any thing in the string.
print(r3) ['srvicee', 'based', 'architecure']
r4 = we_string.split('r') # allows us to split any thing in the string.
print(r4) #

'''
#5-> print Formatting
x= "Insert another string here:{}".format("Insert My Name!")
print(x)
# Inserting multiple strings
y = "Item One:{} Item Tow:{} Item Four:{}".format("Milk","Water","Coffee")
print(y)
z = "Item One:{x} Item Tow:{y} Item Four:{z}".format(x="Milk",y ="Water",z="Coffee")
print(z)
'''

