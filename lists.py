# Lists are Python's form of Arrays
# Lists
from typing import List

mylist = [4,2,3,4,68,90]
print(mylist)
#mylist1 =['service',4,5,6,34.6,True,'enjoy',[4,7,90]]
#print(mylist)
print(len(mylist)) # use 'len ' built in functions
the_list =['G','O','T','O','H','E','L','L']

print(("Before adding the list"))
print(the_list)
#print(the_list[::])
# Adding Item to the list #
the_list[0] = 'add new item'
print("After adding Item")
print(the_list)

# If you wanna add a new item appended to the very end of the list
the_list.append("Solid item")
print(the_list)
#the_list.append(['R','E','S','T']) # Adding list item to the item element
print(the_list)

# If want the above appended list to be a part of the orginal list

list_one = ['R','E','S','T',67,79]
#list_one.extend(the_list)
print(list_one)

# Removing Item from the list
#t = list_one.pop() # pop() method will remove the last element from the list
# keep in mind that pop() methods returns an item.
#print(t)
print(list_one) # the last item is removed
# What if i need to remove the first element from the list
#t = list_one.pop()
list_one.reverse()
# the list element was reversed in place like with out saving to another variable.
print(list_one)

creat_list =[103,63,9,1,90]
creat_list.sort() # python has it own rules for sorting item within the list
print(creat_list)

# nested list index
nest_list =[1,2,['x','y','Z']]
print(nest_list[2])
# if i needed to print particular 'X' elements
print(nest_list[2][0])

# List Comprehension

matrix = [[1,2,3],[4,5,6],[7,8,9]] # three list inside a single list.
# if i want to print the very first column
# List Comprehension
first_col = [row[0] for row in matrix]
print(first_col)