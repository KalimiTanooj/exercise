'''#1. Write a program to get all vowels from given string?

a=input("enter word")
b=['a','e','i','o','u']
for i in a:
    if i in b:
        print(i)

Output:
enter wordtanooj
a
o
o
    
#-----------------------------------------------------------



#2. Write a program to calculate the simple interest?


p=int(input("enter principle"))
t=int(input("enter time"))
r=int(input("enter rate"))
si=(p*t*r)/100
print(si)

Output:
enter principle150
enter time2
enter rate6
18.0

#-----------------------------------------------------------



#3. Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N?


n=int(input())
sum1=0
for i in range(1,n+1):
    sum1=sum1+1/i
print(sum1)


output:
10
2.9289682539682538




#-----------------------------------------------------------


#4 Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!?


num=int(input("Enter number:"))
s=0
for i in range(1,num+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    else:
        s=s+(1/fact)
print("result:",round(s,2))


Output:
Enter number:5
result: 1.72



#-----------------------------------------------------------


#5.Python Program to Replace All Occurrences of ‘a’ with $ in a String?


a=input("enter word")
for i in a:
    if i=='a':
        print("$",end=" ")
    else:
        print(i,end=" ")

Output:

enter wordtanooj
t $ n o o j 


#-----------------------------------------------------------

# problem statement given by batch no:4


##Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
##
##You may assume that each input would have exactly one solution, and you may not use the same element twice.
##
##You can return the answer in any order.
##
## 
##
##Example 1:
##
##Input: nums = [2,7,11,15], target = 9
##Output: [0,1]
##Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
##Example 2:
##
##Input: nums = [3,2,4], target = 6
##Output: [1,2]
##Example 3:
##
##Input: nums = [3,3], target = 6
##Output: [0,1]

nums = [2,7,11,15]

target=9

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if target==(nums[i]+nums[j]):
            print("indices are:",i,j)

Output:
indices are: 0 1

#-----------------------------------------------------------
'''













