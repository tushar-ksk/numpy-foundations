import numpy as np

# Zeros Array
arr_z = np.zeros((3,3,3))
print(arr_z)

# Ones Array
arr_o = np.ones((3,2,3))
print(arr_o)

# random Array
arr_r = np.random.random((2,3))
print(arr_r)

# Full Array
arr_f = np.full((2,3), 5)
print(arr_f)

# Identity Array
arr_i = np.eye(4)
print(arr_i)

# Diagonal Array
arr_d = np.diag([1,2,3,4])
print(arr_d)

# Empty Array
arr_e = np.empty((2,3))  # uninitialized array, it may contain garbage values, it is faster than zeros and ones because it does not initialize the values
print(arr_e)

# Using linspace(start,stop,num)
even = np.linspace(2,20,10)   # 2 se 20 tk k 10 elements print karo equally spaced, it include both values start and stop
print("Even numbers between 2 and 20:")
print(even)

# Using vander(start,stop)
vander_arr = np.vander([1,2,3], 5)  # 1,2,3 ki powers 0 se 4 tk print karo column wise, 5 is the number of columns (powers) to be printed
print("Vandermonde array:")
print(vander_arr)

vander_linspace = np.vander(np.linspace(1,3,5), 5)  # 1 se 3 tk k 5 elements print karo equally spaced, unki powers 0 se 4 tk print karo column wise
print("Vandermonde array using linspace:")
print(vander_linspace)