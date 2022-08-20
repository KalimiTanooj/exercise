'''#1. Write a program to print the following Patterns
  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5



for row in range(1,6):
    for column in range(1,6):
        print(column,end=" ")
    print()

output
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 

#----------------------------------------------------------------

#2.Write a program to print the following Pattern
  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1


for row in reversed(range(1,6)):
    for column in reversed(range(1,6)):
        print(column,end=" ")
    print()

output:

5 4 3 2 1 
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
#------------------------------------------------------------------

#3.Write a program to print the following Pattern
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1


n=5
for row in range(1,n+1):
    string=n+1-row
    pattern=str(string)
    print((pattern+" ")*n)

output:

  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1
  
#------------------------------------------------------------------

#4.Write a program to print the following Pattern
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5



for rows in  range(1,6):
    for col in range(1,rows+1):
        print(col,end=" ")
    print()

output:

  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5

#------------------------------------------------------------------


#5.Write a program to print the following Pattern
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5



for rows in range(1,6):
    for col in range(rows):
        print(rows,end=" ")
    print()

output:
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5

#-------------------------------------------------------------------

#6.Write a program to print the following Pattern
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15


n=5
a=0
for rows in range(1,n+1):
    for col in range(0,rows):
        a=a+1
        print(a,end=" ")
    print()

output:
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15        
#----------------------------------------------------------------

#7.Write a program to print the following Pattern
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1



n=5

for i in range(1,n+1):
    pattern=n+1-i
    a=str(pattern)
    print((a+" ")*i)

output:

  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1

#-------------------------------------------------------------

#8.Write a program to print the following Pattern
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9 



for row in range(1,6):
    for column in range(1,row+1):
        print(row,end=" ")
        row=row+1
    print()

OUTPUT:

  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9 

#-------------------------------------------------------------

9.Write a program to print the following Pattern
  A 
  B C
  D E F
  G H I J
  K L M N O


c=65
for i in range(65,69+1):
    for j in range(65,i+1):
        print(chr(c),end=' ')
        c=c+1
    print()


#-------------------------------------------------------------

#10.Write a program to print the following Pattern
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 


n=5
for i in range(1,n+1):
    print("* "*5)

output:
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
#---------------------------------------------------------------

#11.Write a program to print the following Pattern
   * 
   * * 
   * * * 
   * * * * 
   * * * * * 



n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

output:
   * 
   * * 
   * * * 
   * * * * 
   * * * * * 
#------------------------------------------------------------------

#13.Write a program to print the following Pattern
          * 
        * * * 
      * * * * * 
    * * * * * * *




n=40
for i in range(1,5):
    print(" "*n,end=" ")
    print("* "*i,end=" ")
    print()
    n=n-1

#---------------------------------------------------------

#14.Display Multiplication Table in given range using Nested for loops

n=int(input())
for i in range(1,11):
    print(n,"X",i,"=",i*n)


output:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
#----------------------------------------------------------------------

#15.Display Prime Numbers in the given range using nested for loops 


n=int(input("enter range"))
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

output:

enter range15
2 3 5 7 11 13 

#----------------------------------------------------------------------------

16.Write a program to print the following Pattern
	1
              3  2
       6   5   4
10  9   8   7

17.Write a program to print the following Pattern
10  9  8   7
      6   5  4
           3  2
               1

#-------------------------------------------------------------------------------



"loops"
-------

#1.Accept 10 numbers from the user and display their average. 
n=10
sum1=0
for i in range(1,n+1):
    inp=int(input("enter number"))
    sum1=sum1+inp
    avg=sum1/10
print(avg)

OUTPUT:

#----------------------------------------------------------------------------

#2.Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers) 

upper=12
lower=37
sum1_even=0
sum1_odd=0
for i in range(upper,lower+1):
    if i%2==0:
        sum1_even=sum1+i

    elif i%2==1:
        sum1_odd=sum1+i
print(sum1_even,"= sum of even")
print(sum1_odd,"= sum of odd")

OUTPUT:

312 = sum of even
325 = sum of odd
#----------------------------------------------------------------------------

#3.Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

for i in range(100,501):
    if i%11==0 and i%2!=0:
        print(i)

OUTPUT:
121
143
165
187
209
231
253
275
297
319
341
363
385
407
429
451
473
495

#----------------------------------------------------------------------------

#4.Write a program to print numbers from 1 to 20 except multiple of 2 & 3

for i in range(1,21):
    if i%2!=0 and i%3!=0:

        print(i)
OUTPUT:
1
5
7
11
13
17
19

#----------------------------------------------------------------------------

#5.Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers.

s=0
while(True):
    inp=int(input("enter number"))
    if inp==0:
        break
    s=s+inp
print(s)

OUTPUT:
enter number5
enter number6
enter number0
11

#----------------------------------------------------------------------------


#6.Write a program to accept decimal number and display its binary number.


d=29
l=[]
r=0

while(d>0):
   r=d%2
   if r==1:
       l.append(1)
   elif r==0:
       l.append(0)
   d=d//2
print(l[::-1])

OUTPUT:
[1, 1, 1, 0, 1]
#----------------------------------------------------------------------------


#7.Convert the following loop into for loop : 

x = 4 
while(x<=8): 
    print(x*10) 
    x+=2 



for x in range(4,9,2):
    print(x*10)

OUTPUT:
40
60
80


#----------------------------------------------------------------------------

#8.What is nested loop?

in Python, a loop inside a loop is known as a nested loop A nested loop is a loop inside the body of the outer loop.
The inner or outer loop can be any type, such as a while loop or for loop. For example, the outer for loop can contain a while loop and vice versa.
The outer loop can contain more than one inner loop. There is no limitation on the chaining of loops.
In the nested loop, the number of iterations will be equal to the number of iterations in the outer loop multiplied by the iterations in the inner loop.
In each iteration of the outer loop inner loop execute all its iteration. For each iteration of an outer loop the inner loop re-start and
completes its execution before the outer loop can continue to its next iteration.
Nested loops are typically used for working with multidimensional data structures, such as printing two-dimensional arrays, iterating a list
that contains a nested list.
**Syntax of using a nested for loop in Python
# outer for loop
for element in sequence 
   # inner for loop
   for element in sequence:
       body of inner for loop
   body of outer for loop


#----------------------------------------------------------------------------


#9.Write a program to convert temperature in Fahrenheit to Celsius. formula=>c=5/9(F-32)

farenheit=int(input("enter farenheit"))
celsius=(farenheit-32)*5/9
print(celsius)


output:


enter farenheit5
-15.0

#----------------------------------------------------------------------------

#10.Write a Python program to get the Fibonacci series between 0 to 50.



a=0
b=1
n=int(input())
print(b,end=" ")
while(n>2):
    c=a+b
    a=b
    b=c
    n=n-1
    print(c,end=" ")
OUTPUT:
1 1 2 3 5 8 13 21 34 

#----------------------------------------------------------------------------

#11.Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the
multiples of five print "Buzz". For numbers which are multiples of both three and five print "Fizz Buzz". 

Sample Output : 

fizzbuzz 
1 
2 
fizz 
4 
Buzz



for i in range(1,51):
    if i%3==0 and i%5!=0:
        print("fizz")
    elif i%5==0 and i%3!=0:
        print("buzz")
    elif i%3==0 and i%5==0:
        print("fizz buzz")
    else:
        print(i)
OUTPUT:
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz buzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizz buzz
31
32
fizz
34
buzz
fizz
37
38
fizz
buzz
41
fizz
43
44
fizz buzz
46
47
fizz
49
buzz

#----------------------------------------------------------------------------

#12.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

Note : Use 'continue' statement. 

Expected Output : 0 1 2 4 5


for i in range(0,7):
    if i==3 or i==6:
        continue
    else:
        print(i,end=" ")

OUTPUT:
0 1 2 4 5 
#----------------------------------------------------------------------------
'''







