'''#1. WAP to print middle character of the string

str1="Tanooj"
length=len(str1)/2
i=length
for i in range(1,100):
    if i==length:
        break
print(i)
print("middle character of the stringis '{}'".format(str1[i]))

output:

3
middle character of the stringis 'o'

#----------------------------------------------------------------------------------------------------------

#2. WAP to print half reverse of the string

str1="KNOWLEDGE"
length=len(str1)//2
i=length
for i in range(1,100):
    if i==length:
        break
print(str1[:i])
print(str1[i:])


Output:

KNOW
LEDGE
    
#----------------------------------------------------------------------------------------------------------

#3. WAP to remove all the vouels from the given string


str1="Tanooj"
vowels=["a","e","i","o","u"]
result=""
for i in str1:
    if i not in vowels:
        result=result+i
print(result)


output:

Tnj

#----------------------------------------------------------------------------------------------------------

#4. WAP to insert * in front of every vowels in the string.

#Input: BANANA
#Output: B*AN*AN*A


str1="BANANA"
vowels=["A","E","I","O","U"]
pattren=''
for i in str1:
    if i in vowels:
        pattren+='*'+i
    else:
        pattren+=i
print(pattren)        

Output:

B*AN*AN*A

#----------------------------------------------------------------------------------------------------------


#5. WAP to count number of words in the string.

str1="BANANA"
count=0
for i in str1:
    count=count+1
print(count)

OUTPUT:
BANANA

#----------------------------------------------------------------------------------------------------------

#6. WAP to remove extra space from the given string


str1="B AN ANA"
space=" "
st=""
for i in str1:
    if i==space:
        continue   
    else:
        st=st+i
print(st)

        
#----------------------------------------------------------------------------------------------------------


#7. WAP to insert string in between the given string
#Input: Ojas technologies 
#Output: Ojas innovative technologies


str1="Ojas technologies"
st=""
for i in str1:
    if i=="t":
        st=st+ " Innovative " + i
    else:
        st=st+i
print(st)
      

Output:

Ojas  Innovative technologies


#----------------------------------------------------------------------------------------------------------

#8. WAP to find the ascci value of given char

string = 'A'
print("The ASCII value of '" + string + "' is", ord(string))

#output:
The ASCII value of 'A' is 65

#----------------------------------------------------------------------------------------------------------

#9. insert ojas in front of every string 


str1="Ojas"
str2=""
for i in str1:
    i=i+"  ojas  "
    print(i,end="")

output:
O  ojas  j  ojas  a  ojas  s  ojas

#----------------------------------------------------------------------------------------------------------

#10. insert ojas in every extra space in the string  


str1="Ojas technologies and innovative"
st=""
for i in str1:
    if i==" ":
        st=st+ " ojas " 
    else:
        st=st+i
print(st)


Output:

Ojas ojas technologies ojas and ojas innovative


'''


#----------------------------------------------------------------------------------------------------------
