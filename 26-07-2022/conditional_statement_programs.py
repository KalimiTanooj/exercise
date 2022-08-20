'''#1 first 10 natural numbers 

n=10
i=1
while (i<=n):
    print(i,end=" ")
    i=i+1


OUTPUT:

1 2 3 4 5 6 7 8 9 10 

--------------------------------------------------------------------------------------------
#2 sum of all numbers

n=int(input("enter number for range"))
sum1=0
for i in range(1,n+1):
    sum1=sum1+i
print(sum1)


OUTPUT:

enter number for range10
55

--------------------------------------------------------------------------------------------

#3 multiplication of given number

n=int(input())
for i in range(1,11):
    print(n,"X",i,"=",n*i)

OUTPUT:

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

--------------------------------------------------------------------------------------------
#4 display numbers from a list using loop

list=[1,2,3,4,5,6,7]
for i in list:
    print(i,end=" ")

OUTPUT:

1 2 3 4 5 6 7

--------------------------------------------------------------------------------------------
#5 count total number of digits in a number

n=int(input("enter number"))
b=str(n)
print(len(b),"is length of ",n,"number")

OUTPUT:
enter number156
3 is length of  156 number

--------------------------------------------------------------------------------------------
#6 print list in reverse order

list=[1,2,3,4,5,6,7,8,9]
l=[]
for i in list:
    l.insert(0,i)
print(l)
OUTPUT:
[9, 8, 7, 6, 5, 4, 3, 2, 1]
--------------------------------------------------------------------------------------------
#7 numbers from -10 to -1 using loop

for i in range(-10,0):
    print(i,end=" ")

OUTPUT:

-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
--------------------------------------------------------------------------------------------
#8 else block to display message done

n=int(input("enter number"))
if n>0:
    print("+VE")
else:
    print("-ve")
else:
    print("done")
    
OUTPUT:

enter number-5
-VE
--------------------------------------------------------------------------------------------
#9 prime numbers

r1=int(input("enter range"))
for i in range(1,r1+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
OUTPUT:
1 2 3 5 7 

--------------------------------------------------------------------------------------------

#10 fibonacci series

a=0
b=1
print(a,b,end=" ")
n=int(input())
while(n>2):
    c=a+b
    a=b
    b=c
    n=n-1
    print(c,end=" ")

OUTPUT:
0 1 1 2 3 5 8
--------------------------------------------------------------------------------------------

#11 factorial

n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

OUTPUT:
5
120
--------------------------------------------------------------------------------------------
#12 reverse a given integer

n=982633
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)

OUTPUT:
336289
--------------------------------------------------------------------------------------------


#13 sum of series upto n terms

n=int(input("enter the number of terms"))
x=int(input("enter the value of x"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
print("sum  of series is ",round(sum1,2))

OUTPUT:
enter the number of terms5
enter the value of x1
sum  of series is  2.28

--------------------------------------------------------------------------------------------

#14 cube of all numbers upto given number

n=int(input())
for i in range(1,n+1):
    print(i**3)

OUTPUT:

1
8
27
64
125
--------------------------------------------------------------------------------------------

#15 use loop to display elements from a given list at odd index position

lis=[0,1,2,3,4,5,6,7,8,9]
for lis in range(0,9,2):
    print(lis)

OUTPUT:
0
2
4
6
8
--------------------------------------------------------------------------------------------


#16 Name the keyword which helps in writing code involves condition.  ANS IS IF KEYWORD



--------------------------------------------------------------------------------------------

#17 if (expression.. is true):
#       statement will be executed


--------------------------------------------------------------------------------------------

#18 Is there any limit of statement that can appear under an if block.
ANS: no


--------------------------------------------------------------------------------------------

#19 voter id eligible or not

age=int(input())
if age<18:
    print("not eligibe for voter id")
if age>=18:
    print("eligible for voter id")

OUTPUT:
55
eligible for voteer id
--------------------------------------------------------------------------------------------

#20 even or odd

n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")

OUTPUT:
6
even

--------------------------------------------------------------------------------------------

#21 divisible by 7 or not


n=7
a=int(input())
if a%n==0:
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")
OUTPUT:

49
number is divisible by 7
--------------------------------------------------------------------------------------------


#22 print hello if number is multiple by 5

n=int(input())
if n%5==0:
    print("hello")

OUTPUT:
55
hello

--------------------------------------------------------------------------------------------

#23 calculate electic bill

units=int(input())
if units<=100:
    print("no charge")
    if units>=100 and units<200:
        print(5*units)
        if units>=200:
            print(10*units)

OUTPUT:
100
500
--------------------------------------------------------------------------------------------


#24 last digit of a number

n=446464
last_digit=n%10
print(last_digit)

OUTPUT:
4
--------------------------------------------------------------------------------------------

#25 last digit entered by user is divisible by 3 or not

n=int(input())
last=n%10
if last%3==0:
    print("last digit is divisible by 3")

OUTPUT:
56
last digit is divisible by3
--------------------------------------------------------------------------------------------

#26 accept percentages and print grade

p=int(input("enter percentage"))
if p>90 and p<100:
    print(" a grade")
elif p>80 and p<=90:
    print(" b grade")
elif p>=60 and p<=80:
    print(" c grade")
elif p<60:
    print(" d grade ")

OUTPUT:
82
b grade
--------------------------------------------------------------------------------------------

#27 cost price of a bike display tax

cost=int(input())
tax=0
if cost>100000:
    tax=15/100*cost
    print(tax)
elif cost>50000 and cost<=100000:
    tax=10/100*cost
    print(tax)
elif cost<=50000:
    tax=5/100*cost
    print(tax)
OUTPUT:

--------------------------------------------------------------------------------------------


#28 leap year


year=int(input())
if (year%4==0 and year%100!=0 ) or (year%400==0):
    print("leap year")


OUTPUT:
2012
leap year
--------------------------------------------------------------------------------------------

#29 wap take 1 t0 7 and print monday,tuesday...

d=int(input("enter day"))
if d==1:
    print("monday")
elif d==2:
    print("tuesday")
elif d==3:
    print("wednesday")
elif d==4:
    print("thursday")
elif d==5:
    print("friday")
elif d==6:
    print("saturday")
elif d==7:
    print("sunday")

OUTPUT:
6
saturday
--------------------------------------------------------------------------------------------

#30 


d=int(input("enter day"))
if d==1:
    print("jan")
elif d==2:
    print("feb")
elif d==3:
    print("mar")
elif d==4:
    print("apr")
elif d==5:
    print("may")
elif d==6:
    print("jun")
elif d==7:
    print("jul")
elif d==8:
    print("aug")
elif d==9:
    print("sept")
elif d==10:
    print("oct")
elif d==11:
    print("nov")
elif d==12:
    print("dec")

OUTPUT:
12
dec
--------------------------------------------------------------------------------------------

#31 what is a statement
ANS: a statement is an instruction that a python interpreter can execute


--------------------------------------------------------------------------------------------
#32 logical expression (a>b)and (c>d)


--------------------------------------------------------------------------------------------

#33 accept city and print monument

city=0
delhi=0
agra=0
jaipur=0
if city==delhi:
    print("monument is redfort")
if city==agra:
    print("monument is taj mahal")
if city==jaipur:
    print("monument is jal mahal")

OUTPUT:
delhi
monument is redfort
--------------------------------------------------------------------------------------------

#34 Write the output of the following if a = 9 

         

    if (a > 5 and a <=10):     

         print("Hello")

ANS:write output of following == bye



--------------------------------------------------------------------------------------------

#35 check whether a number enterd is 3 digit or not

n=int(input())
b=str(n)
if len(b)==3:
    print("entered num is 3 digit")
else:
    print("entered num is not a 3 digit number ")

OUTPUT:
456
entered number is 3 digit
--------------------------------------------------------------------------------------------

#36 voter id

age=int(input())
if age<18:
    print("not eligibe for voter id")
if age>=18:
    print("eligible for voter id")

OUTPUT:
56
eligible for voter id
--------------------------------------------------------------------------------------------

#37 senior citizen or not

age=int(input())
if age>=60:
    print("senior citizen")

OUTPUT:
65
senior citizen
--------------------------------------------------------------------------------------------

#38 lowest number of 2 num from user

a=int(input())
b=int(input())
c=min(a,b)
print(c)

OUTPUT:
1
2
1
--------------------------------------------------------------------------------------------

#39 largest number

a=int(input())
b=int(input())
c=max(a,b)
print(c)

OUTPUT:
1
5
6
6

--------------------------------------------------------------------------------------------


#40 positive or negitive

n=int(input())
if n>0:
    print("positive")
else:
    print("negitive")

OUTPUT:
5
positive
--------------------------------------------------------------------------------------------

#41 even or odd

n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")
OUTPUT:
42
even
--------------------------------------------------------------------------------------------


#42 divisible by 2 and 3

n=int(input())
if n%2==0 and n%3==0:
    print("the number is divisible by 2 and 3")

OUTPUT:
6
the number is divisible by 2 and 3
--------------------------------------------------------------------------------------------

#43 largest among 3 inputs

a=int(input())
b=int(input())
c=int(input())
if a>b and b>c:
    print("a is greater")
if b>c and b>a:
    print("b is greater")
else:
    print("c is greater")

OUTPUT:
1
5
6
6 is greater
--------------------------------------------------------------------------------------------

#44 check boiling or not

celsius=float(input())
if celsius >100:
    print("water is boiling")
else:
    print("water is not boiling")

OUTPUT:
125
water is boiling
--------------------------------------------------------------------------------------------

#45 age of youngest and oldest

a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))
d=min(a,b,c)
e=max(a,b,c)
print(d,"youngest")
print(e,"oldest")

OUTPUT:

--------------------------------------------------------------------------------------------

#46 calculate attendance

a=int(input("total no of workingdays"))
b=int(input("total no of days absent"))
c=a-b/100
if c<75:
    print("not allowed to write exam")

OUTPUT:

--------------------------------------------------------------------------------------------

#47 check trisngle is eqitorial , isosceles and scalen

a=int(input("enter side"))
b=int(input("enter side"))
c=int(input("enter side"))
if a==b==c:
    print("equilateral triangle")
elif a!=b!=c:
    print("scalen triangle")

elif a==b or b==c or a==c:
    print("isosceles")
OUTPUT:
enter side5
enter side5
enter side5
equilateral triangle

--------------------------------------------------------------------------------------------

'''











#47 triange is eqi    
