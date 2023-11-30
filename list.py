# List are python's form of arrays
# They behave very similarly to  a javascript array
# list us the important features of list fin python
# create a list
mylist = [1,2,3,5,'hello',[4,5,6]] #
print(mylist)
#print(mylist[-1])
print(mylist[5])
print(mylist[5][0])


mylist_t = ['distributed systems',2,3,54,56,True, '234','you',[45,67,90]]
# print the list
print(mylist_t)
# indexing list
print(mylist_t[0]) #  distridbuted systems
print(mylist_t[1:]) # includes the index itself
print(mylist_t[:1]) # excluding the element itself
print(mylist_t[-1:]) # including the i dex
print(mylist_t[:-1]) # [45,67,90]
print(mylist_t[7][0]) # 45 within the nested list
print(mylist_t[7][1]) # 67 within the nested list
print(mylist_t[7][0]) # 90 within the nested list

# unlike string lists are mutable
st_list =[1,2,3]
print("Before value assigment")
st_list[0] ="hello"
print(type(st_list)) # ['hello',2,3]

# Assign values
print("After value reassignment")
st_list[0]='Felix'
print(st_list) # ['felix',2,3]

# basic list methods
# if you want to add  a value to the list
x_list = [20,30,40]
print("Before adding a value:")
print(x_list)
print("After adding a value:")
x_list.append('hello') #
#x_list.append([2,3,4,5])
myst_list = [34,68,"Distributed systems"]
z=myst_list.pop()
z=myst_list.pop(0)
print(myst_list) # only 68
#print(z)cle
#print(x_list)




# adding a list to a list
x_list.append(["Hello","World"])
#print(x_list)
# adding an item the original list
#y_list =[1,2,3,4]
#y_list.append([5,6,7,8])
#print(y_list)

z_list = [1,2,3,4] # this is the original list
print(" Appending members with out extending")
#z_list.append([5,6,7,8]) # out will be [1,2,3,4,[5,6,7,8]]
#print(z_list)
print("After extending")
z_list.extend([5,6,7,8])
print(z_list)

# reverse() and sort()
l= ['jo','ko','do','se']
l.reverse()
l1=[80,2,3,20,40,1]
l1.sort()

print(l1)


#y_list.append([5,6,7,8]) #
#print(y_list)




#  nested list
nest_list = [1,2,[3,4,5],['a','b','c']]
print(nest_list)
print(nest_list[3][-1]) # output will 'c'
print(nest_list[3][0]) # output will 'c'
print(nest_list[3][-2]) # output will be 'b'
print(nest_list[3][-3]) # output will be 'a'
# list comprehension
x = [[1,2,3],[4,5,6],[7,8,9]]
y_col=[row[0] for row in x]
print(y_col)
#print('X' in x)

