'''#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?


l=[1,5,7,8,90,6,23]
a=l.index(5)
print(a)

#-------------------------------------------------------------------------------------------------------------------------

#2. WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?

l=[1,5,7,8,90,6,23]

list1=[1,5,7,8,90,6,23]
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)

output:

[1, 5, 6, 7, 8, 23, 90]

#-------------------------------------------------------------------------------------------------------------------------

#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and rate of return is 5 percentage for annum. and display the total amount to pay on  the end of the year.?

principle=float(input("Enter principle amount"))
time=float(input("Enter time for annum:"))
rate=float(input("Enter rate of return:"))
a=principle*(1+rate/100)**time
print(round(a,2))

Output:
Enter principle amount500
Enter time for annum:2
Enter rate of return:13
638.45

#-------------------------------------------------------------------------------------------------------------------------

#4. WAP to calculate the sum of the given matrix   [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]], where x1,x2....x9 values must take from command-line


l=[]
for i in range(1,10):
    inp=int(input("enter element:"))
    l.append(inp)
s=0
for i in l:
    s=s+i
print("Sum of matrix is:",s)

Output:
enter element:1
enter element:2
enter element:3
enter element:4
enter element:5
enter element:6
enter element:7
enter element:8
enter element:9
Sum of matrix is: 45

#-------------------------------------------------------------------------------------------------------------------------

#5 pattern program

n = 5
for i in range(n-1):
    for j in range(i):
        print(' ', end='')
    for k in range(2*(n-i)-1):
        print('*', end='')
    print()
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()

Output:
    
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

#-------------------------------------------------------------------------------------------------------------------------

#Problem statement


#You are required to enter a word that consists of x and y 
#that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 * x = y


#Determine if the entered word is similar to word zoo.

#For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

#Input format

    #First line: A word that starts with several Zs and continues by several Os.
    #Note: The maximum length of this word must be 20.

    

#Output format

#Print Yes if the input word can be considered as the string zoo otherwise, print No.

#instruction

#if input = zzzoooooo then print "yes".
#if input = zzooo print "no
'''
a = input("enter the word: ")
b = input("enter the word: ")
word = a+b
while(len(word)<20):
    if(word[0]=='z'):
        if(2 * len(a) == len(b)):
            print("yes")
            break
        else:
            print("no")
            break
    else:
        print("the word length is not start with z: ")
        break
else:
    print("the word length is more than 20")

#output:enter the word: zz
#enter the word: oo
#no
#enter the word: zz
#enter the word: oooo
#yes
#enter the word: zzzzzz
#enter the word: oooooooooooooo
#the word length is more than 20
#enter the word: edfg
#enter the word: thu
#the word length is not start with z: 
'''  
#-------------------------------------------------------------------------------------------------------------------------

