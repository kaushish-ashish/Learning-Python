#Example1 : creating set
# myset={"apple","banana","cherry"}
# print(myset) #{'banana', 'cherry', 'apple'}

#Example2: Accessing items from set
# myset={"apple","banana","cherry"}
# for i in myset:
#     print(i)

#Example3: value exists in set or not
# myset={"apple","banana","cherry"}
# print("banana" in myset)  # true
# print("banana2" in myset)  # false

#Example4: adding items to set
# add()-add single item    update()-add multiple items
# myset={"apple","banana","cherry"}
# #myset.add("orange")
# myset.update(["mango","grapes"])
# print(myset) #{'orange', 'banana', 'apple', 'cherry'}
#                 #{'apple', 'banana', 'mango', 'grapes', 'cherry'}

#Example5: find number of items in a set - len()
# myset={"apple","banana","cherry"}
# print(len(myset)) #3


#Example6: remove item from set - remove() discard()
#myset={"apple","banana","cherry"}
# myset.remove("banana")
# print(myset) # {'cherry', 'apple'}
# myset.remove("xyz")  # KeyError: 'xyz'

# myset.discard("banana")
# print(myset) #{'apple', 'cherry'}
# myset.discard("xyz")   # will not throw any error

#Example7 : clear all items from set
# myset={"apple","banana","cherry"}
# myset.clear()
# print(myset)  #set()
#
# del myset
# print(myset) #NameError: name 'myset' is not defined

#Example8: joining 2 sets  - union()
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)  #{1, 2, 'b', 3, 'c', 'a'}

#update()
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1) # {'b', 1, 2, 3, 'c', 'a'}










