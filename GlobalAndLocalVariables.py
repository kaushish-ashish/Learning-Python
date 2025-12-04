#Example1
# global_var=20   # global variable
#
# def func():
#     local_var=10  # local variable
#     print(local_var)
#     print(global_var)
#
# func()
#
# #print(local_var)  # invalid bcoz local_var is local varaible of func()
# print(global_var)  # valid bcoz global_var is global variable

#Example2:
# xy=100  # global variable
#
# def cool():
#     xy=200   # Local variable
#     print(xy)
#
# cool()  #200

#Example3: Using Global variable in Local variable and update value
# xy=100  # global variable
#
# def cool():
#     #global xy=200  # invalid syntax
#     global xy
#     xy=200   # global variable
#     print(xy)
#
# cool()  #200
# print(xy)



#Example4:
# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
#
# #cool()   # 500
# print(x)  #100

#Example5:
#There is no need to declare global variables outside the function.
#You can declare them global inside the function. - global

def cool():
    global x
    x=100
    print(x)

cool()
print(x)  # able to access x bcoz it is global variable









