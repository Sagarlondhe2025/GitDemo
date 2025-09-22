'''
*************** SET *******************

Set is a data structure which is also called collection of items, in which we can represent a group of unique value as single entity
OR
Set is a collection of non repititive  elements

Syntax:
set_name={item1,item2,item3,...............,item n}

Notes
we write items of set inside curly braces "{}"
Insersion Order is Not Preserved
Indexing and Slicing Not work
Hetrogeneous elements are allowed
Mutable in Nature
'''

'''Empty Set            ## Empty Set can not be set={} because its Empty dictionary'''
set1=set()
print(type(set1))
print(set1)

'''Normal set'''
set2={7,10.5,'sagar',True}
print(set2)

''' Duplicate element not allowed'''
set3={5,7,'sagar','akash','sagar'}
print(set3)
### response is {'sagar', 'akash', 5, 7} it Ignored Duplicate Values

'''Insertion Order is Not Preserved'''
set4={4,'akash','sagar',True, 10.5}
print(set4)
###In response It gives {'akash', True, 'sagar', 4, 10.5} That mean Order is Not preserved
# Because of that Slicing and Indexing Does not Work Here

"""Add"""
set5={1,2}
set5.add('sagar')
print(set5)
## Reesponse {1, 2, 'sagar'}

'''Update... if we want to add more than 1 element in Set'''

set6={1,4,6}
set6.update('sagar')
print(set6)
#Response {1, 4, 's', 6, 'r', 'a', 'g'} which is incorrect

set7={1,4,6}
set7.update(['sagar','akash'])
print(set7)
##response {1, 4, 'akash', 6, 'sagar'}

''' POP method ...it removes Random Element '''
set8={1,2,3,4,5,6,7,'sagar'}
print(set8)
print(set8.pop())
print(set8)
print(set8.pop())
# Response
# #{1, 2, 3, 4, 5, 6, 7, 'sagar'}
# 1
# {2, 3, 4, 5, 6, 7, 'sagar'}
# 2


print("axaxaxaxax", set8.pop('sagar'))
#   Response  print("axaxaxaxax", set8.pop('sagar'))
#                         ~~~~~~~~^^^^^^^^^
# TypeError: set.pop() takes no arguments (1 given


'''Remove Method'''
set9={1,2,3,4,5,6,7,'sagar'}
set9.remove('sagar')
print(set9)
#Response {1, 2, 3, 4, 5, 6, 7} it removed 'sagar'

'''Clear'''
set10={1,2,3,4,5,6,7,'sagar'}
print(set10)
set10.clear()
print(set10)
#response
# {1, 2, 3, 4, 5, 6, 7, 'sagar'}
# set()       It cleared all elements from Set and become empty set

'''Union of sets 
It gives the union of two sets 
'''
set11={2,4,'sagar', 10.5}
set12={2,'sagar',7,True}

print(set11.union(set12))
print(set11 | set12)
#Response {True, 2, 4, 'sagar', 7, 10.5}
#{True, 2, 4, 'sagar', 7, 10.5} it union two sets

''' Intersection of two sets
It Gives a set of Common Elements Between Two Sets
'''
print(set11.intersection(set12))
set13=set11.intersection(set12)
print(set13)
#Response
# {2, 'sagar'}
# {2, 'sagar'}

'''Symetric_differance
It gives a set of values from 2 sets excluding common values
'''
set14={2,4,'sagar', 10.5}
set15={2,'sagar',7,True}

print(set14.symmetric_difference(set15))
#{True, 4, 7, 10.5} that gives valus excluding common values

''' differance
it gives extra element from set 1 excluding common elements
'''
set16={2,4,'sagar', 10.5}
set17={2,'sagar',7,True}
print(set16.difference(set17))
# Response{10.5, 4}
print(set17.difference(set16))
#{True, 7}