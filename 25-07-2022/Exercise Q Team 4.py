'''#1)WAP to find eligibility of a candidate voter_id
age=int(input("enter age"))
if (age >= 18 and age <= 80):
    print("caditate is eligible for voter_id")
else:
    print("candidate is not eigible for voter_")

output:
enter age55
caditate is eligible for voter_id
-------------------------------------------------------------------

#2)student marks in 5 subjects and find grade

telugu=int(input("enter telugu subject marks"))
hindi=int(input("enter hindi subject marks"))
english=int(input("enter english subject marks"))
maths=int(input("enter maths subject marks"))
science=int(input("enter science subject marks"))
sum1=telugu+hindi+english+maths+science
avg=sum1/5
if (avg>=80 and avg<=100):
    print("A grade")
elif (avg>=65 and avg<80):
    print("B grade")
elif (avg>=40 and avg <65):
    print("C grade")
else:
    print("Fail")

OUTPUT:
enter telugu subject marks50
enter hindi subject marks60
enter english subject marks70
enter maths subject marks50
enter science subject marks89
C grade

--------------------------------------------------------------------


#3).Even or Odd

n=int(input("enter number"))
if (n%2 == 0):
    print("given number is even number")
else:
    print("given number is odd number")

Output:
    enter number5
given number is odd number


---------------------------------------------------------------------

#4 WAP to print area of circle result in positive integers

pi=3.14
r=int(input("enter radius"))
area=2*pi*r**2
print(int(area))

Output:
enter radius5
157
-----------------------------------------------------------------------


#5 WAP finding variables  A and B are having the same memory location?

a=10
b=10
print(id(a))
print(id(b))

Output:

2060651790864
2060651790864


----------------------------------------------------------------------------
#problem statement

n=int(input("enter number"))
for i in range(0,n):
    b=i**2
    print(b)
Output:

enter number5
0
1
4
9
16
-------------------------------------------------------------------------'''
