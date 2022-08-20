
'''#1.what is a variable in and describe the role of variable in python memory management?

Variables are identifiers of a physical memory location,
which is used to hold values temporarily during program execution.

Python Variable is containers which store values. Python is not “statically
typed”. We do not need to declare variables before using them or declare their type.
A variable is created the moment we first assign a value to it. A Python variable is
a name given to a memory location. It is the basic unit of storage in a program



#2.what are the advantages and disadvantages of type casting?

advantage:

1. It can produce rough parts or parts with complex shapes;
2. Castings have a wide range of applications, and are not limited by size, shape, and weight;
3. Lower casting production cost;
4. The cutting amount of castings is less, which can reduce the processing cost.

Disadvantages:

1. The casting structure is not dense enough, there are defects such as shrinkage, pores, slag, cracks, etc., the grain size
is uneven, the mechanical properties of the casting are low, and the impact resistance is low;
2. There are many casting production processes, the process control is cumbersome, and it is easy to produce waste products.



#3.what is the difference between while loop and for loop?

For loop

The initialization, condition checking, and the iteration statements are written at the beginning of the loop.
It is used only when the number of iterations is known beforehand.
If the condition is not mentioned in the 'for' loop, then the loop iterates infinite number of times.
The initialization is done only once, and it is never repeated.
The iteration statement is written at the beginning.
Hence, it executes once all statements in loop have been executed.


While condition

The initialization and the condition checking is done at the beginning of the loop.
It is used only when the number of iterations isn’t known.
If the condition is not mentioned in the 'while' loop, it results in a compilation error.
If the initialization is done when the condition is being checked, then initialization occurs every time the loop is iterated through.
The iteration statement can be written within any point inside the loop.



#4.write 5 string method with example?

#1. How would you confirm that 2 strings have the same identity?

str1="ramu"
str2="raju"
if len(str1)==len(str2):
    print("2 strings have same identity")


OUTPUT:
2 strings have same identity

2. How would you check if each word in a string begins with a capital letter?

str1="hello welcome to ojas"
d=str1.title()
print(d)

OUTPUT:

Hello Welcome To Ojas



Check if a string contains a specific substrin


str1="hello welcome to ojas"
b="ojas"
if b in str1:
    print("substring is present")

OUTPUT:

substring is present


the index of the first occurrence of a substring in a string


str1="hello welcome to ojas"
b=str1.find("ojas")
print(b)

OUTPUT:

17


str1="hello welcome to ojas"
count=0
for i in str1:
    if str1:
        count=count+1
print("The number of characters in the string is = ",count)

OUTPUT:

The number of characters in the string is =  21



#---------------------------------------------------------------------------------------------

#5.write the Precedence rule of python with example?

19 + (5 / 2) + 4 % 2 - 6 * 3
19 + (5 / 2) + 4 % 2 - 6 * 3     	will be solved as per operator precedence rule
19 + 2.5 + 4 % 2 - 6 * 3   	 	will be solved as per operator precedence rule
19 + 2.5 + 0 - 6 * 3  		 	will be solved as per operator precedence rule
19 + 2.5 + 0 - 18  		  	will be solved as per operator precedence rule
21.5 + 0 - 18     			will be solved as per operator precedence rule
21.5 - 18   				will be solved as per operator precedence rule
3.5 (Answer)

#---------------------------------------------------------------------------------------------



# problem Statement:
#Write a program to check whether the given password is valid or not .
#conisder the password to be valid if it contain at least one digit ands one capital.
#input:it will be a single line containng string
#output: valid password or invalid password
#ex:GJ22191gopi
#ouput:valid password
password = input("enter the password: ")
number_pass = False
upper_pass = False
for i in password:
    if i.isupper():
        upper_pass = True
    elif i.isnumeric():
        number_pass = True
    if number_pass and upper_pass:
        print("valid password")
        break
else:

#output:enter the password: GJ22191gopi
valid password
enter the password: TANOOJ
not valid password
'''

#---------------------------------------------------------------------------------------------
