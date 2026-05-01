import numpy as np

# Using array(iterable)
arr = np.array([1,2,3,4])
print("Array created using list:")
print(arr)

# Using arange(start,stop,step)
odd = np.arange(1,20,2)     # 1 se 20 tk k odd numbers print karo, it include value start but not stop
print("Odd numbers between 1 and 20:")
print(odd)

# UserInput Array
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of cols: "))
# my_list = []
# for i in range(rows):
#     my_list.append([])
#     for j in range(cols):
#         my_list[i].append(int(input("Enter a number: ")))

# my_arr = np.array(my_list)
# print(my_arr)


## Another Method
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of cols: "))

# my_list = []

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(int(input("Enter a number: ")))
#     my_list.append(row)
# my_arr = np.array(my_list)
# print(my_arr)

## pythonic way 
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))
new_arr = np.array([[int(input("Enter a number: ")) for j in range(cols)] for i in range(rows)])
print(new_arr)