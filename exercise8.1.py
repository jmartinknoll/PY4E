# Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

lst = [1,2,3,4]
lst2 = [1,2,3,4]

def chop(t):
    del t[0]
    del t[len(t) - 1]
    return None

chop(lst)
print(lst)

def middle(t):
    s = t[1:]
    del s[:-1]
    return(s)

middle(lst2)
print(lst2)



