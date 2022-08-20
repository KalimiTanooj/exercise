'''1.##Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included). 
##The numbers obtained should be printed in a comma-separated sequence on a single line.

l=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)

Output:

2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184,
2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373,
2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569,
2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758,
2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954,
2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143,
3157, 3164, 3171, 3178, 3192, 3199]



#------------------------------------------------------------------------------------


##2.Write a program which can compute the factorial of a given numbers. 
##
##The results should be printed in a comma-separated sequence on a single line. 
##
##Suppose the following input is supplied to the program: 
##
##8 
##
##Then, the output should be: 
##
##40320 


f=1
n=int(input())
for i in range(1,n+1):
    f=f*i
print("the factoial of {} is {}".format(n,f))


#------------------------------------------------------------------------------------

##3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
##
##Suppose the following input is supplied to the program: 
##
##8 
##
##Then, the output should be: 
##
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

d=dict()
n=int(input())
for i in range(1,n+1):
    d.update({i:i*i})
print(d)

n=int(input())
print({i:i*i for i in range(1,n+1)})


#------------------------------------------------------------------------------------

##4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.  



l=[]
for i in range(6):
    n=int(input())
    l.append(n)
print(l)
print(tuple(l))


#------------------------------------------------------------------------------------

##5.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. 
##
##Suppose the following input is supplied to the program: 
##
##without,hello,bag,world 
##
##Then, the output should be: 
##
##bag,hello,without,world



word=["without","hello","bag","world"]
word.sort()
print(word)

#------------------------------------------------------------------------------------

##6.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
##Suppose the following input is supplied to the program: 
##Hello world 
##Practice makes perfect 
##Then, the output should be: 
##HELLO WORLD 
##PRACTICE MAKES PERFECT


st=input('Hello world Practice makes perfect')
x=st.upper()
print(x)

#------------------------------------------------------------------------------------

##
##7.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
##
##Example: 
##
##0100,0011,1010,1001 
##
##Then the output should be: 
##
##1010 
##
##Notes: Assume the data is input by console. 



l=[5,21,27,28]
for i in l:
    if i%5==0:
        print(format(i,"b"))

#------------------------------------------------------------------------------------


##8.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
##
##Suppose the following input is supplied to the program: 
##
##Hello world! 
##
##Then, the output should be: 
##
##UPPER CASE 1 
##
##LOWER CASE 9



st="Hello world!"
u=0
l=0
for i in st:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print(u,l)


#------------------------------------------------------------------------------------

#9.Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

st='New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'
st=st.split(' ')
d={}
for i in st:
    d[i]=d.get(i,0)+1
i=list(d.keys())
i.sort()
for word in i:
    print(word,d[word])

Output:

2 2
3 1
3? 1
New 1
Python 5
Read 1
and 1
between 1
choosing 1
or 2
to 1

#------------------------------------------------------------------------------------

#10.Convert 2nd Part of String into Upper Case


st="tanooj"
l=len(st)//2
st2=st[:l]
st3=st[l:].upper()
st4=st2+st3
print(st4)


Output:
tanOOJ
        
#------------------------------------------------------------------------------------


#11.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.\ 


tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)

'''
#------------------------------------------------------------------------------------
