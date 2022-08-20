'''#1.WAP to find the senior citizens in the given list,list values should take dynamicaly (or) from the user only.
# suppose list=[23,67,45,89,65,12,15,19], and output:[65,67,89] final list should be in accending order.
# person age is 60 (or) more than 60 belongs to senior citizens.?

l=[]
n=8
l2=[]
count=0
while count<n:
    count=count+1
    inp=int(input())
    l.append(inp)
print(l)
for i in l:
    if i>=60:
        l2.append(i)
print(l2)


Output:
    
23
67
45
89
65
12
15
19
[23, 67, 45, 89, 65, 12, 15, 19]
[67, 89, 65]

#-----------------------------------------------------------------------------------

#2. WAP to find the diagonal matrix absolute difference?
# suppose  1   2  3
#          7   9  3
#         12   5  67
#result:=>53


m=[[1,2,3],[7,9,3],[12,5,67]]
a=[]
d1=0
d2=0
for i in m:
    for j in i:
        d1=m[0][0]+m[1][1]+m[2][2]
        d2=m[0][2]+m[1][1]+m[2][0]
print(d1-d2,"is diagonal of given matrix")


outtput:
53 is diagonal of given matrix


#-----------------------------------------------------------------------------------



#3. WAP to solve this pattern
     A
     A B
     A B C
     A B C D
     A B C D E
     A B C D
     A B C
     A B
     A






for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()


Output:
     A
     A B
     A B C
     A B C D
     A B C D E
     A B C D
     A B C
     A B
     A

#-----------------------------------------------------------------------------------



'''
