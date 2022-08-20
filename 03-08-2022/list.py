'''#1.Take 10 integer inputs from user and store them in a list and print them on screen.


l=[]
while True:
    inp=int(input("enter number"))
    if inp==0:
        break
    else:
        l.append(inp)
print(l)
      

OUTPUT:

enter number5
enter number6
enter number4
enter number2
enter number1
enter number3
enter number1
enter number2
enter number0
[5, 6, 4, 2, 1, 3, 1, 2]

#-------------------------------------------------------------------------------------------

#2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present 
#in list or not.
#( Iterate over list using while loop ).


l=[]
count=0
n=10
while count<n:
    inp=int(input("enter number"))
    count=count+1
    l.append(inp)
print(l)
inp2=int(input("enter number"))
if inp2 in l:
    print("given number is present in list")
else:
    print("given number is not present in list")
    
OUTPUT:


enter number1
enter number2
enter number3
enter number4
enter number5
enter number6
enter number7
enter number8
enter number9
enter number10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
enter number5
given number is present in list


#-------------------------------------------------------------------------------------------

#3.Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s.


l=[]
sum1=0
for i in range(1,21):
    inp=int(input("enter number"))
    l.append(inp)
print(l)
positive=0
negative=0
even=0
odd=0
zero=0
for i in l:
    if i>0:
        positive=positive+1
    if i<0:
        negative=negative+1
    if i%2==0:
        even=even+1
    if i%2!=0:
        odd=odd+1
    if i==0:
        zero=zero+1
print(positive,"number of positive numbers")
print(negative,"number of negative numbers")
print(even,"number of even numbers")
print(odd,"number of odd numbers")
print(zero,"number of 0s")
    
OUTPUT:



enter number-9
enter number5
enter number8
enter number0
enter number9
enter number-3
enter number5
enter number9
enter number8
enter number6
enter number3
enter number0
enter number5
enter number-9
enter number6
enter number3
enter number8
enter number7
enter number5
enter number9
[-9, 5, 8, 0, 9, -3, 5, 9, 8, 6, 3, 0, 5, -9, 6, 3, 8, 7, 5, 9]
15 number of positive numbers
3 number of negative numbers
7 number of even numbers
13 number of odd numbers
2 number of 0s

#-------------------------------------------------------------------------------------------

#4.Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.


l=[]
b=0
n=10
count=0
while count<n:
    inp=int(input("enter number"))
    count=count+1
    l.append(inp)
print(l)
b=l[::-1]
print(b)

OUTPUT:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#-------------------------------------------------------------------------------------------

#5.Write a program to find the sum of all elements of a list.

         
l=[1,2,3,4,5,6,7,8,9,10]
sum1=0
for i in l:
    sum1=sum1+i
print(sum1,"sum of all elements in list")

OUTPUT:

55 sum of all elements in list


#-------------------------------------------------------------------------------------------

#6.Write a program to find the product of all elements of a list.

l=[1,2,3,6,5]
product=1
for i in l:
    product=product*i
print(product)

OUTPUT:
180

#-------------------------------------------------------------------------------------------

#7.Initialize and print each element in new line of a list inside list.


l=[1,2,3,6,5]
print(*l, sep = "\n")


OUTPUT:

1
2
3
6
5

#-------------------------------------------------------------------------------------------

#8.Find largest and smallest elements of a list.



l=[5,8,3,4,6]
b=min(l)
c=max(l)
print(b,c)

OUTPUT:

3 8
#-------------------------------------------------------------------------------------------

#9.Write a program to print sum, average of all numbers, smallest and largest element of a list.



l=[5,8,3,4,6]
b=min(l)
c=max(l)
a=sum(l)/len(l)
print(a,b,c,end="")

OUTPUT:

5.2 3 8

#-------------------------------------------------------------------------------------------

#11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
#INITIAL list :
#58 24	13	15	63	9	8	81	1	78

#After spliting :
#58	24	13	15	63
#9	8	81	1	78



l=[58,24,13,15,63,9,8,81,1,78]
length=len(l)//2
print(l[:length])
print(l[length:])

OUTPUT:

[58, 24, 13, 15, 63]
[9, 8, 81, 1, 78]

#-------------------------------------------------------------------------------------------

#12. Ask user to give integer inputs to make a list. Store only even values given and print the list.
    

l=[]
n=6
count=0
while count<n:
    inp=int(input("enter number"))
    l.append(inp)
    count=count+1
print("list:",l)
l2=[]
for i in l:
    if i%2==0:
        l2.append(i)
print("even values in the list are",l2)

OUTPUT:

enter number1
enter number2
enter number3
enter number4
enter number5
enter number6
list: [1, 2, 3, 4, 5, 6]
even values in the list are [2, 4, 6]

'''

#-------------------------------------------------------------------------------------------