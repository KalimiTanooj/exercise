'''#List methods

#1.Accessing Values in Lists

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])



output:


list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]

#=============================================================================================

#2.Updating Lists



list = ['physics', 'chemistry', 1997, 2000];
print("Value available at index 2 : ")
print(list[2])
list[2] = 2001;
print("New value available at index 2 : ")
print(list[2])

output:

Value available at index 2 : 
1997
New value available at index 2 : 
2001

#=============================================================================================

#3.Delete List Elements


list1 = ['physics', 'chemistry', 1997, 2000];
print(list1)
del(list1[2]);
print("After deleting value at index 2 : ")
print(list1)

output:
    
['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 : 
['physics', 'chemistry', 2000]


#=============================================================================================
len[1, 2, 3]                            3 Length
[1, 2, 3] + [4, 5, 6]                   [1, 2, 3, 4, 5, 6] Concatenation
['Hi!'] *                               ['Hi!', 'Hi!', 'Hi!', 'Hi!'] Repetition
3 in [1, 2, 3]                          True Membership
for x in [1, 2, 3]: print x,            1 2 3 Iteration


#=============================================================================================

#4.append list elements

aList = [123, 'xyz', 'tanooj', 'abc'];
aList.append(2009);
print("Updated List : ", aList)

output:
    
Updated List : [123, 'xyz', 'tanooj', 'abc', 2009]

#=============================================================================================

#5.count list elements

aList = [123, 'xyz', 'tanooj', 'abc', 123];
print("Count for 123 : ", aList.count(123))
print("Count for tanooj : ", aList.count('tanooj'))

Output:

Count for 123 :  2
Count for tanooj :  1

#=============================================================================================

#6. extend

aList = [123, 'xyz', 'tanooj', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print("Extended List : ", aList)


Output:

Extended List :  [123, 'xyz', 'tanooj', 'abc', 123, 2009, 'manni']

#=============================================================================================

#7. index

aList = [123, 'xyz', 'tanooj', 'abc'];
print("Index for xyz : ", aList.index( 'xyz' ))
print("Index for tanooj : ", aList.index( 'tanooj' ))

Output:
    
Index for xyz : 1
Index for tanooj : 2

#=============================================================================================

#8.Python List insert() Method

aList = [123, 'xyz', 'tanooj', 'abc']
aList.insert( 3, 2009)
print("Final List : ", aList)

output:

Final List :  [123, 'xyz', 'tanooj', 2009, 'abc']


#=============================================================================================

#9.Python List pop() Method

aList = [123, 'xyz', 'tanooj', 'abc'];
print("A List : ", aList.pop())
print("B List : ", aList.pop(2))


A List :  abc
B List :  tanooj


#=============================================================================================


#10.Python List remove() Method

aList = [123, 'xyz', 'tanooj', 'abc', 'xyz'];
aList.remove('xyz');
print("List : ", aList)
aList.remove('abc');
print("List : ", aList)

Output:
    
List :  [123, 'tanooj', 'abc', 'xyz']
List :  [123, 'tanooj', 'xyz']

#=============================================================================================


#11.Python List reverse() Method


aList = [123, 'xyz', 'tanooj', 'abc', 'xyz'];
aList.reverse();
print("List : ", aList)

Output:
    
List :  ['xyz', 'abc', 'tanooj', 'xyz', 123]



#=============================================================================================



#12.Python List sort() Method

aList = [123, 'xyz', 'tanooj', 'abc', 'xyz'];
aList.sort();
print("List : ", aList)

Output:

List : [123, 'abc', 'xyz', 'xyz', 'tanooj']

#=============================================================================================

1 list.appendobj
Appends object obj to list
2 list.countobj
Returns count of how many times obj occurs in list

3 list.extendseq
Appends the contents of seq to list
4 list.indexobj
Returns the lowest index in list that obj appears
5 list.insertindex, obj
Inserts object obj into list at offset index
6 list.popobj = list[ − 1]
Removes and returns last object or obj from list
7 list.removeobj
Removes object obj from list
8 list.reverse
Reverses objects of list in place
9 list.sort[func]
Sorts objects of list, use compare func if given

#=============================================================================================
'''





