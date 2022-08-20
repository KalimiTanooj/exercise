'''#1.Accessing Values in Tuples:

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

Output:

tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)


#------------------------------------------------------------------------


#2.Updating Tuples


tup1=(12, 34.56)
tup2=('abc', 'xyz')
tup3=tup1+tup2
print(tup3)

Output:

(12, 34.56, 'abc', 'xyz')

#------------------------------------------------------------------------

#3.Python Tuple len() Method


tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print("First tuple length : ", len(tuple1))
print("Second tuple length : ", len(tuple2))

Output:

First tuple length :  3
Second tuple length :  2

#------------------------------------------------------------------------

#4.Python Tuple max() Method

tuple1=(456, 700, 200)
print("Max value element : ", max(tuple1))

output:

Max value element :  700

#------------------------------------------------------------------------


#5.Python Tuple max() Method

tuple1=(456, 700, 200)
print("min value element : ", min(tuple1))

Output:

min value element :  200

#------------------------------------------------------------------------

#6.Python Tuple tuple() Method

aList=[123, 'xyz', 'tanooj', 'abc']
aTuple=tuple(aList)
print("Tuple elements : ", aTuple)

Output:

Tuple elements :  (123, 'xyz', 'tanooj', 'abc')

'''

