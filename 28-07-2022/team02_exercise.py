'''
#1.WAP in python arrange string characters
#such that lowercase letters should come first
st=input("enter string")
st1=""
st2=""
for i in st:
    if i.islower():
        st1=st1+i
    elif i.isupper():
        st2=st2+i
print(st1+st2)

OUTPUT:

enter stringTaNooj
aoojTN

#---------------------------------------------------------------------------------------------

#Q2.WAP to print sum of prime numbers in given list input
#:- 2 4 5 6 7 3 8 output :- 17

lst=[2,4,5,6,7,3,8]
s=0
for i in lst:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s=s+i
print("sum of prime numbers:",s)

Output:
    
sum of prime numbers: 17

#---------------------------------------------------------------------------------------------

#3.when do we use nested for loop.Write an example?
 nested loop is a loop inside the body of the outer loop. The inner or outer loop can be any type, such as a while loop or for loop.
 For example, the outer for loop can contain a while loop and vice versa.The outer loop can contain more than one inner loop. There
 is no limitation on the chaining of loops.In the nested loop, the number of iterations will be equal to the number of iterations in
 the outer loop multiplied by the iterations in the inner loop.In each iteration of the outer loop inner loop execute all its iteration.
 For each iteration of an outer loop the inner loop re-start and completes its execution before the outer loop can continue to its next iteration.
Nested loops are typically used for working with multidimensional data structures, such as printing two-dimensional arrays, iterating a list that
contains a nested list.A nested loop is a part of a control flow statement that helps you to understand the basics of Python.

# outer for loop
for element in sequence 
   # inner for loop
   for element in sequence:
       body of inner for loop
   body of outer for loop

#---------------------------------------------------------------------------------------------


#4.WAP in python remove all characters from a string except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )


char=input("enter your sentence:")
for i in char:
    if i.isdigit():
        print(i,end=' ')

enter your sentence:gfjgh43578438
4 3 5 7 8 4 3 8

#---------------------------------------------------------------------------------------------

#5.WAP to take a list and find the possition of the item .
#(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)?

l=[1,2,3,4,5,6]
n=int(input("enter number"))
for i in l:
    if i==n:
        print(l.index(n),"is the position in the given list")

Output:
enter number5
4 is the position in the given list


#---------------------------------------------------------------------------------------------

'''
