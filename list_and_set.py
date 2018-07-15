# File: list_and_set.py
# Description: Function for modifying lists with remove and count methods
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Function for modifying lists with remove and count methods. // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Modify_list_function (date of access: XX.XX.XXXX)



# Implementing the task
# As an input there is integer numbers divided by gap
# As an output to show just repeated numbers

# Option 1 with list and set and method 'remove'
# Creating a list with integer numbers by inputting them in one line with gap
lst = [int(i) for i in input().split()]

# Creating a set out of the list
# Repeated elements will not be added
s = set(lst)

# Going through all list and checking for the repetitions
for x in s:
    # Removing element from the list with method 'remove'
    lst.remove(x)
    if x in lst:
        # Again removing element from the list with method 'remove'
        lst.remove(x)
        # Showing the result
        print(x, end=' ')
        # Removing all other elements that can be met more then two times
        while x in lst:
            lst.remove(x)


# Option 2 with list and set and method 'count'
# Inputting string of integer numbers
# And at the same time converting it to the list of this divided by gap elements
lst = input().split()

# Creating a set out of the list
# Repeated elements will not be added
s = set(lst)

# Going through all elements of the set and checking for the repetitions in the list
for x in s:
    # Using method 'count' to find repetitions
    if lst.count(x) > 1:
        print(x, end=' ')

