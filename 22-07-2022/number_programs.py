'''#1).Write a program to find sum of number.
a=int(input("enter the number"))
b=int(input("enter the number"))
sum = a + b
print(sum)

Output:
    
enter the number5
enter the number5
10

-- -------------------------------------------------------------------------------

#2).Python Program to Check strong number

sum1 = 0
num = int(input("Enter a number:"))
temp = num
while(num):
    i = 1
    f = 1
    r = num%10
    while(i <= r):
        f=f*i
        i=i + 1
    sum1=sum1 + f
    num=num//10
if(sum1 == temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")    

Output:
    
case 1:
Enter a number:145
The number is a strong number
case 2:
Enter a number:156
The number is not a strong number

--------------------------------------------------------------------

#3).Python Program to calculate the square root

num=float(input("Enter number"))
square_root = (num**0.5)
print("square root of number - ",num,"is:",square_root)

Output:
    
Enter number25
square root of number -  25.0 is: 5.0

---------------------------------------------------------------------

#4).Python Program to Calculate the Area of a Triangle

area=0
bredth=float(input("enter bredth: "))
height=float(input("enter height: "))
area = 0.5*bredth*height   #area
print("area of triangle is: ",area)

Output:
   
enter bredth: 
5
enter height: 
6
area of triangle is:  15.0


---------------------------------------------------------------------

#5).Python Program to Solve Quadratic Equation
#Equation: ax^2 + bx + c , d=b**2-4*a*c , d1=d**0.5

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
d = (b**2 - 4*a*c)
d1 = (d**0.5)
if(d<0):
    print("The roots are imaginary")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("First root is :",r1)
    print("Second root is :",r2)
    
output:
    
case - 1:
enter a: 1
enter b: -5
enter c: 6
First root is : 3.0
Second root is : 2.0

case - 2
enter a: 1
enter b: 5
enter c: 10
The roots are imaginary

-------------------------------------------------------------

#6).swapping two values

a=15
b=20
a,b=b,a
print("The value of a is: ",a)
print("The value of b is: ",b)

output:
    
The value of a is:  20
The value of b is:  15

--------------------------------------------------------------------------

#7).Python Program to Convert Kilometres to Miles

kilometer = float(input("Enter value in kilometer"))
conv_fac = 0.621371
miles = kilometer*conv_fac
print(kilometer,"kilometers is equal to",round(miles,2),"miles")

output:
    
Enter value in kilometer3.5
3.5 kilometere is equal to 2.17 miles

-------------------------------------------------------------------------

#8).Python Program to Check Leap Year

year=int(input("Enter year  "))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")

output:

case1:
Enter year  1996
The year is a leap year

case2:
Enter year  1998
The year is not a leap year

-----------------------------------------------------------------------

#9).Python Program to Check Prime Number

num=int(input("Enter a number "))
if (num>1):
    for i in range(2,num):
        if (num%i)==0:
            print(num,"Number is not a prime number")
            break
    else:
            print(num,"Number is a prime number")

output:
    
case1:    
Enter a number 5
5 Number is a prime number
case2:
Enter a number 6
6 Number is not a prime number

-------------------------------------------------------------------------

#10).Python Program to Find the Factorial of a Number 

num=int(input("Enter number  "))
factorial=1
if (num<0):
    print("Factorial doesnot exist in negative number")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("factorial of {} is {}".format(num,factorial))

output:

Enter number  5
factorial of 5 is 120

-----------------------------------------------------------------------------------

#11).Python Program to Print the Fibonacci sequence

a=0
b=1
n=int(input("enter number"))
print(a,b,end=" ")
while (n - 2):
    c = a + b
    a = b
    b = c
    n = n - 1
    print(c,end=" ")

Output:

enter number 10
0 1 1 2 3 5 8 13 21 34

-----------------------------------------------------------------------------------------

#12).Python Program to Check Armstrong Number

num = int(input("Enter a number"))
sum = 0
temp = num
while (temp > 0):
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10
if num == sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")

Output:
    
case 1:
Enter a number153
153 is an amstrong number
case2:
Enter a number159
159 is not an amstrong number

----------------------------------------------------------------------------------------

#13).Program to check Armstrong numbers in a certain interval

lower = 100
upper = 200
for num in range(lower, upper+1):
    order=len(str(num))
    sum=0
    temp = num
    while temp > 0:
        digit = temp%10
        sum += digit**order
        temp //=10
    if num == sum:
        print("amstrong numbers from {} to {} is".format(lower,upper),num)

Output:

amstrong numbers from 100 to 200 is 153

-------------------------------------------------------------------------------------

#14).Python Program to Find the Sum of Natural Numbers
    
num=int(input("Enter a number:"))
sum=0
while (num > 0):
    sum = sum + num
    num = num - 1
print("The sum of n natural numbers is :",sum)


output:
    
Enter a number:5
The sum of n natural numbers is : 15

----------------------------------------------------------------------------------------


#15).Python Program to find the factors of a number

n=125
for i in range(1,n+1):
    if n%i == 0:
        print("the factor of number {} is".format(n),i)

output:

the factor of number 125 is 1
the factor of number 125 is 5
the factor of number 125 is 25
the factor of number 125 is 125

--------------------------------------------------------------------------------------------


#16).Python program to convert decimal into other number systems

decimal_number=int(input("Enter decimal number"))
print("Binary number for {} is :".format(decimal_number),bin(decimal_number))
print("Octal number for {} is :".format(decimal_number),oct(decimal_number))
print("Hexa number for {} is :".format(decimal_number),hex(decimal_number))

Output:

Enter decimal number354
Binary number for 354 is : 0b101100010
Octal number for 354 is : 0o542
Hexa number for 354 is : 0x162

-----------------------------------------------------------------------------------------------

#17).Find LCM of two numbers

a = int(input("Enter the first number"))
b = int(input("enter the second number"))
if (a > b):
    min1=a
else:
    min1=b
while(True):
    if (min1%a == 0 and min1%b == 0):
        print("LCM is :",min1)
        break
    min1 = min1+1

Output:

Enter the first number5
enter the second number6
LCM is : 30

------------------------------------------------------------------------------------------------

#18).Find GCD of two numbers

a = int(input("Enter number"))
b = int(input("Enter number"))
for i in range (1,a + 1):
    if i <= b:
        if a%i == 0 and b%i == 0:
            GCD = i
print ("The GCD number of ",a," & ",b, " is: ",GCD)

Output:

Enter number6
Enter number9
The GCD number of  6  &  9  is:  3'''
