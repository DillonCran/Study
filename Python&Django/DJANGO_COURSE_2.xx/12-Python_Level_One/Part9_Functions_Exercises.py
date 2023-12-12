#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

lists = [1, 1, 3, 3, 1]

def arrayCheck(nums):
    if filter([1,2,3], nums):
        return True

test = arrayCheck(lists)
print(test)



#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

test_string = "Hello"

def stringBits(str):
    i = 0
    for letter in str:
        if i % 2 == 0:
            print(letter)
            i += 1
        else:
            i += 1
            
stringBits(test_string)


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
test1 = "jkjhj"
test2 = "abc"

def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    a_len = len(a_lower)
    b_len = len(b_lower)

    if a_lower[-b_len:] == b_lower:
        print(True)
    elif b_lower[-a_len:] == a_lower:
        print(True)
    else:
        print(False)

end_other(test1, test2)

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

doub_test = "The"

def doubleChar(str):
    temp_string = ""
    for letter in str:
        temp_string += letter * 2
    print(temp_string)

doubleChar(doub_test)

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    adj_a = fix_teen(a)
    adj_b = fix_teen(b)
    adj_c = fix_teen(c)
    print(adj_a + adj_b + adj_c)
    
def fix_teen(n):
    if n in range(13, 20):
        if n == 15 or n == 16:
            return n
        else:
            return 0
    else:
        return n
        
no_teen_sum(2, 1, 14)

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

test_list = [2, 1, 2, 3, 4, 5, 5, 5, 6]

def count_evens(nums):
    temp_list = []

    for num in nums:
        if num % 2 == 0:
            temp_list.append(num)
        else:
            continue
    print(len(temp_list))
            
count_evens(test_list)
