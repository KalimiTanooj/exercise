'''

#1.  Add a list of elements to a given set



l=[15,26,23]
s=set()
for i in l:
    s.add(i)
print(s)

Output:

{26, 23, 15}

#------------------------------------------------------------------------------------------------------------------------------------------------

#2. Return a set of identical items from a given two Python

s1={1,2,3,4,5}
s2={2,3,4,5,6}
s3=s1&s2
print(s3)


s3=set()
s1={1,2,3,4,5}
s2={2,3,4,5,6}
for i in s1:
    for j in s2:
        if i==j:
            s3.add(i)
            s3.add(j)
print(s3)
            
{2, 3, 4, 5}


#------------------------------------------------------------------------------------------------------------------------------------------------

#3.Returns a new set with all items from both sets by removing duplicates

s3=set()
s1={1,2,3,4,5}
s2={2,3,4,5,6}
for i in s1:
    for j in s2:
        if i==j:
            continue
        s3.add(i)
        s3.add(j)
print(s3)



s3=set()
s1={1,2,3,4,5}
s2={2,3,4,5,6}
s3=s1.union(s2)
print(s3)

#------------------------------------------------------------------------------------------------------------------------------------------------

#4.Given two Python sets, update first set with items that exist only in the first set and not in the second set.


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}
set3 = set()
set1.difference_update(set2)

#print(set1)

#or

for i in set1:
    if i not in set2:
        set3.add(i)
print(set3)

#output:

#{1, 2}



#------------------------------------------------------------------------------------------------------------------------------------------------

#5.Remove 10, 20, 30 elements from a following set at once


s1 = {10,20,30,4,5}
s2=set()
for i in s1:
    if i==10 or i==20 or i==30:
        continue
    s2.add(i)
print(s2)



s1 = {10,20,30,4,5}
s2={10,20,30}
s3=set()
s3=s1-s2
print(s3)


Output:
{4, 5}

#------------------------------------------------------------------------------------------------------------------------------------------------


#6.Return a set of all elements in either A or B, but not both


set1 = {10,20,30,40,50}
set2 = {20,40,50,60}
set3 = set()

print(set1.symmetric_difference(set2))



for i in set1:
    if i not in set2:
        set3.add(i)
for j in set2:
    if j not in set1:
        set3.add(j)
print(set3)

#output:
{10, 60, 30}

#------------------------------------------------------------------------------------------------------------------------------------------------



#7.Determines whether or not the following two sets have any elements in common. If yes display the common elements


s1={1,2,3,4,5,6}
s2={2,3,4,5,6,12}
s3=set()
print(s1.isdisjoint(s2))


for i in s1:
    if i in s2:
        s3.add(i)
print(s3)


False
{2, 3, 4, 5, 6}

#------------------------------------------------------------------------------------------------------------------------------------------------


#8. Update set1 by adding items from set2, except common items


s1={1,2,3,4,5,6}
s2={2,3,4,5,6,12}
s3=set()
s1.symmetric_difference_update(s2)
print(s1)



for i in s1:
    for j in s2:
        if i==j:
            continue
    s3.add(i)
print(s3)


#------------------------------------------------------------------------------------------------------------------------------------------------


#9. Remove items from set1 that are not common to both set1 and set2


set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
set3 = set()

set1.intersection_update(set2)
#print(set1)

#or

for i in set1:
    if i in set2:
        set3.add(i)
print(set3)

#output:
{40, 50, 30}

#------------------------------------------------------------------------------------------------------------------------------------------------

#10.Write a Python program to check if a given set is superset of itself and superset of another given set

set1 = {10,20,30,40,50}
set2 = {60,50,70}

print(set1.issuperset(set2))
print(set1.issuperset(set1))

#output:
False
True


#----------------------------------------------------------------------------------------------------------------------------------------------

#11.Write a Python program to check a given set has no elements in common with other given set


set1 = {1,2,3}
set2 = {4,5,6}
#print(set1.isdisjoint(set2))
#print(set1.isdisjoint(set3))

#or

for i in set1:
    if i in set2:
        print("false")
        break
else:
    print("true")

#output:
true

#------------------------------------------------------------------------------------------------------------------------------------------------

#12.Write a Python program to remove the intersection of a 2nd set from the 1st set.


set1 = {1,2,3,4,5,6}
set2 = {3,4,5,6,7}

set3 = set()
set1.difference_update(set2)
print(set1)

for i in set1:
    if i not in set2:
        set3.add(i)
print(set3)
        

#output:
{1, 2}
{1, 2}

'''

#------------------------------------------------------------------------------------------------------------------------------------------------

Method	Description
add()	             Adds an element to the set
clear()	             Removes all the elements from the set
copy()	             Returns a copy of the set
difference()	     Returns a set containing the difference between two or more sets
difference_update()  Removes the items in this set that are also included in another, specified set
discard()	     Remove the specified item
intersection()	     Returns a set, that is the intersection of two or more sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	    Returns whether two sets have a intersection or not
issubset()	    Returns whether another set contains this set or not
issuperset()	    Returns whether this set contains another set or not
pop()	            Removes an element from the set
remove()	    Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	            Return a set containing the union of sets
update()	Update the set with another set, or any other iterable















