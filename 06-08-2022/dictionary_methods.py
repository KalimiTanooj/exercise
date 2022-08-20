'''#1.Accessing Values in Dictionary:

dict={'Name': 'tanooj', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

Output:
    
dict['Name']:  tanooj
dict['Age']:  7

#-----------------------------------------------------------------------------

#2.Updating Dictionary

dict={'Name': 'tanooj', 'Age': 7, 'Class': 'First'}
dict['Age']=8                      # update existing entry
dict['School']="DPS School"        # Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])


Output:

dict['Age']:  8
dict['School']:  DPS School

#-----------------------------------------------------------------------------

#3.Delete Dictionary Elements

dict={'Name': 'tanooj', 'Age': 7, 'Class': 'First'}
del dict['Name']                    # remove entry with key 'Name'
dict.clear()                        # remove all entries in dict
del dict                            # delete entire dictionary
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

Output:
    
dict['Age']:  dict['Age']
dict['School']:  dict['School']

#-----------------------------------------------------------------------------

#4.Python dictionary len() Method


dict={'Name': 'tanooj', 'Age': 7}
print("Length :",len (dict))

Output:
    
Length : 2

#-----------------------------------------------------------------------------

#5.Python dictionary clear() Method

dict={'Name': 'tanooj', 'Age': 7}
print("Start Len : ", len(dict))
dict.clear()
print("End Len : ", len(dict))

Output:

Start Len : 2
End Len : 0

#-----------------------------------------------------------------------------


#6.Python dictionary copy() Method

dict1={'Name': 'tanooj', 'Age': 7}
dict2=dict1.copy()
print("New Dictionary : ", str(dict2))

Output:

New Dictionary : {'Name': 'tanooj', 'Age': 7}

#-----------------------------------------------------------------------------

#7.Python dictionary fromkeys() Method


seq=('name', 'age', 'sex')
dict=dict.fromkeys(seq)
print("New Dictionary : ", str(dict))
dict=dict.fromkeys(seq, 10)
print("New Dictionary : ", str(dict))

Output:

New Dictionary : {'name': None, 'age': None, 'sex': None}
New Dictionary : {'name': 10, 'age': 10, 'sex': 10}

#-----------------------------------------------------------------------------


#8.Python dictionary get() Method

dict={'Name': 'tanooj', 'Age': 7}
print("result ", dict.get('Age'))
print("result ", dict.get('Education', "Never"))

Output:

result 7
result Never

#-----------------------------------------------------------------------------

#9.Python dictionary items() Method

dict={'Name': 'tanooj', 'Age': 7}
print("result ", dict.items())


Output:
    
result dict_items([('Name', 'tanooj'), ('Age', 7)])

#-----------------------------------------------------------------------------

#10.Python dictionary setdefault() Method


dict={'Name': 'tanooj', 'Age': 7}
print("result ", dict.setdefault('Age', None))
print("result ", dict.setdefault('Sex', None))


Output:

result 7
result None

#-----------------------------------------------------------------------------


#11.Python dictionary update() Method


dict={'Name': 'tanooj', 'Age': 7}
dict2={'Sex': 'male' }
dict.update(dict2)
print("result ", dict)

Output:

result {'Name': 'tanooj', 'Age': 7, 'Sex': 'male'}


#-----------------------------------------------------------------------------

#12.Python dictionary values() Method


dict={'Name': 'tanooj', 'Age': 7}
print("result ", dict.values())


Output:
    
result  dict_values(['tanooj', 7])

'''
#-----------------------------------------------------------------------------
