'''##1.Python Program to Return the Length of the Longest Word from the List of Words
##
##Problem Description:
##
##The program takes a list of words and returns the word with the longest length.
##
##Runtime Test Cases:
##
##Case 1:
##Enter the number of elements in list:4
##Enter element1:"Apple"
##Enter element2:"Ball"
##Enter element3:"Cat"
##Enter element4:"Dinosaur"
##The word with the longest length is:
##Dinosaur
## 
##Case 2:
##Enter the number of elements in list:3
##Enter element1:"Bangalore"
##Enter element2:"Mumbai"
##Enter element3:"Delhi"
##The word with the longest length is:
##Bangalore


l=[]
l2=[]
temp=0
n=int(input("enter number"))
for i in range(n):
    st=input("enter word")
    l.append(st)
for i in l:
    if len(i)>temp:
        temp=len(i)
        l2.append(i)
print(l2[-1])


Output:
    
enter number3
enter wordapple
enter wordbat
enter wordbanana
banana


'''

