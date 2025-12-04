#Example1: creating dictionary
# mydic={101:"x",102:"y",103:"z"}
# print(mydic) #{101: 'x', 102: 'y', 103: 'z'}

# Example2: access items from dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2021
# }
# print(mydic["brand"])  # Hyudai
# print(mydic["model"]) #i10
# # using get()
# print(mydic.get("brand")) #Hyudai

#Example3: change values in dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
# }
# print(mydic) # {'brand': 'Hyudai', 'model': 'i10', 'year': 2020}
# mydic["year"]=2021    # new value
# print(mydic) #{'brand': 'Hyudai', 'model': 'i10', 'year': 2021}

#Example4: reading items from dictionary using loop
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
# }
#
# for i in mydic:
#     print(i)   # prints only keys from dictionary
#
# for i in mydic:
#     print(mydic[i])    # prints only values from dictionary

# for i in mydic.values():
#     print(i)  # prints only values from dictionary

# for x,y in mydic.items():
#     print(x,y)    # print keys along with the value

#Example5: check key is exist in dictionary or not
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
#
# if "model1" in mydic:
#     print("exist")
# else:
#     print("not exist")

# print("model" in mydic)  # True

#Example6: find number of items in dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
# print(len(mydic))  #3

#Example7: Adding items to dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
# mydic["color"]="red"
# print(mydic) #{'brand': 'Hyudai', 'model': 'i10', 'year': 2020, 'color': 'red'}

#Example8: Remove item from dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
# mydic.pop("year")
# print(mydic) # {'brand': 'Hyudai', 'model': 'i10'}

# del mydic["year"]
# print(mydic) #{'brand': 'Hyudai', 'model': 'i10'}

# del mydic
# print(mydic) #NameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic)   # {}

# Example9: copying dictionary
mydic1={
    "brand": "Hyudai",
    "model": "i10",
    "year": 2020
 }

# using copy()
mydic2=mydic1.copy()
print(mydic2) # {'brand': 'Hyudai', 'model': 'i10', 'year': 2020}

# without using copy()
# mydic2=mydic1
# print(mydic2) #{'brand': 'Hyudai', 'model': 'i10', 'year': 2020}