# #Reverse String || Reverse String || Reverse String || Reverse String ||

# text="My name is sagar"
# words=text.split()
# reversed_word=[]
# for word in words:
#     reversed_word.append(word[::-1])
# output=" ".join(reversed_word)
# print(output)



# #palindrom and Non Palindrom || palindrom and Non Palindrom ||palindrom and Non Palindrom || palindrom and Non Palindrom

# word= input("nter a word:")
#
# if word ==word[::-1]:
#     print("Given Word id Palindrom")
# else:
#     print(f"Given '{word}' is Not Palindrom")



##Common Letter Between 2 String || Common Letter Between 2 StringCommon Letter Between 2 String || Common Letter Between 2 String

# stl1=input("enter stl1: ")
# stl2=input("enter stl2: ")
#
# s1=set(stl1)
# s2=set(stl2)
#
# common_letter=s1 & s2
# print(common_letter)
#
# # commonLette2=s1.intersection(s2)
# # print(commonLette2)



# #Repeated character in String or LIST ||Repeated character in String or LIST
#
# str=input("Enter a string: ")
# repeat={}
#
# for char in str:
#     if str.count(char)>1:
#         repeat[char]=str.count(char)
# print(repeat)
#
# #OR||OR
#
# a=["banana","apple","apple"]
# repeat={}
# for i in a:
#     if a.count(i)>1:
#         repeat[i]=a.count(i)
# print(repeat)


#Number of character in String or Number of Item in List

# a=["berry","apple","Mango","apple","Mango","cherry"]
# repeat={}
#
# for i in a:
#     repeat[i]=a.count(i)
# print(repeat)
#
#
# # convert two Lists in Dictionary
#
# keys=[1,2,3]
# values=["one","two","three"]
#
# result=dict(zip(keys,values))
# print(result)
#




# # Convert Dictionary to Tupple
# x={1: 'one', 2: 'two', 3: 'three'}
#
# for i in x.items():
#     print(i)





# import re
# str="S10a29g123q12345r"
# list1=re.findall(r'\d+',str)
# print(list1)
# list2=list(map(int,list1))
# print(list2)


l1 = [3, 5, 1, 6, 3, 4]
l2 = [1, 7, 2, 3, 4, 5]

merged=l1+l2

print(merged)
unique=set(merged)
print(unique)
uniqlist=list(unique)
print(uniqlist)
# sortlist=sorted(uniqlist,reverse=True)
sortlist =uniqlist.sort(reverse =True)
print(sortlist)