#Example1  : how to create list

# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple",10,"banana",20]
# mylist=list()  # empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

#Example2 : Accessing items from the list
# mylist=["apple","banana","cherry"]     # idex starts from 0
#
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

#Example3: Range of indexes
# mylist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[2:5])  #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1]) #['orange', 'kiwi', 'melon']

#Example4: change item value
# mylist=["apple", "banana", "cherry"]
# print(mylist) #['apple', 'banana', 'cherry']
# mylist[0]="orange"  # this will change the values based on index
# print(mylist)  ['orange', 'banana', 'cherry']

#Example5: read the list items using loop
# mylist=["apple", "banana", "cherry"]
# for i in mylist:
#     print(i)

#Examplr6: check if the item is exist in the list or not
# mylist=["apple", "banana", "cherry"]
#
# if "apple" in mylist:
#     print("yes. apple is present")
# else:
#     print("No, apple is not present")


#Example7:List Length (counting number of items in a list)
# mylist=["apple", "banana", "cherry"]
# print(len(mylist))  #3


#Example8: Add items  append()  insert()
# mylist=["apple", "banana", "cherry"]
# #mylist.append("orange") # adding new item at the end of the list
# mylist.insert(1,"orange")  # add item some where in the middle of the list based on the index
# print(mylist)

#Example9: remove item from the list
#pop()
# mylist=["apple", "banana", "cherry"]
# mylist.pop(0) # here we should specify index not the value
# print(mylist) #['banana', 'cherry']

#del
# mylist=["apple", "banana", "cherry"]
# del mylist[2]      #here del command removes single item based on the index
# print(mylist) #['apple', 'banana']

#clear()
# mylist=["apple", "banana", "cherry"]
# mylist.clear()
# print(mylist) #[]

#Example10 : copy list
#list()
# mylist1=["apple", "banana", "cherry"]
# mylist2=list(mylist1)
# print(mylist1)  #['apple', 'banana', 'cherry']
# print(mylist2)  #['apple', 'banana', 'cherry']

#copy()
mylist1=["apple", "banana", "cherry"]
mylist2=mylist1.copy()
print(mylist1)  #['apple', 'banana', 'cherry']
print(mylist2)  #['apple', 'banana', 'cherry']

#Example11: combine/join lists
# using + operator
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3) #['a', 'b', 'c', 1, 2, 3]

#using loop statement
# list1=["a","b","c"]
# list2=[1,2,3]
#
# for i in list2:
#     list1.append(i)
# print(list1) #['a', 'b', 'c', 1, 2, 3]

#using extend()
# list1=["a","b","c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1) #['a', 'b', 'c', 1, 2, 3]


#  lists comparison
mylist1=[10,20,30]
mylist2=[10,20,30]

if mylist1==mylist2:
    print("lists are equal")
else:
    print("lists are not eqaul")