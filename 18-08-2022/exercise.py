'''

##three occurrences of five. 
##Input: 
##[19, 19, 15, 5, 3, 5, 5, 2] 
##Output: 
##True

l=[19,19,15,5,3,5,5,2]
l1=l.count(19)
l2=l.count(5)
if l1>=2 and l2>=3:
    print("True")
else:
    print("False")
        
Output:
True


##2.WAPP to check a given list of integers where the sum of the integers is equal to length of list.

l=[1,1,1,1,1,1]
l2=len(l)
sum1=0
for i in l:
    sum1=sum1+i
l3=sum1
if l2==l3:
    print("sum of elements in given list is equal to length of given list")
else:
    print("sum of elements in given list is not equal to length of given list")

Output:

sum of elements in given list is equal to length of given list




##3.WAPP to add two integers without using arithmetic operator


l=[5,6]
c=sum(l)
print(c)

Output:
11

'''
