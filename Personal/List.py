'''
************** List *********************

######Notes######
List is Mutable in nature
Duplicate are allowed

#####Operations#######
create empty list
add values in List
Indexing
slicing
count
append
pop
insert
Extends
reverse
Nested List
List Compression
Copy
length '''


list1= [10,10.5,"Anuj",True,10,10.5]
print(list1)
# Response [10, 10.5, 'Anuj', True, 10, 10.5]

# #Empty List
list2=[]
list3=list()
print(type(list2))
print(type(list3))
print(list2)
print(list3)
# Response
# <class 'list'>
# <class 'list'>
# []
# []



# Indexing Print Anuj
list4= [10,10.5,"Anuj",True,10,10.5]
print(list4[2])
#Response Anuj


#Count()
list5= [10,10.5,"Anuj",True,10,10.5]
print(list5.count(10))
# Response 2



# #Index
list6= [10,10.5,"Anuj",True,10,10.5]
print(list6.index(10))
print(list6.index(10,1))
# Response 0      4

# #OR
listY=[1,4,'sagar','akash',10,'sagar',1]
print(listY.index('akash'))
print(listY.index(1,1))
#Response 3   6


 #Insert
list7= [10,10.5,"Anuj",True,10,10.5]
list7.insert(2,"Learn Python")
print(list7)
#Response [10, 10.5, 'Learn Python', 'Anuj', True, 10, 10.5



 #pop  Used for delete index value
list8= [10,10.5,"Anuj",True,10,10.5]
list8.pop(3)
print(list8)
#Response [10, 10.5, 'Anuj', 10, 10.5]

list9=[10,10.5,"Anuj",True,10,10.5,"Last Value"]
list9.pop()      # it will delete last element from list
print(list9)
#Response [10, 10.5, 'Anuj', True, 10, 10.5]


# #Extend
list10=[10,10.5,"Anuj",True,10,10.5]
list11=["Lamborgini","Mustang"]
list10.extend(list11)
print(list10)
#Response [10, 10.5, 'Anuj', True, 10, 10.5, 'Lamborgini', 'Mustang']

list11.extend(list10)
print(list11)
#Response ['Lamborgini', 'Mustang', 10, 10.5, 'Anuj', True, 10, 10.5, 'Lamborgini', 'Mustang']

# #Copy
list12=[10,10.5,"Anuj",True,10,10.5]
list13=list12.copy()
print(list13)
#Response [10, 10.5, 'Anuj', True, 10, 10.5]
# Another Way for Copy
list14=list12[:]       #list12[0:n-1]
print(list14)
#Response [10, 10.5, 'Anuj', True, 10, 10.5
list15=list12[0:3]       #copy 1st 3 elements from list
print(list15)
#Response [10, 10.5, 'Anuj']


# #Sort Method

list16=[7,3,9,5,34,1]
print(list16)
list16.sort()
print(list16)
#Response [7, 3, 9, 5, 34, 1]      [1, 3, 5, 7, 9, 34]


list16.sort(reverse=True)     #descending Order
print(list16)
#Response  [34, 9, 7, 5, 3, 1]
list16.sort(reverse=True)     # descending order
print(list16)
#Response [34, 9, 7, 5, 3, 1]

list16.sort(reverse=False)   #ascending order
print(list16)
#Response [1, 3, 5, 7, 9, 34]


list17=['a','t','w','d']
list17.sort()
print(list17)
#Response ['a', 'd', 't', 'w']

list18=['zensar','sagar','akalh','akanh']
list18.sort()
print(list18)
#Response ['akalh', 'akanh', 'sagar', 'zensar']


#     #reverse Method############

list19=[32,3,5,1,9,56]
list19.reverse()
print(list19)
#Response [56, 9, 1, 5, 3, 32]


#     ## Nested List ####

list20=[1,2,3,['surya',['jaysurya']]]
print(list20)
#Response [1, 2, 3, ['surya', ['jaysurya']]]


# # Tuple inside List
list21=[32,3,5,1,9,56,(1,2,"sagar")]

print(list21)
#Response [32, 3, 5, 1, 9, 56, (1, 2, 'sagar')]
list21.insert(4,(10,9,8))
print(list21)
#Response    [32, 3, 5, 1, (10, 9, 8), 9, 56, (1, 2, 'sagar')]


# #List comprehension

list22=['akash','anuj','aditya','sagar','sudarshan']
list23=[word for word in list22 if word.startswith('a')]
print(list23)
#Response      ['akash', 'anuj', 'aditya']



list24=[]
for word in list22:
    if word.startswith('s'):
        list24.append(word)
print(list24)
#Response            ['sagar', 'sudarshan']




#     ### lIST Unpacking####
list25=["Sagar","Saurabh"]
n1,n2=list25
print(n1)
print(n2)
#Response         Sagar       Saurabh