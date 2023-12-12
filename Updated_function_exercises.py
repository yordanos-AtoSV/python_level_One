#############################
#### FUNCTION EXERCISES ####
############################
# Complete the tasks below by writing functions!

####################
## -- PROBLEM 1 --##
####################

# Given  a list of integers, return True if the
# sequence of numbers 1,2,3 appears
# in the list somewhere.

# Example
# arrayCheck([1,2,3,1])-> True
# arrayCheck([1,2,4,1])-> False
# arrayCheck([1,2,1,2,3])-> True

def arrayCheck(nums):
    #CODE GOES HERE

####################
## -- PROBLEM 2 --##
####################

# Given a string, return a new string mode of every other character starting
# with the first , so "hello" yields "Hlo".
#For example

#stringBits('Hello') -> 'Hlo'
# stringBits('Hello') -> 'H'
# stringBits('Hello') -> 'Hello'

def stringBits(str):
    #CODE GOES HERE

####################
## -- PROBLEM 3 --##
####################

# Given two strings, return True if either of the strings appears at the very end and
# of the other string,ignoring upper/lower case differences (in the other words, the
# computation should  not be "case sensitive")
# Note: s.lower() returns the lowercase version of a string

# Examples
#
# end_other('Hiabc','abc')->True
# end_other('AbC','Hiabc')->True
# end_other('abc','abXabc')->True

 def end_other(a,b):
     #CODE GOES OVER HERE

###################
## -- PROBELM 4 -- ##
###################
# Given a string, return a string where for every char in the orginal,
# there are two chars
# doubleChar('The') -> 'TThhee'
# doubleChar('AAbb') -> 'AAAAbbbb'
# doubleChar('Hi-There') -> 'HHii--TThheerree'

def doubleChar(str):
    #CODE GOES HERE

# Read this problem statement carefully
# Given 3 int values, a, b, c, returns their sum.However, if any of the values is a
# teen -- in the range 13 - 19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens.Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# define the helper below and the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
# Examples
#
# no_teen_sum(1,2,3)-> 6
# no_teen_sum(1,2,3)-> 3
# no_teen_sum(1,2,3)-> 3

def no_teen_sum(a,b,c):
    # CODE GOES HERE
def fix_teen(n):
    #CODE GOES HERE

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array
#
# examples
#
# count_evens([2,1,3,4]) -> 3
# count_evens([2,2,0]) -> 3
# count_evens([1,3,5]) -> 0

def count_evens(nums):
    # GOES GO HERE








