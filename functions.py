# functions in python  use the def keyword.
def my_func(): # define function
    print("this is my function!")
# call a function
my_func()

# example two
#While you define a function in python you have to careful since your input night produce the out you are expecting
def addNum(num1,num2):
    return  num1+num2
#result = addNum(20,30)
result = addNum("20","40")

#print(type(result))
# let's us if statement to check the validation

def sum(num1,num2):
    if type(num1) == type(num2)==type(10):
        return  num1+num2
    else:
        return 'sorry, I only require int values'

#result = addNum(20,30)
result1 = sum(20,30)
print(result1)

# lamda expression
# when do we use lamda expression?
# We need to introduce a function that accept another functions input parameters
# Filter function-> (accepting normal function as input and accepting lamda ass input function
mylist =[1,2,3,4,5,6,8]
def even_bool(num):
    return num%2==0
#filter function
#filter function accepts two param (func and sequence)
even_number = filter(even_bool,mylist)
#cast output as a list
print(list(even_number)) # print in the form of list
# lamda expression
# A break down of any functions

l_mylist =[1,2,3,4,5,6,8]
even_num = filter(lambda  num:num%2==0,l_mylist)
print(list(even_num))
# More functions
tweet ="go sports! #Sports"
res = tweet.split('#')
res1 = tweet.split('#')[1]
print(res)
print(res1)

# finally lets use in operator
# in is not a method it just useful
print('x' in [1,2,3,4,'y']) # returns boolean





