
'''
 ************** Tuple **************

 Tuppleis data structure which is also callef collection of items
in which we can store anything like String, Float, Integer

OR
A Tupple is Immutable Data type in Python

Syntax:-
tupple_name=(item 1, item 2,............,item n)

@ Dupplicate values are allowed
@ Immutable in Nature              <-- iMPORTANT

'''

a=()               #'''Empty Tupple'''
print(type(a))
#Response <class 'tuple'>

x=(1,5, 10.5, 1, 5, 'sagar',True,'sagar')
print(x)
#Response (1, 5, 10.5, 1, 5, 'sagar', True, 'sagar')

b=1,2,3,'sagar'      # IMPORTANT
print("b is a :",type(b))
print(b)
# Response      b is a : <class 'tuple'>            (1, 2, 3, 'sagar')



'''Tupple with single element'''
c=10,         # Single element tupple always write with , at the end
print(c)

d=(10,)
print(d)
# Response       (10,)        (10,)



'''Copy Tupple in another Tupple'''

tupple1=(1,2,'Ajinkya')
tupple2=tupple1
print(tupple2)
print(tupple1)
#Response       (1, 2, 'Ajinkya')               (1, 2, 'Ajinkya')

''' Methods'''

# Count
print(tupple1.count(2))
print(x.count(5))
print(x.count('sagar'))
# Response  1  2   2


#Index
print(x.index('sagar'))
# Response    5