'''

*********** Dictionary ***************


Dictionary is Collection of Key Value Pairs

Syntax:
dict_name={ "key":"value"}
a={ "Name" : "Sagar", "Age": 22 }

IMP NOTES
1. Indexing and Slicing does Not Work
2. Insertion order is Preserved
3. Hetrogenious Elements are Allowed
4. Mutable in Nature
5. Key Must be Unique,but Duplicate Values are allowed
'''

'''Empty Dictionary'''
dict1={}
print(type(dict1))
#Response <class 'dict'>

'''Key Must be Unique,but Duplicate Values are allowed '''
dict2= {"name":"Sagar","age":22, "Username" : "Sagar"}
print(dict2)
# Response {'name': 'Sagar', 'age': 22, 'Username': 'Sagar'}

dict3={"name":"Sagar","age":22, "name": "akash"} #Wrong
print(dict3)
#Response {'name': 'akash', 'age': 22} which is Wrong

'''Key method
It gives all Keys contains in Dictionary'''
dictX={"name":"Sagar","age":22, "username" : "Sagar"}
print(dictX.keys())
# Response is dict_keys(['name', 'age', 'username'])

''' Values Method
It gives all Values Contains in Dictionary'''

dictY={"name":"Sagar","age":22, "username" : "Sagar"}
print(dictY.values())
# Response is dict_values(['Sagar', 22, 'Sagar'])


'''Pop Methods '''
dict4= {"name":"Sagar","age":22, "Username" : "Sagar"}
dict4.pop("age")
print(dict4)
#Response {'name': 'Sagar', 'Username': 'Sagar'}

'''get method 
It gives the Values of Given key '''
dict5= {"name":"Sagar","age":22, "Username" : "Sagar"}
print(dict5.get("age"))
# Response 22
print(dict5.pop("Username"))
#Response Sagar
print(dict5.get("Sagar")) # Wrong Input "It doesnot get values from values ";
# Response None

'''Clear Method
It clears the Dictionary '''
dict6={"name":"Sagar","age":22, "Username" : "Sagar"}
dict6.clear()
print(dict6)
# Response {} It gives Empty Dictionary


'''Items Method 
which returns list of (key, value) tuple  '''

dict7={"name":"Sagar","age":22, "username" : "Saggy123"}
print(dict7.items())
# Response dict_items([('name', 'Sagar'), ('age', 22), ('username', 'Saggy123')])    Which are List of "TUPLES"

'''Modify Values from Dictionary'''
dict8={"name":"Sagar","age":22, "username" : "Sagar"}
dict8["age"]=30
print(dict8)
# Response {'name': 'Sagar', 'age': 30, 'username': 'Sagar'}


'''Update the dictionary'''
dict9={"name":"Sagar","age":22, "username" : "Sagar"}
dict9.update({ "Location" : "Solapur" })
print(dict9)
#Response {'name': 'Sagar', 'age': 22, 'username': 'Sagar', 'Location': 'Solapur'}
