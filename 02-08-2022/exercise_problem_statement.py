'''#-----------------------------------------------------------------------------------------
#1.Calculate income tax for the given income by adhering to the below rules
""" Taxable Income    Rate (in %)
    First $10,000     0
    Next $10,000      10
    The remaining     20
    
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% - $6000. ? """


while True:
    n-int(input("Enter amount:"))
    if (n>0) and (n<-10000):
        print("not tax to pay:0")
    elif (n>10000) and (n<-20000):
        r-(n-10000)
        print("your tax will be :",int((10/100)*r))
    elif (n>20000):
        r-(n-10000)
        p-10000
        t-(r-10000)
        t1-int((10/100)*p)
        
        t2-int((20/100)*t)
        
        print("tax will be:",t1+t2)
    
Enter amount:10000
not tax to pay:0

Enter amount:20000
your tax will be : 1000

Enter amount:35000
tax will be: 4000

Enter amount:45000
tax will be: 6000



#-----------------------------------------------------------------------------------------

#2.Count the length of list with out using any inbuilt function.?

ls = [1,2,5,4,9,13,54]

count=0
for i in ls:
    count=count+1
print('length of the list is:',count)
    
output:
length of the list is: 7
    

#-----------------------------------------------------------------------------------------


#3.Write a Python program to create a histogram from a given list of integers.?


ls=[1,2,3,4,5,4,3,2,1]

for n in ls:
    output = ''
    times = n
    while( times > 0 ):
        output += '*'
        times = times - 1
    print(output)

output:

*
**
***
****
*****
****
***
**
*

#-----------------------------------------------------------------------------------------

#4. Take input from user and if input is string print String
#if input is integer/float print integer
#if input is mix of string and integer print Error
#HINT Can be done using ASCII code?

st=input("enter string")
n=int(input("enter number"))
concat=0
concat=st+n
print(concat)

output:
    
enter string hi
enter number0
Traceback (most recent call last):
  File "C:/Users/sk22173/OneDrive - Ojas Innovative Technologies Pvt Lt/Desktop/1.py", line 9, in <module>
    concat=st+n
TypeError: can only concatenate str (not "int") to str

#-----------------------------------------------------------------------------------------


#5.Python program to check if a string is palindrome or not?


st1=input("enter string")
st2=""
st3=0
for i in st1:
    st2=st2+i
st3=st2[::-1]
print(st3)
if st1==st3:
    print(" given string is palindrome")
else:
    print("given string is not palindrome")

OUTPUT:
    
enter stringmadam
madam
 given string is palindrome


#-----------------------------------------------------------------------------------------
#problem statement
'''#2<=n<=10
#0<=marks[i]<=100
#length of marks arrys=3
#The query_name is 'beta'. beta's average score is .
#Input Format
#The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
#Constraints
#Output Format
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#Sample Input 0
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Sample Output 0
#56.00
#Explanation 0
#marks for Mallika are{52,56,60} whose average is ((52+56+60)/3)=56
#Marks for Malika are  whose average is 
#Sample Input 1
#2
#Harsh 25 26.5 28
#Anurag 26 28 30
#Harsh
#Sample Output 1
#26.50

'''
krishna = [67,68,69]
Arjun = [70,98,63]
malika = [52,56,60]
krishna_sum = 67+68+69
krishna_avg = krishna_sum/3
print(round(krishna_avg))
Arjun_sum = 70+98+63
Arjun_avg = Arjun_sum/3
print(round(Arjun_avg/3))
malika_sum = 52+56+60
malika_avg = malika_sum/3
print(round(malika_avg))
if(krishna_avg<Arjun_avg)and(krishna_avg<malika_avg):
    print("the minimal avg of krisha: ",krishna_avg)
elif(Arjun_avg<krishna_avg)and(Arjun_avg<malika_avg):
    print("the minimal avg of Arjun: ",Arjun_avg)
else:
    print("the minimal avg of malika: ",malika_avg)
#output:68
26
56
the minimal avg of malika:  56.0
'''
